<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Calendar</h1>
    </template>
    <div v-for="group in sortedGroupedEvents" :key="group.month" class="flex flex-col gap-3">
      <p class="text-2xl font-bold">{{ group.month }}</p>
      <div v-for="event in group.events" :key="event.id">
        <CalendarItem :event="event" />
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth'
})

const client = useSupabaseClient()
const events = await getEvents()

for (const event of events) {
  event.farm_name = await getFarmName(event.farm_id)
}

const groupedEvents = events?.reduce((acc, event) => {
  const month = new Date(event.end_date).toLocaleString('default', { month: 'long' });
  if (!acc[month]) {
    acc[month] = [];
  }
  acc[month].push(event);
  return acc;
}, {});

const sortedGroupedEvents = Object.keys(groupedEvents).sort((a, b) => {
  const dateA = new Date(a);
  const dateB = new Date(b);
  return dateA - dateB;
}).map(key => ({ month: key, events: groupedEvents[key] }));

async function getEvents() {
  try {
    let { data: events, error } = await client
      .from('events')
      .select('*')
      .order('end_date', { ascending: true })
      .eq('is_completed', false)
    if (error) {
      throw error
    }
    return events
  } catch (error) {
    console.log(error)
  }
}

async function getFarmName(farmId) {
  try {
    let { data: farm, error } = await client
      .from('farms')
      .select('name')
      .eq('id', farmId)
      .single()
    if (error) {
      throw error
    }
    return farm.name
  } catch (error) {
    console.log(error)
}
}
</script>

<style scoped>

</style>