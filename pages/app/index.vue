<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Dashboard</h1>
    </template>
    <div class="w-full h-full flex flex-col gap-5">
      <NuxtLink to="/app/calendar" class="cursor-pointer">
        <div class="flex flex-row gap-2 justify-start items-center hover:underline transition-all">
          <NuxtImg src="/images/icons/alert.svg" alt="ai" class="w-[2rem]" />
          <h1 v-if="pendingEventsCount > 0" class="text-2xl">You have <span class="text-[#D36135] font-bold">{{ pendingEventsCount }}</span> Pending Activities. View all activities in Calendar</h1>
        </div>
      </NuxtLink>
      <DashboardActivityLogsCard />
    </div>
  </NuxtLayout>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth'
})

const client = useSupabaseClient()
const pendingEvents = ref([])
const pendingEventsCount = ref(0)

pendingEvents.value = await getPendingEvents()
pendingEventsCount.value = pendingEvents.value.length

async function getPendingEvents() {
  try {
    const today = new Date();
    const threeDaysFromNow = new Date(today.getTime() + 3 * 24 * 60 * 60 * 1000).toISOString();

    let { data: events, error } = await client
      .from('events')
      .select('*')
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

<style scoped></style>