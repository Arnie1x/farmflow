<!-- eslint-disable vue/html-self-closing -->
<template>
  <NuxtLink :to="{ name: 'app-farms-id', params: { id: farm['id'] }}">
    <div class="h-[18.75rem] max-w-[31.25rem] min-w-[18.75rem] rounded-2xl border-2 flex flex-col justify-between gap-2">
      <div class="w-full h-full p-3">
        
      </div>
      <div class="border" />
      <div class="w-full h-full p-3 flex flex-col">
        <p class="text-2xl font-bold">{{ farm['name'] }}</p>
        <div class="flex flex-row gap-2 justify-start">
          <NuxtImg src="/images/icons/location.svg" alt="location" class="w-[1.25rem]" />
          <p class="text-base font-bold text-[#848AA0]">{{ farm['location']['full_address'].split(',').reverse()[1] }}</p>
        </div>
        <div class="flex flex-row gap-2 justify-start items-center h-full">
          <NuxtImg src="/images/icons/alert.svg" alt="location" class="w-[1.25rem]" />
          <p class="text-base font-bold text-[#D36135]">2 Activities Pending</p>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script lang="ts" setup>

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  farm: {
    type: Object,
    required: true
  }
})
</script>

<style>

</style>