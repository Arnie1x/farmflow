<template>
  <div class="w-full flex flex-col rounded-2xl border-2 p-5">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/weather.svg" alt="weather" class="w-[2.5rem]" />
      <p class="text-3xl font-bold text-[#2B9B3C]">Forecast</p>
    </div>
    <div>
      <!-- TODO :: Weather data here -->
    </div>
  </div>
</template>

<script lang="ts" setup>
import WeatherCache from '~/types/weather_cache';

const props = defineProps({
  latitude: {
    type: Number,
    required: true
  },
  longitude: {
    type: Number,
    required: true
  },
  limit : {
    type: Number,
    required: false,
    default: 5
  }
})

const runtimeConfig = useRuntimeConfig();
const openWeatherMapApiKey = runtimeConfig.public.openWeatherMapApiKey;

const weatherCache = new WeatherCache(openWeatherMapApiKey);

try {
  const weatherData = await weatherCache.getWeatherData({ longitude: props.longitude, latitude: props.latitude });
  console.log(weatherData);
} catch (error) {
  console.log(error);
}
// console.log(props.longitude, props.latitude);
// const weatherData = await weatherCache.getWeatherData({ longitude: props.longitude, latitude: props.latitude });
// console.log(weatherData);
</script>

<style>

</style>