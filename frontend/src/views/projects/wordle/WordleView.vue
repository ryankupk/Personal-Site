<script setup>
import axios from 'axios';
import BaseProjectView from '@/views/projects/BaseProjectView.vue';
import { ref, onMounted } from 'vue';
import { nextTick } from 'vue';

import { Tippy } from 'vue-tippy';
import 'tippy.js/dist/tippy.css'

import ToolTipInfo from '@/components/icons/ToolTipInfo.vue'

const maxGuesses = ref(6);
const wordLength = ref(5);
const words = ref(Array(maxGuesses.value).fill().map(() => Array(wordLength.value).fill('')));
const inputs = ref([]);
const possibleWords = ref([]);
const colors = ref(['gray', 'yellow', 'green']);
const colorIndices = ref(Array(maxGuesses.value).fill().map(() => Array(wordLength.value).fill(0)));
const rowDisabled = ref(Array(maxGuesses.value).fill(true));

const getPossibleWords = () => {
  possibleWords.value = ["loading..."]

  const guess_list = {};
  const guessesElements = Array.from(document.querySelectorAll(".guessInput"));

  const guessPattern = Array.from(guessesElements).map(input => {
    const notPresent = '!';
    const presentWrongPlace = '_';
    const presentCorrectPlace = ' ';

    if (input.classList.contains(colors.value[0])) {
      return notPresent;
    }
    else if (input.classList.contains(colors.value[1])) {
      return presentWrongPlace;
    }
    else if (input.classList.contains(colors.value[2])) {
      return presentCorrectPlace;
    }
  }).join('');
  const guessPatternWords = guessPattern.match(new RegExp(`.{${wordLength.value}}`, 'g'));

  const guessLetters = guessesElements.map(input => input.value.toLowerCase()); 
  let flag = true;
  for (let letter of guessLetters) {
    if (letter != '') {
      flag = false;
      break;
    }
  }
  if (flag) {
    possibleWords.value = [];
    return;
  }
  const guessString = guessLetters.join('');

  const words = guessString.match(new RegExp(`.{${wordLength.value}}`, 'g'));
  for (let i = 0; i < words.length; ++i) {
    guess_list[words[i]] = guessPatternWords[i];
  }

  axios.post('/api/wordle', {"guess_list": guess_list})
  .then((response) => {
    const possible_words = response.data.possible_words;
    if (possible_words.length == 1) {
      possible_words.push("🎉")
    }
    possibleWords.value = response.data.possible_words;
  })
  .catch((error) => {
    possibleWords.value = ["Invalid guess!"];
    // console.error('Failed to fetch possible words: ', error);
  })
}

const clearWord = async (wordIndex) => {

  for (let i = 0; i < words.value[wordIndex].length; ++i) {
    words.value[wordIndex][i] = '';
    colorIndices.value[wordIndex][i] = 0;
  }

  rowDisabled.value[wordIndex] = true;

  await nextTick();

  getPossibleWords();
}

const handleInput = async (event, wordIndex, charIndex) => {
  if (event.inputType === 'deleteContentBackward') { // don't move to the next box if backspacing
    return;
  }

  const nextCharIndex = charIndex + 1;
  if (nextCharIndex < words.value[wordIndex].length) {
    inputs.value[wordIndex * wordLength.value + nextCharIndex].focus();
  }
  else if (wordIndex < words.value.length - 1) {
    inputs.value[(wordIndex + 1) * wordLength.value].focus();
    await nextTick();
    getPossibleWords();
  }

  const rowFilled = words.value[wordIndex].every(char => char !== '');
  rowDisabled.value[wordIndex] = !rowFilled;
}

const handleBackspace = (event, wordIndex, charIndex) => {
  if (event.key !== "Backspace") {
    return;
  }

  const currentInput = inputs.value[wordIndex * wordLength.value + charIndex];
  currentInput.value = '';

  if (charIndex > 0) {
    inputs.value[wordIndex * wordLength.value + charIndex - 1].focus();
  } else if (wordIndex > 0) {
    inputs.value[(wordIndex - 1) * wordLength.value + wordLength.value - 1].focus();
  }

  const rowFilled = words.value[wordIndex].every(char => char !== '');
  rowDisabled.value[wordIndex] = !rowFilled;
}

