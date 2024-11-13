<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Calendar</h1>
    </template>
    <div class="flex flex-col gap-3">
      <p class="text-2xl font-bold">November</p>
      <CalendarItem />
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth'
})
</script>

<style scoped>

</style>