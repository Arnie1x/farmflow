<template>
  <NuxtLayout name="auth">
    <div class="w-full h-full flex flex-col gap-3 justify-between items-center text-white">
      <Logo />
      <form class="flex flex-col gap-3 mx-auto items-center max-w-[37.5rem] w-full" @submit.prevent="signup">
        <p class="text-3xl">Sign Up</p>
        <div class="flex flex-row gap-3 w-full">
          <input id="fname" v-model="first_name" type="text" name="fname" placeholder="First Name" class="textfield">
          <input id="lname" v-model="last_name" type="text" name="lname" placeholder="Last Name" class="textfield">
        </div>
        <input id="email" v-model="email" type="text" name="email" placeholder="Email" class="textfield">
        <input id="password" v-model="password" type="password" name="password" placeholder="Password" class="textfield">
        <input id="confirm-password" v-model="confirm_password" type="password" name="confirm-password" placeholder="Confirm Password" class="textfield">
        <p v-if="errorMsg" class="text-red-500">{{ errorMsg }}</p>
        <p v-if="successMsg" class="text-green-500">{{ successMsg }}</p>
        <button type="submit">Sign Up</button>
      </form>
      <p>Already have an account? <NuxtLink class="link" to="/login">Sign In</NuxtLink></p>
    </div>
    <template #image>
      <div class="auth-bg w-full h-full rounded-2xl"/>
    </template>
  </NuxtLayout>
</template>

<script setup lang="ts">

const client = useSupabaseClient()
const first_name = ref('')
const last_name = ref('')
const email = ref('')
const password = ref(null)
const confirm_password = ref(null)
const errorMsg = ref('')
const successMsg = ref('')

async function signup() {
  errorMsg.value = ''
  successMsg.value = ''
  if (password.value !== confirm_password.value) {
    errorMsg.value = 'Passwords do not match'
    return
  }
  try {
    const { data, error } = await client.auth.signUp({
    email: email.value,
    password: password.value,
  //   options: {
  //     data: {
  //       first_name: first_name,
  //       last_name: last_name,
  //   },
  // },
  })
  if (error) {
    throw error
  }
  successMsg.value = 'Account Creation Successful. Check your Email for the Verification Link'
  } catch (error) {
    errorMsg.value = error.message
  }
}

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