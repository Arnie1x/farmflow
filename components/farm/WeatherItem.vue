<template>
  <div class="flex flex-col items-center p-2 w-min min-w-[5rem]">
    <NuxtImg :src="`https://openweathermap.org/img/wn/${weather.weather[0].icon}@2x.png`" alt="weather" class="w-[4rem] drop-shadow-xl" />
    <p class="text-2xl">{{ Math.round(weather.temp) }}°C</p>
    <p class="text-[#848AA0] text-sm">{{ getTimeDate(weather.dt) }}</p>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  weather: {
    type: Object,
    required: true
  }
})

function getTimeDate(epoch: string) {
  const time = new Date(epoch * 1000).toLocaleString('default', { hour: 'numeric', minute: 'numeric' });
  return time
}

</script>

<style>

</style>