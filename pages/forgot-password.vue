<template>
  <NuxtLayout name="auth">
    <div class="w-full h-full flex flex-col gap-3 justify-between items-center text-white">
      <LogoItem />
      <form class="flex flex-col gap-3 mx-auto items-center max-w-[37.5rem] w-full" @submit.prevent="forgotPassword">
        <p class="text-3xl">Forgot Password?</p>
        <input id="email" v-model="email" type="text" name="email" placeholder="Email" class="textfield">
        <p v-if="errorMsg" class="text-red-500">{{ errorMsg }}</p>
        <p v-if="successMsg" class="text-green-500">{{ successMsg }}</p>
        <button class="button" type="submit">Recover Account</button>
      </form>
      <div />
    </div>
    <template #image>
      <div class="auth-bg w-full h-full rounded-2xl" />
    </template>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "empty"
})
// const router = useRouter()
const client = useSupabaseClient()
const email = ref('')
const errorMsg = ref('')
const successMsg = ref('')

async function forgotPassword() {
  errorMsg.value = ''
  if (email.value === null) {
    errorMsg.value = 'Email is required.'
    return
  }
  try {
    const { error } = await client.auth.resetPasswordForEmail(email.value, { redirectTo: '/reset-password' })
    if (error) {
      throw error
    }
    else {
      successMsg.value = 'Password reset link sent to ' + email.value
    }
  } catch (error) {
    errorMsg.value = error.message
  }
}

</script>

<style scoped>
.auth-bg {
  background-image: url("/images/sign-in.png");
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