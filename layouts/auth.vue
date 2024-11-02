<template>
  <div
    class="w-screen h-screen flex flex-row justify-center items-center bg-gradient-to-br from-[#24252D] to-[#06240A] p-2">

    <div class="h-full w-full">
      <slot />
    </div>

    <div class="h-full w-full bg-white rounded-2xl">
      <slot name="image" />
    </div>

  </div>
</template>
<style scoped></style>