<template>
  <h1 class="p-5 text-xl">Homepage</h1>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth'
})

navigateTo('/app')
</script>

<style></style>