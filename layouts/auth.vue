<template>
  <div
    class="w-screen h-screen flex flex-row justify-center items-center bg-gradient-to-br from-[#1C1C1F] to-[#06240A] via-[#1D2122] via-30% p-2">

    <div class="h-full w-full p-2">
      <slot />
    </div>

    <div class="h-full w-full rounded-2xl">
      <slot name="image" />
    </div>

  </div>
</template>
<style scoped>


</style>