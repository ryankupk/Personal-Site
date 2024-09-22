from fastapi import APIRouter, HTTPException, Depends
from asyncpg import Connection
from ..config.database import get_db
from ..models.guess_list import GuessList
from collections import defaultdict
import heapq

router = APIRouter()

def set_patterns(guess: str,
                 pattern: str,
                 correct: dict[str, int],
                 in_word: defaultdict[str, list[int]],
                 not_in_word: defaultdict[str, list[int]]
                 ) -> tuple[ dict[str, int], defaultdict[str, list[int]], dict[str, int] ]:

    for idx, _ in enumerate(guess):
        # '!' means not in word
        # '_' means present, in wrong place
        # ' ' means present, in right place

        # check that the letter at position[idx] is not in word
        # duplicate letters cannot be added to the list of letters not in the word if they were otherwise decided to be in the word and/or in the correct place
        if (
            pattern[idx] == "!"
            and guess[idx] not in correct.keys()
            ):
                not_in_word[guess[idx]].append(idx)

        # check if the letter is in the word and correct place
        elif pattern[idx] == ' ':
            correct[guess[idx]] = idx 

        # check if the letter is in the word but not in the correct place
        elif pattern[idx] == '_':
            in_word[guess[idx]].append(idx)

    return correct, in_word, not_in_word
        
def add_to_heap(heap, word, score, max_size=20):
    if len(heap) < max_size:
        heapq.heappush(heap, (score, word))
    elif score > heap[0][0]:
        heapq.heapreplace(heap, (score, word))

@router.get("/wordle")
async def return_possible_words(guess_list: str, conn: Connection = Depends(get_db)) -> dict[str, list[str]]:
    guesses = {}
    for guess in guess_list.split(','):
        word, pattern = guess.split(':')
        guesses[word] = pattern

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
    if len(guess_set.intersection(all_words)) != len(guess_set):
        raise HTTPException(status_code=400, detail="Invalid guess")

    for guess, pattern in guesses.items():
        correct, in_word, not_in_word = set_patterns(guess, pattern, correct, in_word, not_in_word)

    possible_words_heap = []
    for word in all_words:
        # flag to skip the word if it doesn't meet criteria that indicate that it could be a possible solution
        skip_word_flag = False
        
        # iterate across known letters and their positions
        for letter, position in correct.items():
            # skip word if a known letter is not in the right spot
            if word[position] != letter:
                skip_word_flag = True
                break
        if skip_word_flag: continue
        
        # iterate across letters that are known, and the positions that they're *not* in
        for letter, positions in in_word.items():
            # skip word if letter is not in word, or letter is in a known wrong position
            idx = word.find(letter)
            if idx == -1 or idx in positions:
                skip_word_flag = True
                break
        if skip_word_flag: continue

        # if any letters that are known to not be in the word are in the current word, skip it
        for position, letter in enumerate(word):
            if letter not in not_in_word:
                continue
            if letter not in correct:
                skip_word_flag = True
                break
            if position in not_in_word[letter]:
                skip_word_flag = True
                break
        if skip_word_flag: continue

        # add current word to list of possible words if it passes all above checks
        if not skip_word_flag:
            add_to_heap(possible_words_heap, word, int(word_frequency[word]))

    if len(possible_words_heap) == 0:
        raise HTTPException(status_code=400, detail="No possible words")

    # Extract top 20 words from the heap
    top_words = [word for _, word in sorted(possible_words_heap, reverse=True)]

    return {
        "possible_words": top_words
    }
