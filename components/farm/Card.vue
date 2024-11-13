<!-- eslint-disable vue/html-self-closing -->
<template>
  <NuxtLink :to="{ name: 'app-farms-id', params: { id: farm['id'] }}">
    <div class="h-[18.75rem] max-w-[31.25rem] min-w-[18.75rem] rounded-2xl border-2 flex flex-col justify-between gap-2">
      <div class="w-full h-full p-3">
        <FarmWeatherList :latitude="farm.location.coordinates[1]" :longitude="farm.location.coordinates[0]" :limit="8" />
      </div>
      <div class="border" />
      <div class="w-full h-full p-3 flex flex-col">
        <p class="text-2xl font-bold">{{ farm['name'] }}</p>
        <div class="flex flex-row gap-2 justify-start">
          <NuxtImg src="/images/icons/location.svg" alt="location" class="w-[1.25rem]" />
          <p class="text-base font-bold text-[#848AA0]">{{ farm['location']['full_address'].split(',').reverse()[1] }}</p>
        </div>
        <div class="flex flex-row gap-2 justify-start items-center h-full">
          <NuxtImg src="/images/icons/alert.svg" alt="location" class="w-[1.25rem]" />
          <p v-if="eventCount > 0" class="text-base font-bold text-[#D36135]">{{ eventCount }} Activities Pending</p>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script lang="ts" setup>

const props = defineProps({
  farm: {
    type: Object,
    required: true
  }
})

const client = useSupabaseClient();
const today = new Date();
const threeDaysFromNow = new Date(today.getTime() + 3 * 24 * 60 * 60 * 1000).toISOString();
const eventCount = ref(0)

eventCount.value = await getEventsCount()
// console.log(props.farm.id.toString())

async function getEventsCount() {
  try {
    let { data: count, error } = await client
    .from('events')
    .select('id') // select only the id column to reduce data transfer
    .eq('farm_id', props.farm.id.toString())
    .eq('is_completed', false)
    .lte('end_date', threeDaysFromNow)

    if (error) {  
      throw error
    }
    if (!count) {
      return 0
    }
    return count?.length;
} catch (error) {
  console.log(error)
}
}
</script>

<style>

</style>