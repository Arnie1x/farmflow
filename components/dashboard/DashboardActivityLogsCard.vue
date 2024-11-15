<template>
  <div class="w-full flex flex-col rounded-2xl border-2 p-5 gap-3">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/logs.svg" alt="weather" class="w-[1.75rem] mx-2" />
      <p class="text-3xl font-bold text-[#104547]">Recent Events</p>
    </div>
    <div v-for="event in events" :key="event.id" class="flex flex-col gap-3">
      <!-- <p class="text-2xl font-bold text-[#104547]">No Activity Logs</p> -->
      <FarmActivityLogItem :event="event" :show-farm-name="true"/>
    </div>
    <!-- <NuxtLink to="/app/calendar" class="link h-min w-full font-bold">View More</NuxtLink> -->
  </div>
</template>


<script lang="ts" setup>

const client = useSupabaseClient()

const events = await getEvents()

for (const event of events) {
  event.farm_name = await getFarmName(event.farm_id)
}

async function getEvents() {
  try {
    let { data: events, error } = await client
      .from('events')
      .select('*')
      .order('created_at', { ascending: false })
      .limit(8)
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
.link {
  color: #104547;
  transition: 0.5s all ease;
}

.link:hover {
  text-decoration: underline;
  color: #2ac241;
}
</style>