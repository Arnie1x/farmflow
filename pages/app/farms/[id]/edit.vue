<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold capitalize">{{ farm['name'] }}: Edit</h1>
    </template>
    <FarmForm :farm="farm" :is-update="true" />
  </NuxtLayout>
</template>

<script setup lang="ts">
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

<style scoped></style>