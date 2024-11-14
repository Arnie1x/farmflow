<template>
  <NuxtLink class="chat-link p-2 rounded-xl">
    <p class="text-ellipsis line-clamp-1">{{ title }}</p>
  </NuxtLink>
</template>

<script lang="ts" setup>
defineProps({
  id: {
    type: String,
    required: false,
    default: '0'
  },
  title: {
    type: String,
    required: false,
    default: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt ducimus odit nulla minus necessitatibus.'
  }
})
</script>

<style scoped>
.chat-link {
  transition: 0.5s all ease;
  cursor: pointer;
}

.chat-link:hover {
  background-color: #848aa04D;
}

.chat-link:active {
  background-color: #848aa0b0;
}
</style>