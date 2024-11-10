<!-- eslint-disable vue/first-attribute-linebreak -->
<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">New Farm</h1>
    </template>
    <FarmForm />
  </NuxtLayout>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth',
})



</script>

<style></style>