<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Farms</h1>
      <NuxtLink to="/app/farms/create" class="button-outlined flex flex-row gap-3 justify-center items-center">
        <svg width="25" height="25" viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M10.5 20.5C10.5 20.8978 10.658 21.2794 10.9393 21.5607C11.2206 21.842 11.6022 22 12 22C12.3978 22 12.7794 21.842 13.0607 21.5607C13.342 21.2794 13.5 20.8978 13.5 20.5V14H20C20.3978 14 20.7794 13.842 21.0607 13.5607C21.342 13.2794 21.5 12.8978 21.5 12.5C21.5 12.1022 21.342 11.7206 21.0607 11.4393C20.7794 11.158 20.3978 11 20 11H13.5V4.5C13.5 4.10218 13.342 3.72064 13.0607 3.43934C12.7794 3.15804 12.3978 3 12 3C11.6022 3 11.2206 3.15804 10.9393 3.43934C10.658 3.72064 10.5 4.10218 10.5 4.5V11H4C3.60218 11 3.22064 11.158 2.93934 11.4393C2.65804 11.7206 2.5 12.1022 2.5 12.5C2.5 12.8978 2.65804 13.2794 2.93934 13.5607C3.22064 13.842 3.60218 14 4 14H10.5V20.5Z"
            fill="#000000" class="header-btn-svg" />
        </svg>
        <p class="text-xl">Create</p>
      </NuxtLink>
    </template>
    <div v-for="farm in farms" :key="farm['id']"
      class="w-full h-content grid xl:grid-cols-3 lg:grid-cols-2 grid-cols-1 gap-2">
      <FarmCard :farm="farm" />
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth',
})

const client = useSupabaseClient()
const farms = ref([])

await getFarms()

async function getFarms() {
  try {
    const { data, error } = await client.from('farms').select('*')
    if (error) {
      throw error
    }
    console.log(data)
    farms.value = data
  } catch (error) {
    console.error(error)
  }
}

</script>

<style scoped></style>