<script setup>
defineProps({
  name: String,
  text: String,
})

</script>

<template>
  <h1 class="read-the-docs">{{ name }}</h1>
  <p>{{ text }}</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
