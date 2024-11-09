<!-- eslint-disable vue/first-attribute-linebreak -->
<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">New Farm</h1>
    </template>
    <form class="w-full h-full flex xl:flex-row flex-col gap-3" @submit.prevent="createFarm">
      <div class="flex flex-col gap-3 max-w-[64rem] w-full relative">
        <input id="farm_name" v-model="farmName" type="text" class="text-black textfield" name="farm_name"
          placeholder="Farm Name *">
        <input id="location" v-model="location" type="text" class="text-black textfield" name="location"
          placeholder="Location *" @input="getLocationList">
        <ul v-show="mapboxSearchResults" v-if="showSearchResults" class="w-full rounded-2xl px-4 bg-[#dadce2] absolute top-[7rem]">
          <p v-if="searchError">Sorry, something went wrong. Please try again.</p>
          <p v-if="!searchError && mapboxSearchResults.length === 0 && location !== ''">
            No results match your query, try a different location.
          </p>
          <template v-else>
            <li v-for="searchResult in mapboxSearchResults" v-if="location !== ''" :key="searchResult['id']"
              class="cursor-pointer py-2 hover:font-medium duration-200" @click="setLocation(searchResult['id'])">
              {{ searchResult['properties']['full_address'] }}
            </li>
          </template>
        </ul>
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
const locationJSON = ref({})
const areaSize = ref(null)
const errorMsg = ref('')
const searchError = ref('')

const showSearchResults = ref(true)
const mapboxSearchResults = ref([])
const runtimeConfig = useRuntimeConfig()
const mapboxAccessToken = runtimeConfig.public.mapboxAccessToken

async function getLocationList() {
  if (location.value.length <= 3) {
    return
  }
  showSearchResults.value = true
  try {
    const results = await fetch(`https://api.mapbox.com/search/geocode/v6/forward?q=${location.value}&access_token=${mapboxAccessToken}&country=KE`)
    const data = await results.json()
    mapboxSearchResults.value = data['features']
    console.log(mapboxSearchResults.value)
  } catch (error) {
    searchError.value = error.message
  }
}

async function setLocation(id) {
  try {
    for (let i = 0; i < mapboxSearchResults.value.length; i++) {
      if (mapboxSearchResults.value[i]['id'] === id) {
        const data = mapboxSearchResults.value[i]
        location.value = data['properties']['full_address']
        locationJSON.value = {
          'name': data['properties']['name'],
          'full_address': data['properties']['full_address'],
          'coordinates': [data['geometry']['coordinates'][0], data['geometry']['coordinates'][1]]
        }
        console.log(locationJSON.value)
        showSearchResults.value = false
        break
      }
    }
  } catch (error) {
    searchError.value = error.message
  }
}

async function createFarm() {
  // TODO:: Need to add validation
  try {
    const { error } = await client
      .from('farms')
      .insert(
        { user_id: user.value.id, name: farmName.value, area_size: areaSize.value, location: locationJSON.value }
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