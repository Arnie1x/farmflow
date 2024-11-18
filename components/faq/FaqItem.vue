<template>
  <div class="flex flex-col gap-3 w-full border-2 rounded-2xl p-5 pb-2 cursor-pointer" @click="isOpen = !isOpen">
    <p class="text-2xl font-bold">{{ question}}</p>
    <div v-auto-animate>
      <p v-if="isOpen" class="whitespace-pre-line">{{ answer }}</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  answer: {
    type: String,
    required: false,
    default: ''
  },
  question: {
    type: String,
    required: false,
    default: ''
  }
})

const isOpen = ref(false)
</script>

<style>

</style>