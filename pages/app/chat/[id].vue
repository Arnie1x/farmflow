<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold text-ellipsis line-clamp-1">Chat: {{ title }}</h1>
    </template>
    <ChatComponent />
  </NuxtLayout>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: 'auth'
})

const title = ref('')
const client = useSupabaseClient()
const route = useRoute()
const id = route.params.id

try {
  const { data, error: dataError } = await client.from("chats").select("*").eq("id", id).single();
  if (dataError) throw dataError
  title.value = data.title
} catch (error) {
  console.log(error)
}

</script>

<style>

</style>