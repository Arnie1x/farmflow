<template>
  <NuxtLink :to="{ name: 'app-farms-id-events-event_id', params: { id: event.farm_id, event_id: event.id } }">
    <div class="w-full flex flex-row justify-between items-center">
      <div class="flex flex-col justify-center items-center px-8 pr-14 min-w-[10rem]">
        <p class="text-4xl font-bold text-[#D36135]">{{ getDayDate(event.end_date) }}</p>
        <p class="text-[#848AA0]">{{ getTimeDate(event.end_date) }}</p>
      </div>
      <div class="h-[4rem] border border-gray-400" />
      <div class="flex w-full items-center justify-center">
        <p class="text-2xl text-ellipsis p-3">{{ event.name }}</p>
      </div>
    </div>
  </NuxtLink>
</template>

<script lang="ts" setup>
defineProps({
  event: {
    type: Object,
    required: true
  }
})

function getDayDate(date) {
  const day = new Date(date).toLocaleString('default', { day: 'numeric' });
  return day
}

function getTimeDate(date) {
  const time = new Date(date).toLocaleString('default', { hour: 'numeric', minute: 'numeric' });
  return time
}
</script>

<style></style>