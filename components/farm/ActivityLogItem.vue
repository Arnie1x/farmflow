<template>
  <div class="w-full flex 2xl:flex-row flex-col justify-start items-start">
    <div class="max-w-[16rem] w-full">
      <p class="text-xl text-ellipsis font-semibold">{{ event.name }}</p>
      <div class="flex flex-row gap-2">
        <p class="text-[#848AA0] font-semibold text-sm w-10">From:</p>
        <p class="text-[#848AA0] font-semibold text-sm">{{ dateFormatter(event.start_date) }}</p>
      </div>
      <div class="flex flex-row gap-2">
        <p class="text-[#848AA0] font-semibold text-sm w-10">To:</p>
        <p class="text-[#848AA0] font-semibold text-sm">{{ dateFormatter(event.end_date) }}</p>
      </div>
    </div>
    <p class="text-ellipsis">{{ event.description }}</p>
  </div>
</template>

<script lang="ts" setup>
// eslint-disable-next-line no-unused-vars
const props = defineProps({
  event: {
    type: Object,
    required: true
  }
})

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

<style>

</style>