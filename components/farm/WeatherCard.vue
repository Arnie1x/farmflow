<template>
  <div class="flex flex-col rounded-2xl border-2 p-5">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/weather.svg" alt="weather" class="w-[2.5rem]" />
      <p class="text-3xl font-bold text-[#2B9B3C]">Forecast</p>
    </div>
    <div class="grow overflow-x-auto overscroll-none items-end">
      <div class="flex gap-2 justify-start items-start pt-2 max-w-[1rem]">
        <div v-for="weather in filteredWeatherData" :key="weather.id">
          <FarmWeatherItem :weather="weather" />
           <!-- <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus rem iusto magnam nam, minima maxime ab eius quidem culpa modi tenetur officia non dolorem reprehenderit perferendis, quibusdam laudantium similique. Corporis aperiam error odit exercitationem nihil pariatur optio quasi molestiae nisi voluptas! Tempora esse ullam ducimus dolor nemo voluptatum sequi repudiandae tenetur vel, reprehenderit provident, officia aspernatur nisi. Voluptas, iure velit.</p> -->
        </div>
      </div>
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

const filteredWeatherData = ref([]);

const runtimeConfig = useRuntimeConfig();
const openWeatherMapApiKey = runtimeConfig.public.openWeatherMapApiKey;

const weatherCache = new WeatherCache(openWeatherMapApiKey);

try {
  const weatherData = await weatherCache.getWeatherData({ longitude: props.longitude, latitude: props.latitude });
  filteredWeatherData.value = filterWeatherData(weatherData, props.limit);

} catch (error) {
  console.log(error);
}


function filterWeatherData(weatherData: any, limit: number): any[] {
  const filteredData = [];
  const currentTime = Math.floor(Date.now() / 1000); // get current time in epoch
  for (let i = 0; i < weatherData.forecast_data.hourly.length; i++) {
    const hourData = weatherData.forecast_data.hourly[i];
    const hourTime = hourData.dt;

    if (hourTime >= currentTime && filteredData.length < limit) {
      filteredData.push(hourData);
    }
  }

  return filteredData;
}
</script>

<style>

</style>