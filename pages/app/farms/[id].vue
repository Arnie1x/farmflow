<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Farm: Sunny Fields</h1>
    </template>
    <div class="w-full h-full flex xl:flex-row flex-col gap-2">
      <div class="h-full w-full xl:max-w-[31.25rem] max-w-[64rem] flex flex-col gap-2">
        <AISummaryCard />
        <PendingActivitiesCard />
      </div>
      <div class="w-full h-full flex flex-col gap-2">
        <FarmWeatherCard />
        <ActivityLogsCard />
      </div>
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
import AISummaryCard from '~/components/AISummaryCard.vue';

definePageMeta({
  middleware: 'auth',
})
</script>

<style>

</style>