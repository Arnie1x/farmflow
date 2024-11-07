<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Farms</h1>
    </template>
    <div class="w-full h-full grid xl:grid-cols-3 lg:grid-cols-2 grid-cols-1 gap-2">
      <FarmCard />
      <FarmCard />
      <FarmCard />
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth',
})
</script>

<style scoped>

</style>