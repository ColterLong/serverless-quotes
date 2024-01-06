<script setup>
import { onMounted } from 'vue';
import Quote from './components/Quote.vue'

// const quotes = ref([])
const quotes = [{
  name: "test 1",
  text: "quote text 1"
}, {
  name: "test 2",
  text: "quote text 2"
}]

// onMounted(() => {
//   axios.get('api/getQuotes')
//     .then(res => {
//       console.log('hope there are quotes below')
//       console.log(res.data)
//       quotes.value = res.data
//     })
//     .catch(err => {
//       console.error('Error getting quotes: ', err)
//     })
// })
</script>


<template>
    <h1 class="title">Top 10 Famous Quotes</h1>
    <div class="quotes" v-for="quote in quotes">
      <Quote :name="quote.name" :text="quote.text" />
    </div>
</template>

<style scoped>

.title {
  color: #ececec;
}
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
