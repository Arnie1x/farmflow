<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">New Farm</h1>
    </template>
    <form class="w-full h-full flex xl:flex-row flex-col gap-3">
      <div class="flex flex-col gap-3 max-w-[64rem] w-full">
        <input id="farm_name" type="text" class="text-black textfield" name="farm_name" placeholder="Farm Name *">
        <input id="location" type="text" class="text-black textfield" name="location" placeholder="Location *">
        <input id="area_size" type="number" class="text-black textfield" name="area_size"
        placeholder="Area Size (in Ha) *">
      </div>
      <button class="text-white button h-min xl:max-w-[25rem]">Create Farm</button>
    </form>
  </NuxtLayout>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth',
})
</script>

<style></style>