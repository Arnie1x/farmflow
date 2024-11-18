<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">FAQ</h1>
    </template>
    <div class="h-full w-full max-w-[64rem] mx-auto flex flex-col gap-3">
      <FaqItem v-for="item in data" :question="item.question" :answer="item.answer" />
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth'
})

const data = ref([])

data.value.push({
  question: 'How do I start interacting with the chatbot?',
  answer: `
  To interact with the chatbot:

- Navigate to the "Chat" section from the main menu.
- Type your question or request in the input box at the bottom of the chat page.
- The chatbot will provide a response tailored to your query.
- You can also reference specific farms using the @ symbol to include farm-specific context.

The chatbot is designed to provide clear, concise answers and guide you step-by-step for your rice farming needs.

`
})
data.value.push({
  question: 'How can I link my farm details to the chatbot?',
  answer: `
  You can link your farm details to the chatbot by referencing your farm's name in your message. Here’s how:

- While chatting, type the @ symbol followed by your farm's name.
- The chatbot will use the associated farm data (e.g., soil type, location) to give tailored advice.
- Make sure your farm profile is up-to-date under the "Farm Profile" section in the app!

`
})
data.value.push({
  question: 'How can I access and update my farm profile?',
  answer: `
To manage your farm profile:

- Go to the "Farms" page from the navigation menu.
- Add new farms by clicking "Add Farm" and entering the required details, such as farm size, soil type, and location.
- To update an existing farm, select the farm from the list, make your changes, and save them.
- Your farm profile helps the app and chatbot provide personalized recommendations.

`
})
</script>

<style scoped>

</style>