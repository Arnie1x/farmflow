<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Farm: {{ farm.name }}</h1>
      <NuxtLink :to="{ name: 'app-farms-id-edit', params: { id: farm.id } }" class="button-outlined flex flex-row gap-3 justify-center items-center">
        <svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M13 3.5C13.2549 3.50028 13.5 3.59788 13.6854 3.77285C13.8707 3.94782 13.9822 4.18695 13.9972 4.44139C14.0121 4.69584 13.9293 4.94638 13.7657 5.14183C13.6021 5.33729 13.3701 5.4629 13.117 5.493L13 5.5H5V19.5H19V11.5C19.0003 11.2451 19.0979 11 19.2728 10.8146C19.4478 10.6293 19.687 10.5178 19.9414 10.5028C20.1958 10.4879 20.4464 10.5707 20.6418 10.7343C20.8373 10.8979 20.9629 11.1299 20.993 11.383L21 11.5V19.5C21.0002 20.0046 20.8096 20.4906 20.4665 20.8605C20.1234 21.2305 19.6532 21.4572 19.15 21.495L19 21.5H5C4.49542 21.5002 4.00943 21.3096 3.63945 20.9665C3.26947 20.6234 3.04284 20.1532 3.005 19.65L3 19.5V5.5C2.99984 4.99542 3.19041 4.50943 3.5335 4.13945C3.87659 3.76947 4.34684 3.54284 4.85 3.505L5 3.5H13ZM19.243 3.843C19.423 3.66365 19.6644 3.55953 19.9184 3.55177C20.1723 3.54402 20.4197 3.63322 20.6103 3.80125C20.8008 3.96928 20.9203 4.20355 20.9444 4.45647C20.9685 4.7094 20.8954 4.96201 20.74 5.163L20.657 5.258L10.757 15.157C10.577 15.3363 10.3356 15.4405 10.0816 15.4482C9.82767 15.456 9.58029 15.3668 9.38972 15.1988C9.19916 15.0307 9.07969 14.7964 9.0556 14.5435C9.03151 14.2906 9.10459 14.038 9.26 13.837L9.343 13.743L19.243 3.843Z"
            fill="#2B9B3C" class="header-btn-svg" />
        </svg>
        <p class="text-xl">Edit</p>
      </NuxtLink>
    </template>
    <div class="w-full h-full flex xl:flex-row flex-col gap-2">
      <div class="h-full w-full xl:max-w-[31.25rem] max-w-[64rem] flex flex-col gap-2">
        <FarmAISummaryCard />
        <FarmPendingActivitiesCard />
      </div>
      <div class="w-full h-full flex flex-col gap-2">
        <FarmWeatherCard :latitude="farm.location.coordinates[1]" :longitude="farm.location.coordinates[0]"/>
        <FarmActivityLogsCard />
      </div>
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth',
})

const route = useRoute()
const client = useSupabaseClient()

const farmId = route.params.id
const farm = await getFarm()

async function getFarm() {
  try {
  let { data: farm, error } = await client
    .from('farms')
    .select('*')
    .eq('id', farmId)
    .single()
  if (error) {
    throw error
  }
  return farm
} catch (error) {
  console.log(error)
}
}
</script>

<style></style>