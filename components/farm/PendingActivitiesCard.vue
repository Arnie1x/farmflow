<template>
  <div class="w-full min-w-[18.75rem] rounded-2xl border-2 p-5 flex flex-col justify-between gap-5">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/alert.svg" alt="ai" class="w-[2.125rem]" />
      <h1 class="text-3xl font-bold text-[#D36135]">Pending Activities</h1>
    </div>
    <div class="w-full h-full flex flex-col gap-5">
      <p class="text-2xl font-bold">Month</p>
      <FarmPendingActivityItem />
      <FarmPendingActivityItem />
      <FarmPendingActivityItem />
      <FarmPendingActivityItem />
    </div>
  </div>
</template>

<script lang="ts" setup>

</script>

<style>

</style>