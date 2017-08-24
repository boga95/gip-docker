<template>
  <div id="app">
    <h2> {{ title }} </h2>
    <h3>Play the rock-paper-scissors game against computer.</h3>
    <input type="radio" id="rock" value="rock" v-model="picked">
    <label for="rock">Rock</label>
    <br>
    <input type="radio" id="paper" value="paper" v-model="picked">
    <label for="paper">Paper</label>
    <br>
    <input type="radio" id="scissors" value="scissors" v-model="picked">
    <label for="scissors">Scissors</label>
    <br>
    <button v-on:click="submitInput">Submit</button>
    <h3 v-if="resultAvailable"> {{result}} </h3>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'app',
  data: function () {
    return {
      title: 'Rock-paper-scissors game!',
      picked: 'rock',
      result: '',
      resultAvailable: false
    }
  },
  methods: {
    submitInput: function () {
      axios.post('/submit', {
        picked: this.picked
      }).then(response => {
        this.result = response.data
        this.resultAvailable = true
      })
      alert(this.picked)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
