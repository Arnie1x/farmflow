<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Dashboard</h1>
    </template>
  </NuxtLayout>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth'
})
</script>

<style scoped>

</style>