<script setup>
import axios from 'axios';
import BaseProjectView from '@/views/projects/BaseProjectView.vue';
import { ref, onMounted } from 'vue';
// import { nextTick } from 'vue';

const maxGuesses = ref(6);
const wordLength = ref(5);
const words = ref(Array(maxGuesses.value).fill().map(() => Array(wordLength.value).fill('')));
const inputs = ref([]);
const possibleWords = ref([]);
const colors = ref(['gray', 'yellow', 'green']);
const colorIndices = ref(Array(maxGuesses.value).fill().map(() => Array(wordLength.value).fill(0)));
const rowDisabled = ref(Array(maxGuesses.value).fill(true));

const getPossibleWords = () => {
  const guess_list = {};
  const guessesElements = Array.from(document.querySelectorAll(".guessInput"));
  console.log(guessesElements)
  const guessPattern = Array.from(guessesElements).map(input => {
    if (input.classList.includes(colors.value[0])) {
      return '!'; // not present - gray
    }
    else if (input.classList.includes(colors.value[1])) {
      return '_'; // present, wrong place - yellow
    }
    else if (input.classList.includes(colors.value[2])) {
      return ' '; // present, correct place - green
    }
  })
  console.log(guessPattern)
  const guessLetters = guessesElements.map(input => input.value); 
  const guessString = guessLetters.join('');
  const words = guessString.match(new RegExp(`.{${wordLength.value}}`, 'g'));
  words.forEach(word => {
    guess_list[word] = '_____'
  })

  axios.post('/api/wordle', {"guess_list": guess_list}).then((response) => {
    possibleWords.value = response.data.possible_words
  })
}

const handleInput = (event, wordIndex, charIndex) => {
  if (event.inputType === 'deleteContentBackward') { // don't move to the next box if backspacing
    return;
  }

  const nextCharIndex = charIndex + 1;
  if (nextCharIndex < words.value[wordIndex].length) {
    inputs.value[wordIndex * wordLength.value + nextCharIndex].focus();
  }
  else if (wordIndex < words.value.length - 1) {
    inputs.value[(wordIndex + 1) * wordLength.value].focus();
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

const togglePresence = (wordIndex, charIndex) => {
  colorIndices.value[wordIndex][charIndex] = (colorIndices.value[wordIndex][charIndex] + 1) % colors.value.length;
  getPossibleWords();
}

const getColorClass = (wordIndex, charIndex) => {
  const colorIndex = colorIndices.value[wordIndex][charIndex];
  return colors.value[colorIndex]
}

onMounted(() => {
})


</script>

<template>
  <BaseProjectView>
    <div class="viewContainer">
      <div class="guessesContainer">
        <h4 class="guessHeader">Guesses</h4>
        <div class="guessContainer">
          <div class="guess" v-for="(word, wordIndex) in words" :key="wordIndex">
            <div class="inputContainer">
              <div v-for="(char, charIndex) in word" :key="charIndex" class="inputWrapper">
                <input
                  class="guessInput"
                  :class="getColorClass(wordIndex, charIndex)"
                  type="text"
                  maxlength="1"
                  ref="inputs"
                  v-model="words[wordIndex][charIndex]"
                  @input="handleInput($event, wordIndex, charIndex)"
                  @keydown="handleBackspace($event, wordIndex, charIndex)"
                />
                <button :disabled="rowDisabled[wordIndex]" @click="togglePresence(wordIndex, charIndex)">x</button>
              </div>
            </div>
            <button @click="getPossibleWords">lock in</button>
            <button @click="getPossibleWords">clear</button>
          </div>

        </div>
      </div>

      <div class="possibleContainer">
        <h4 class="possibleHeader">Possible words</h4>
        <div class="wordContainer">
          <div v-for="word in possibleWords" :key="word">
            {{ word }}
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
}

.wordContainer {
  max-height: 300px;
  min-height: 300px;
  overflow-y: auto;
  justify-content: center;
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
}
</style>
