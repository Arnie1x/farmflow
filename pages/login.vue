<template>
  <NuxtLayout name="auth">
    <div class="w-full h-full flex flex-col gap-3 justify-between items-center text-white">
      <LogoItem />
      <form class="flex flex-col gap-3 mx-auto items-center max-w-[37.5rem] w-full" @submit.prevent="signin">
        <p class="text-3xl">Sign In</p>
        <input id="email" v-model="email" type="text" name="email" placeholder="Email" class="textfield">
        <input id="password" v-model="password" type="password" name="password" placeholder="Password"
          class="textfield">
        <NuxtLink to="/auth/forgot-password" class="text-sm w-full text-right link-white">Forgot your Password?
        </NuxtLink>
        <p v-if="errorMsg" class="text-red-500">{{ errorMsg }}</p>
        <button class="button" type="submit">Sign In</button>
      </form>
      <p>Don't have an account? <NuxtLink class="link" to="/register">Sign Up</NuxtLink>
      </p>
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
const password = ref(null)
const errorMsg = ref('')

async function signin() {
  errorMsg.value = ''
  if (password.value === null) {
    errorMsg.value = 'Password is required.'
    return
  }
  try {
    const { error } = await client.auth.signInWithPassword({
      email: email.value,
      password: password.value,
    })
    if (error) {
      throw error
    }
    navigateTo("/app")
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