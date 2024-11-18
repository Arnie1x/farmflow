<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Chat</h1>
    </template>
    <ChatComponent />
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth'
})

</script>

<style scoped>
textarea {
  resize: none;
}
</style>