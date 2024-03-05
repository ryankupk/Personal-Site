from fastapi import APIRouter, HTTPException
from ..models.guess_list import GuessList
from ..config.settings import motor_details
from motor.motor_asyncio import AsyncIOMotorClient
from collections import defaultdict

router = APIRouter()

client = AsyncIOMotorClient(motor_details)
db = client.wordle
word_freq_collection = db.word_freq

def set_patterns(guess: str, pattern: str, correct: dict[str, int], in_word: defaultdict[str, list[int]], not_in_word: set) -> tuple[ dict[str, int], defaultdict[str, list[int]], set ]:
    guess = guess.upper()
    for idx, _ in enumerate(guess):
        # check that the letter at position[idx] is not in word
        # duplicate letters cannot be added to the list of letters not in the word if they were otherwise decided to be in the word and/or in the correct place
        if  pattern[idx] == "_" \
            and guess[idx].lower() not in correct.keys() \
            and (guess[idx].lower() not in in_word.keys() and guess[idx] not in guess[idx+1:]):
                not_in_word.add(guess[idx].lower())

        # check if the letter is in the word and correct place
        elif guess[idx] == pattern[idx]:
            correct[guess[idx].lower()] = idx 

        # check if the letter is in the word but not in the correct place
        elif guess[idx] == pattern[idx].upper():
            in_word[guess[idx].lower()].append(idx)

    return correct, in_word, not_in_word
        
        
def sort_possible_words(possible_words: list[str], word_frequency) -> list[str]:
    # list of words to return, starting with an arbitrary word in the list of possible words
    return_list: list[str] = [possible_words[0]]

    for possible_word in possible_words[1:]:
        for idx, return_word in enumerate(return_list):
            # if the frequency of the current possible word is less than or equal to the frequency of the current word in the list to be returned
            # and the current possible word is not already in the list
            if int(word_frequency[possible_word]) <= int(word_frequency[return_word]) and possible_word not in return_list:
                return_list.insert(idx-1 if idx > 0 else idx, possible_word)
                break
        # insert word into return_list only if it's not already in the list
        else:
            return_list.append(possible_word)

    return return_list

@router.post("/wordle")
async def return_possible_words(guesses: GuessList) -> dict[str, list[str]]:
    # dictionary of letters that are correct and their known positions
    correct: dict[str, int] = {}
    # dictionary of letters and positions that they are known to not be in
    in_word: defaultdict[str, list[int]] = defaultdict(list)
    # list of letters that are not in the word
    not_in_word = set()

    # dictionary of words and their frequency in English
    word_frequency = await word_freq_collection.find({}, {'_id': False}).next() # this collection has only one document
    all_words = set(word_frequency.keys())
    guess_set = set(guesses.guess_list.keys())
    # ensure all guesses are in the word list
    if len(guess_set.intersection(all_words)) != len(guess_set):
        raise HTTPException(status_code=400, detail="Invalid guess")

    for guess, pattern in guesses.guess_list.items():
        correct, in_word, not_in_word = set_patterns(guess, pattern, correct, in_word, not_in_word)

    possible_words: list[str] = []
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
            # skip word if (letter not in word) or ((letter in word) and (letter in known incorrect position))
            idx = word.find(letter)
            if idx == -1 or idx in positions:
                skip_word_flag = True
                break
        if skip_word_flag: continue

        # if any letters that are known to not be in the word are in the current word, skip it
        for letter in not_in_word:
            if letter in word:
                skip_word_flag = True
                break
        if skip_word_flag: continue

        # add current word to list of possible words if it passes all above checks
        possible_words.append(word)


    possible_words = sort_possible_words(possible_words, word_frequency)
    return {
        # "message": "Success",
        "possible_words": possible_words
        }
