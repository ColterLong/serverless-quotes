<script setup>
defineProps({
  name: String,
  text: String,
})

</script>

<template>
  <main class="quote">
    <h1 class="title">{{ name }}</h1>
    <hr class="line"/>
    <p class="text">{{ text }}</p>
  </main>
</template>

<style scoped>
.quote {
  background-color: #385170;
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  margin: 16px;

}
.quote:hover {
  background-color: #547296;
}
/* .title {
  color: #9fd3c7;
} */
.title, .text {
  color: #ececec;
}

.line {
  border-color: #9fd3c7;
}
</style>