const togglePresence = async (wordIndex, charIndex) => {
  colorIndices.value[wordIndex][charIndex] = (colorIndices.value[wordIndex][charIndex] + 1) % colors.value.length;
  await nextTick();
  getPossibleWords();
}

const getColorClass = (wordIndex, charIndex) => {
  const colorIndex = colorIndices.value[wordIndex][charIndex];
  return colors.value[colorIndex]
}

// const fillWord = (word) => {
//   console.log(word);
// }

onMounted(() => {
})


</script>

<template>
  <BaseProjectView>
    <div class="viewContainer">
      <div class="guessesContainer">
        <h4 class="guessHeader">Guesses&nbsp;<ToolTipInfo placement="top" content="Enter your guesses below the same as you entered them in Wordle" /></h4>
        <div class="guessContainer">
          <div class="guess" v-for="(word, wordIndex) in words" :key="wordIndex">
            <div class="inputContainer">
              <div v-for="(char, charIndex) in word" :key="charIndex" class="inputWrapper">
                <input
                  class="guessInput"
                  :class="getColorClass(wordIndex, charIndex)"
                  type="text"
                  autocapitalize="none"
                  autocorrect="off"
                  maxlength="1"
                  ref="inputs"
                  v-model="words[wordIndex][charIndex]"
                  @input="handleInput($event, wordIndex, charIndex)"
                  @keydown="handleBackspace($event, wordIndex, charIndex)"
                />
                <button :disabled="rowDisabled[wordIndex]" @click="togglePresence(wordIndex, charIndex)">ㅤ</button> <!-- this line contains an empty character for the text of the button -->
              </div>
            </div>
             <tippy content="Clear word" placement="right"><button @click="clearWord(wordIndex)">✗</button></tippy>
          </div>

        </div>
      </div>

      <div class="centeredDiv"></div>

      <div class="possibleContainer">
        <h4 class="possibleHeader">Possible&nbsp;words&nbsp;<ToolTipInfo placement="top" content="Below are possible words given the parameters in the 'Guesses'<br/><br/>They're sorted from most-likely to least-likely according to occurrence in English, however if none of the words are in the top 100,000 most used words, then they're arbitrarily sorted"/></h4>
        <div class="wordContainer">
          <div v-for="word in possibleWords" :key="word">
            {{ word }} <!-- <button @click="fillWord(word)">↵</button> -->
          </div>
        </div>
      </div>
    </div>
  </BaseProjectView>
</template>

<style lang="scss" scoped>
$guessInputSize: 30px;

.guessesContainer {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.guessHeader {
  margin-bottom: 20px;
}

.guessContainer {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 10px;
}

.guess {
  display: flex;
  align-items: center;
}

.inputContainer {
  display: grid;
  grid-template-columns: repeat(5, $guessInputSize);
  gap: 5px;
  margin-right: 10px;
}
.inputWrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.gray {
  background-color: #3a3a3c;
}
.yellow {
  background-color: #b59f3b;
}
.green {
  background-color: #538d4e;
}

.guessInput {
  width: 100%;
  height: $guessInputSize;
  text-align: center;
  color: #f8f8f8;
  border: none;
  margin: 8px;
  border-radius: 5px;
}

.wordContainer {
  margin-top: 15px;
  max-height: 300px;
  min-height: 300px;
  max-width: 300px;
  min-width: 200px;
  overflow-y: auto;
  justify-content: center;
  border: 1px solid gray;
  border-radius: 5px;
}

.centeredDiv {
  max-width: 15%;
  min-width: 10%;
}

.possibleContainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.wordContainer > div {
  text-align: center;
}

@media (min-width: 1024px) {
  .viewContainer {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
  }
}

@media (max-width: 1024px) {
  .viewContainer {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .centeredDiv {
    display: none;
  }
}
</style>
