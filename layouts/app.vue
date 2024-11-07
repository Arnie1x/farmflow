<template>
  <div
    class="w-screen h-screen flex flex-row justify-between items-center bg-gradient-to-br from-[#1C1C1F] to-[#06240A] via-[#1D2122] via-30% p-2 gap-2">

    <div class="w-full h-full max-w-[18.75rem]">
      <SideBar />
    </div>

    <div class="h-full w-full flex flex-col rounded-2xl bg-white">
      <div class="w-full h-[4rem] flex flex-row justify-between items-center border-gray-300 border-b-2 p-5">
        <slot name="header" />
      </div>
      <div class="p-5">
        <slot />
      </div>
    </div>

  </div>
</template>
<script lang="ts" setup>

</script>
<style scoped></style>