<script setup>
import { ref, onMounted } from 'vue';
import Quote from './components/Quote.vue'
import axios from 'axios';

const quotes = ref([])

onMounted(() => {
  axios.get('api/getQuotes')
    .then(res => {
      console.log('hope there are quotes below')
      console.log(res.data)
      quotes.value = res.data
    })
    .catch(err => {
      console.error('Error getting quotes: ', err)
    })
})
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
</style>
