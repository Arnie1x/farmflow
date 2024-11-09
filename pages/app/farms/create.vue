<!-- eslint-disable vue/first-attribute-linebreak -->
<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">New Farm</h1>
    </template>
    <form class="w-full h-full flex xl:flex-row flex-col gap-3" @submit.prevent="createFarm">
      <div class="flex flex-col gap-3 max-w-[64rem] w-full">
        <input id="farm_name" v-model="farmName" type="text" class="text-black textfield" name="farm_name"
          placeholder="Farm Name *">
        <input id="location" v-model="location" type="text" class="text-black textfield" name="location"
          placeholder="Location *" @input="getLocationList">
        <input id="area_size" v-model="areaSize" type="number" class="text-black textfield" name="area_size"
          placeholder="Area Size (in Ha)">
      </div>
      <p v-if="errorMsg" class="text-red-500 w-full text-center">{{ errorMsg }}</p>
      <button class="text-white button h-min xl:max-w-[25rem]">Create Farm</button>
    </form>
  </NuxtLayout>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth',
})

const client = useSupabaseClient()
const user = useSupabaseUser()

const farmName = ref('')
const location = ref('')
const areaSize = ref(null)
const errorMsg = ref('')

const mapboxSearchResults = ref([])
const runtimeConfig = useRuntimeConfig()
const mapboxAccessToken = runtimeConfig.public.mapboxAccessToken

async function getLocationList() {
  if (location.value.length <= 3) {
    return
  }
  try {
    const results = await fetch(`https://api.mapbox.com/search/geocode/v6/forward?q=${location.value}&access_token=${mapboxAccessToken}&country=KE`)
    const data = await results.json()
    mapboxSearchResults.value = data['features']
    console.log(mapboxSearchResults.value)
  } catch (error) {
    errorMsg.value = error.message
  }
}

async function createFarm() {
  try {
    const { error } = await client
      .from('farms')
      .insert(
        { user_id: user.value.id, name: farmName.value, area_size: areaSize.value, location: location.value }
      )
    if (error) {
      throw error
    }
    navigateTo('/app/farms')
  } catch (error) {
    errorMsg.value = error.message
  }
}

</script>

<style></style>