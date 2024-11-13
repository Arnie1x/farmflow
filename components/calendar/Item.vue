<template>
  <div class="w-full flex xl:flex-row flex-col justify-between items-center p-3 rounded-2xl border-2">
    <div class="flex flex-row justify-start gap-5 items-center xl:py-0 py-3 w-fit">
      <div class="flex flex-col justify-center items-center px-3 pl-8 w-fit">
        <p class="font-bold">{{ getWeekDay(event.end_date) }}</p>
        <p class="text-3xl font-bold text-[#2B9B3C]">{{ getDayDate(event.end_date) }}</p>
      </div>
      <div class="border h-[2.5rem] mx-4" />
      <div class="flex flex-col min-w-[10rem] justify-start">
        <div class="flex flex-row gap-2 justify-start">
          <NuxtImg src="/images/icons/location.svg" alt="location" class="w-[1.25rem]" />
          <p class="text-base text-ellipsis line-clamp-1">{{ event.farm_name }}</p>
        </div>
        <div class="flex flex-row gap-2 justify-start">
          <NuxtImg src="/images/icons/time.svg" alt="location" class="w-[1.25rem]" />
          <p class="text-base">{{ getTimeDate(event.end_date) }}</p>
        </div>
      </div>
    </div>
    <div class="border h-[2.5rem] mx-4 xl:block hidden" />
    <div class="w-full">
      <p class="text-ellipsis line-clamp-2 w-full">
        <b>{{ event.name }}: </b> <br>
        {{ event.description }}
      </p>
    </div>
    <div>
      <!-- <NuxtLink class="link flex flex-row gap-3 justify-center items-center p-4 min-w-[8rem]"> -->
      <NuxtLink :to="{ name: 'app-farms-id-events-event_id', params: { id: event.farm_id, event_id: event.id } }"
        class="link flex flex-row gap-3 justify-center items-center p-4 min-w-[8rem]">
        <p class="text-xl">Edit</p>
        <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.5 5.25L10 12.75L2.5 5.25L1 6.75L10 15.75L19 6.75L17.5 5.25Z" fill="#104547" class="link-svg" />
        </svg>
      </NuxtLink>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  event: {
    type: Object,
    required: true
  }
})
function getDayDate(date) {
  const day = new Date(date).toLocaleString('default', { day: 'numeric' });
  return day
}
function getWeekDay(date) {
  const day = new Date(date).toLocaleString('default', { weekday: 'short' });
  return day
}

function getTimeDate(date) {
  const time = new Date(date).toLocaleString('default', { hour: 'numeric', minute: 'numeric' });
  return time
}

</script>

<style scoped>
.link-svg {
  fill: #104547;
  transition: 0.5s all ease;
}

.link {
  color: #104547;
  transition: 0.5s all ease;
}

.link:hover {
  cursor: pointer;
  color: #2ac241;
  fill: #2ac241;
}

.link:hover .link-svg {
  fill: #2ac241;
}
</style>