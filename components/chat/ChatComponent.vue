<template>
  <div class="flex flex-row gap-5 w-full h-full">
      <div class="w-full h-full flex flex-col gap-3 align-bottom justify-end">
        <div v-if="messages.length > 0" v-auto-animate class="w-full h-full flex flex-col-reverse gap-3 overflow-y-scroll overflow-x-hidden">
          <!-- Look into different ways of making this scroll behavior if the flex-col-reverse doesn't work -->
          <div v-for="message in messages.toReversed()" :key="message.id">
            <ChatBubble :message="message.message" :is-user="message.is_user" />
          </div>
        </div>
        <p v-if="loading" class="text-sm font-bold px-5 animate-pulse">Loading...</p>
        <form class="flex flex-row gap-3 h-min" @submit.prevent="sendMessage">
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
</template>

<script lang="ts" setup>
import ChatService from '~/types/chat_service';

const messages = ref([])
const prompt = ref('')
const loading = ref(false)

const chatId = ref('')
const route = useRoute()
const query = route.query

const chatService = new ChatService()
if (route.params.id) {
  chatId.value = route.params.id
  chatService.setChatId(chatId.value)
}

if (chatService.hasChatID()) {
  await chatService.getAllMessages()
}
messages.value = chatService.messages

if (query.prompt) {
  loading.value = true
  await chatService.sendMessage(query.prompt)
  // latestMessages.push(await chatService.sendMessage(query.prompt))
  // messages.value.push(...latestMessages)
  loading.value = false
}

async function sendMessage() {
  if (!prompt.value) return

  if (!route.params.id) {
    chatId.value = await chatService.createChat(prompt.value)
    navigateTo('/app/chat/' + chatId.value + "?prompt=" + prompt.value)
    return
  }

  loading.value = true
  await chatService.sendMessage(prompt.value)
  messages.value = chatService.messages
  // console.log(chatService.messages)
  // console.log(messages.value)
  loading.value = false
  prompt.value = ''
}

</script>

<style>

</style>