<script setup>
import { ref, onMounted } from 'vue';
import Quote from './components/Quote.vue'
import axios from 'axios';

const quotes = ref([])
const loading = ref(true)

onMounted(() => {
  axios.get('api/getQuotes')
    .then(res => {
      // console.log('hope there are quotes below')
      // console.log(res.data)
      quotes.value = res.data
    })
    .catch(err => {
      console.error('Error getting quotes: ', err)
    })
    .finally(() => (loading.value = false))
})
</script>


<template>
    <h1 class="title">Top 5 Famous Quotes</h1>
    <div v-if="loading">
      <Quote :name="''" :text="'Loading...'" />
    </div>
    <div v-else>
      <div class="quotes" v-for="quote in quotes">
        <Quote :name="quote.name" :text="quote.text" />
      </div>
    </div>
</template>

<style scoped>

.title {
  color: #ececec;
  max-width: 800px;
}
</style>
