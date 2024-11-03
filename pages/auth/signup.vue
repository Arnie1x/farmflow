<template>
  <NuxtLayout name="auth">
    <div class="w-full h-full flex flex-col gap-3 justify-between items-center text-white">
      <Logo />
      <form class="flex flex-col gap-3 mx-auto items-center max-w-[37.5rem] w-full">
        <p class="text-3xl">Sign Up</p>
        <div class="flex flex-row gap-3 w-full">
          <input type="text" name="fname" id="fname" placeholder="First Name" class="textfield">
          <input type="text" name="lname" id="lname" placeholder="Last Name" class="textfield">
        </div>
        <input type="text" name="email" id="email" placeholder="Email" class="textfield">
        <input type="password" name="password" id="password" placeholder="Password" class="textfield">
        <input type="password" name="confirm-password" id="confirm-password" placeholder="Confirm Password" class="textfield">
        <button type="submit">Sign Up</button>
      </form>
      <p>Already have an account? <NuxtLink class="link" to="/auth/signin">Sign In</NuxtLink></p>
    </div>
    <template #image>
      <div class="auth-bg w-full h-full rounded-2xl">
      </div>
    </template>
  </NuxtLayout>
</template>

<script setup lang="ts">

</script>

<style scoped>

.auth-bg {
  background-image: url("/images/sign-up.png");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.link-white {
  color: #F8F8F8;
  transition: 0.5s all ease;
}

.link-white:hover {
  text-decoration: underline;
  color: #2ac241;
}

</style>