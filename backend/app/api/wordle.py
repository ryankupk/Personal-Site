from fastapi import APIRouter, HTTPException, Depends, status
from asyncpg import Connection
from ..config.database import get_wordle_db
from ..models.guess_list import GuessList
from collections import defaultdict
import heapq

router = APIRouter()

def set_patterns(guess: str,
                 pattern: str,
                 correct: dict[str, int],
                 in_word: defaultdict[str, list[int]],
                 not_in_word: defaultdict[str, list[int]]
                 ) -> tuple[dict[str, int], defaultdict[str, list[int]], defaultdict[str, list[int]]]:
    """
    Pattern characters:
    ' ' (space) - Green: Correct letter in correct position
    '_' (underscore) - Yellow: Correct letter in wrong position
    '!' (exclamation) - Gray: Letter not in word

    Wordle rules (simplified):
    1. Green letters are marked first
    2. Yellow letters are marked left to right, not reusing letters
    3. Gray letters are marked for remaining positions
    """

    letter_count = defaultdict(int)
    for idx, letter in enumerate(guess):
        if pattern[idx] in [' ', '_']:
            letter_count[letter] += 1

        if pattern[idx] == ' ':
            correct[letter] = idx
        elif pattern[idx] == '_':
            in_word[letter].append(idx)
        elif pattern[idx] == '!' and letter not in letter_count:
            not_in_word[letter].append(idx)

    return correct, in_word, not_in_word
        
def add_to_heap(heap, word, score, max_size=20):
    if len(heap) < max_size:
        heapq.heappush(heap, (score, word))
    elif score > heap[0][0]:
        heapq.heapreplace(heap, (score, word))

@router.get("/wordle")
async def return_possible_words(guess_list: str, conn: Connection = Depends(get_wordle_db)) -> dict[str, list[str]]:
    if not guess_list:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty guess list")

    guesses = {}
    for guess in guess_list.split(','):
        try:
            word, pattern = guess.split(':')
            if not all(c in ' _!' for c in pattern) or len(word) != len(pattern):
                raise ValueError(f"Invalid pattern format for guess: {guess}")
            guesses[word] = pattern
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    for word, pattern in guesses.items():
        if pattern == ' ' * len(pattern):
            return {  # return if the word given is indicated to be the answer
                "possible_words": [word]
            }

    # dictionary of letters that are correct and their known positions
    correct: dict[str, int] = {}
    # dictionary of letters and positions that they are known to not be in
    in_word: defaultdict[str, list[int]] = defaultdict(list)
    # list of letters that are not in the word
    not_in_word: defaultdict[str, list[int]] = defaultdict(list)

    # dictionary of words and their frequency in English
    rows = await conn.fetch(
        'SELECT * FROM words'
    )
    all_words = set()
    word_frequency = {}
    for row in rows:
        all_words.add(row['word'])
        word_frequency[row['word']] = row['score']

    guess_set = set(guesses.keys())
    # ensure all guesses are in the word list
    invalid_guesses = guess_set - all_words
    if invalid_guesses:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Invalid guesses: {', '.join(invalid_guesses)}")

    for guess, pattern in guesses.items():
        correct, in_word, not_in_word = set_patterns(guess, pattern, correct, in_word, not_in_word)

    possible_words_heap = []
    for word in all_words:
        skip_word_flag = False
        letter_count = defaultdict(int)

        for letter, position in correct.items():
            if word[position] != letter:
                skip_word_flag = True
                break
            letter_count[letter] += 1
        if skip_word_flag:
            continue

        for letter, positions in in_word.items():
            if letter not in word:
                skip_word_flag = True
                break
            for pos in positions:
                if word[pos] == letter:
                    skip_word_flag = True
                    break
            if skip_word_flag:
                break
            letter_count[letter] += 1
        if skip_word_flag:
            continue

        for letter, positions in not_in_word.items():
            if letter in word and letter_count[letter] == 0:
                skip_word_flag = True
                break
        if skip_word_flag:
            continue

        # add current word to list of possible words if it passes all above checks
        if not skip_word_flag:
            add_to_heap(possible_words_heap, word, int(word_frequency[word]))

    if len(possible_words_heap) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No possible words found")

    # Extract top 20 words from the heap
    top_words = [word for _, word in sorted(possible_words_heap, reverse=True)]

    return {
        "possible_words": top_words
    }
