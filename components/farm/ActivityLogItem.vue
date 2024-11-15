<template>
  <div class="w-full flex 2xl:flex-row flex-col justify-start items-start">
    <div class="2xl:max-w-[16rem] w-full">
      <div class="flex flex-row justify-between w-full">
        <p class="text-xl text-ellipsis font-semibold">{{ event.name }}</p>
        <NuxtLink :to="{ name: 'app-farms-id-events-event_id', params: { id: farmId, event_id: event.id } }"
          class="link 2xl:hidden flex flex-row gap-3 justify-center items-center">
          <p class="text-xl">Edit</p>
          <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M17.5 5.25L10 12.75L2.5 5.25L1 6.75L10 15.75L19 6.75L17.5 5.25Z" fill="#104547" class="link-svg" />
          </svg>
        </NuxtLink>
      </div>
      <p v-if="event.farm_name" class="font-semibold text-sm">{{ event.farm_name }}</p>
      <div class="flex flex-row gap-2">
        <p class="text-[#848AA0] font-semibold text-sm w-10">From:</p>
        <p class="text-[#848AA0] font-semibold text-sm">{{ dateFormatter(event.start_date) }}</p>
      </div>
      <div class="flex flex-row gap-2">
        <p class="text-[#848AA0] font-semibold text-sm w-10">To:</p>
        <p class="text-[#848AA0] font-semibold text-sm">{{ dateFormatter(event.end_date) }}</p>
      </div>
    </div>
    <p class="text-ellipsis w-full">{{ event.description }}</p>
    <div>
      <NuxtLink :to="{ name: 'app-farms-id-events-event_id', params: { id: farmId, event_id: event.id } }"
        class="link hidden 2xl:flex 2xl:flex-row gap-3 justify-center items-center">
        <p class="text-xl">Edit</p>
        <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.5 5.25L10 12.75L2.5 5.25L1 6.75L10 15.75L19 6.75L17.5 5.25Z" fill="#104547" class="link-svg" />
        </svg>
      </NuxtLink>
    </div>
  </div>
</template>

<script lang="ts" setup>
// eslint-disable-next-line no-unused-vars
const props = defineProps({
  event: {
    type: Object,
    required: true
  },
  isEventPage: {
    type: Boolean,
    required: false,
    default: false
  },
  showFarmName: {
    type: Boolean,
    required: false,
    default: false
  }
})

const farmId = props.event.farm_id

function dateFormatter(date) {
  const currentDate = new Date()
  const newDate = new Date(date)
  const month = newDate.toLocaleString('default', { month: 'short' })
  const day = newDate.getDate()
  const time = newDate.toLocaleString('default', { hour: 'numeric', minute: 'numeric' })
  const year = newDate.getFullYear()

  if (currentDate.getFullYear() !== newDate.getFullYear()) {
    return `${time} ${month} ${day} ${year}`
  }
  else {
    return `${time} ${month} ${day}`
  }
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
  color: #2ac241;
  fill: #2ac241;
}

.link:hover .link-svg {
  fill: #2ac241;
}
</style>