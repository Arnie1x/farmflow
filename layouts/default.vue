<template>
  <div
    class="w-screen h-screen flex flex-row justify-between items-center bg-gradient-to-br from-[#1C1C1F] to-[#06240A] via-[#1D2122] via-30% p-2 gap-2">

    <div class="w-full h-full max-w-[18.75rem]">
      <SideBar />
    </div>

    <div class="h-full w-full rounded-2xl bg-white">
      <slot />
    </div>

  </div>
</template>
<script lang="ts" setup>

</script>
<style scoped></style>