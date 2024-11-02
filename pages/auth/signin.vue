<template>
  <NuxtLayout name="auth">
    <div class="w-full h-full flex flex-col gap-3 justify-center items-center text-white">
      <Logo />
      <p class="text-3xl">Sign In</p>
      <form class="inline-flex flex-col gap-3">
        <input type="text" name="email" id="email" placeholder="Email">
        <input type="password" name="password" id="password" placeholder="Password">
        <p>Forgot your Password?</p>
        <button type="submit">Sign In</button>
      </form>
      <p>Don't have an account? Sign Up</p>
    </div>
    <template #image>
      <div class="w-full h-full">
        <NuxtImg src="/images/sign-in.png" fit="fill" />
      </div>
    </template>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  layout: false
})

</script>

<style scoped></style>