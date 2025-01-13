<!-- eslint-disable vue/first-attribute-linebreak -->
<template>
  <NuxtLayout name="auth">
    <div class="w-full h-full flex flex-col gap-3 justify-between items-center text-white">
      <LogoItem />
      <form class="flex flex-col gap-3 mx-auto items-center max-w-[37.5rem] w-full" @submit.prevent="updateUser">
        <p class="text-3xl">Change Password</p>
        <input id="password" v-model="password" type="password" name="password" placeholder="Password"
          class="textfield">
        <input id="confirm-password" v-model="confirm_password" type="password" name="confirm-password" placeholder="Confirm Password"
          class="textfield">
        <p v-if="errorMsg" class="text-red-500">{{ errorMsg }}</p>
        <button class="button" type="submit">Update</button>
      </form>
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
const password = ref(null)
const confirm_password = ref(null)
const errorMsg = ref('')

async function updateUser() {
  errorMsg.value = ''
  if (password.value === null) {
    errorMsg.value = 'Password is required.'
    return
  }
  if (password.value !== confirm_password.value) {
    errorMsg.value = 'Passwords do not match.'
    return
  }
  try {
    const { error } = await client.auth.updateUser({
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