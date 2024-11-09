<template>
  <div class="w-full flex flex-col rounded-2xl border-2 p-5 gap-3">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/logs.svg" alt="weather" class="w-[1.75rem] mx-2" />
      <p class="text-3xl font-bold text-[#104547]">Activity Logs</p>
    </div>
    <div class="flex flex-col gap-3">
      <!-- <p class="text-2xl font-bold text-[#104547]">No Activity Logs</p> -->
       <FarmActivityLogItem />
       <FarmActivityLogItem />
       <FarmActivityLogItem />
    </div>
  </div>
</template>

<script lang="ts" setup>

</script>

<style>

</style>