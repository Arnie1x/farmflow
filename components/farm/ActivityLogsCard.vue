<template>
  <div class="w-full flex flex-col rounded-2xl border-2 p-5 gap-3">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/logs.svg" alt="weather" class="w-[1.75rem] mx-2" />
      <p class="text-3xl font-bold text-[#104547]">Event Logs</p>
    </div>
    <div v-if="events.length > 0" v-for="event in events" :key="event.id" class="flex flex-col gap-3">
      <FarmActivityLogItem :event="event" />
    </div>
    <p v-else-if="isFarmPage" class="text-lg">No Activity Logs, click on <b>View More</b> to create an event log</p>
    <NuxtLink v-if="!isEventPage" :to="{ name: 'app-farms-id-events', params: { id: farmId } }"
      class="link h-min w-full font-bold">View More</NuxtLink>
  </div>
</template>

<script lang="ts" setup>

const route = useRoute()
const client = useSupabaseClient()
const isEventPage = ref(false)
const isFarmPage = ref(false)

const farmId = route.params.id
const events = await getEvents()

if (route.path.includes('farms')) {
  isFarmPage.value = true
}
if (route.path.includes('events')) {
  isEventPage.value = true
}

async function getEvents() {
  try {
    let { data: events, error } = await client
      .from('events')
      .select('*')
      .eq('farm_id', farmId).order('created_at', { ascending: false })
      .limit(5)
    if (error) {
      throw error
    }
    return events
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