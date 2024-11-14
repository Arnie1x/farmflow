<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Chat</h1>
    </template>
    <div class="flex flex-row gap-5 w-full h-full">
      <div class="w-full h-full flex flex-col gap-3 align-bottom justify-end">
        <div class="w-full h-full flex flex-col-reverse gap-3 overflow-y-scroll">
          <!-- Look into different ways of making this scroll behavior if the flex-col-reverse doesn't work -->
          <ChatBubble />
          <ChatBubble :is-user="false"/>
          <ChatBubble />
          <ChatBubble :is-user="false"/>
          <ChatBubble />
          <ChatBubble :is-user="false"/>
          <ChatBubble />
          <ChatBubble :is-user="false"/>
        </div>
        <form class="flex flex-row gap-3 h-min" @submit.prevent>
          <textarea v-model="prompt" class="w-full textfield" placeholder="Start Typing" rows="1"/>
          <button type="submit" class="button max-w-[3.5rem] max-h-[3.5rem]">
            <NuxtImg src="/images/icons/send.svg" alt="send" class="w-full p-3" />
          </button>
        </form>
      </div>
      <div>
        <ChatSidebar />
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth'
})

const prompt = ref('')
</script>

<style scoped>
textarea {
  resize: none;
}
</style>