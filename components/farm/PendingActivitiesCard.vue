<template>
  <div v-if="sortedGroupedEvents.length > 0" class="w-full min-w-[18.75rem] rounded-2xl border-2 p-5 flex flex-col justify-between gap-5">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/alert.svg" alt="ai" class="w-[2.125rem]" />
      <h1 class="text-3xl font-bold text-[#D36135]">Pending Activities</h1>
    </div>
    <div v-for="group in sortedGroupedEvents" :key="group.month" class="w-full h-full flex flex-col gap-5">
      <p class="text-2xl font-bold">{{ group.month }}</p>
      <div v-for="event in group.events" :key="event.id">
        <FarmPendingActivityItem :event="event" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const route = useRoute()
const client = useSupabaseClient()

const farmId = route.params.id
const events = await getEvents()
events?.reverse()

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

// console.log(sortedGroupedEvents);

async function getEvents() {
  try {
    const today = new Date();
    const threeDaysFromNow = new Date(today.getTime() + 3 * 24 * 60 * 60 * 1000).toISOString();

    let { data: events, error } = await client
      .from('events')
      .select('*')
      .eq('farm_id', farmId)
      .eq('is_completed', false)
      .lte('end_date', threeDaysFromNow)
      .order('end_date', { ascending: false })
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

<style>

</style>