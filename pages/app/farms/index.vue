<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Farms</h1>
    </template>
    <div v-for="farm in farms" :key="farm['id']"
      class="w-full h-content grid xl:grid-cols-3 lg:grid-cols-2 grid-cols-1 gap-2">
      <FarmCard :id="farm['id']" :farm="farm" />
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