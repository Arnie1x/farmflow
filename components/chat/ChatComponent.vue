<template>
  <div class="flex flex-row gap-5 w-full h-full">
    <div class="w-full h-full flex flex-col gap-3 align-bottom justify-end">
      <div v-if="messages.length > 0" v-auto-animate
        class="w-full h-full flex flex-col-reverse gap-3 overflow-y-scroll overflow-x-hidden">
        <!-- Look into different ways of making this scroll behavior if the flex-col-reverse doesn't work -->
        <div v-for="message in messages.toReversed()" :key="message.id">
          <ChatBubble :message="message.message" :is-user="message.is_user" />
        </div>
      </div>
      <p v-if="loading" class="text-sm font-bold px-5 animate-pulse">Loading...</p>
      <div v-if="toggleFarmSelect" class="relative w-full">
        <ul v-show="farmList" class="w-full rounded-2xl px-4 bg-[#dadce2] absolute bottom-0 max-h-[15rem] overflow-scroll">
          <p class="text-lg font-bold py-2">Select Farm:</p>
          <li @click="setFarm(null)" class="cursor-pointer py-1 hover:font-medium duration-200">None</li>
          <li v-for="farm in farmList" :key="farm['id']" class="cursor-pointer py-2 hover:font-medium duration-200"
          @click="setFarm(farm)">
          {{ farm['name'] }}
        </li>
      </ul>
    </div>
    <p @click="toggleFarmSelect = !toggleFarmSelect" class="text-sm font-bold px-5 text-[#848AA0] cursor-pointer">{{ selectedFarm }}</p>
      <form class="flex flex-row gap-3 h-min" @submit.prevent="sendMessage">
        <textarea v-model="prompt" class="w-full textfield" placeholder="Start Typing" rows="1" :disabled="loading" />
        <button v-auto-animate type="submit" class="button max-w-[3.5rem] max-h-[3.5rem]">
          <NuxtImg v-if="!loading" src="/images/icons/send.svg" alt="send" class="w-full p-3" />
          <NuxtImg v-else src="/images/icons/loading.svg" alt="send" class="w-full p-3 animate-spin" />
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

const client = useSupabaseClient()

const messages = ref([])
const prompt = ref('')
const loading = ref(false)

const toggleFarmSelect = ref(false)
const selectedFarm = ref('Select a Farm')
const selectedfarmId = ref(null)
const farmList = ref([])

const chatId = ref('')
const route = useRoute()
const query = route.query

await getFarms()

const chatService = new ChatService()
if (route.params.id) {
  chatId.value = route.params.id
  chatService.setChatId(chatId.value)
}

if (chatService.hasChatID()) {
  await chatService.getAllMessages()
}
messages.value = chatService.messages

if (query.prompt && messages.value.length === 0) {
  prompt.value = query.prompt
  if (query.farm) {
    const selectedFarm = farmList.value.find(farm => farm.id === parseInt(query.farm))
    console.log(selectedFarm)
    setFarm(selectedFarm)
  }
  // loading.value = true
  await sendMessage()
}

async function sendMessage() {
  if (!prompt.value) return

  loading.value = true
  if (!route.params.id) {
    chatId.value = await chatService.createChat(prompt.value)
    if (selectedfarmId.value) {
      navigateTo('/app/chat/' + chatId.value + "?prompt=" + prompt.value + "&farm=" + selectedfarmId.value)
    }
    else {
      navigateTo('/app/chat/' + chatId.value + "?prompt=" + prompt.value)
    }
    return
  }

  await chatService.sendMessage(prompt.value, selectedfarmId.value)
  messages.value = chatService.messages
  // console.log(chatService.messages)
  // console.log(messages.value)
  loading.value = false
  prompt.value = ''
}


async function getFarms() {
  try {
    const { data, error } = await client.from('farms').select('*')
    if (error) {
      throw error
    }
    farmList.value = data
  } catch (error) {
    console.error(error)
  }
}

function setFarm(farm) {
  if (farm === null) {
    selectedFarm.value = 'Select a Farm'
    selectedfarmId.value = null
  }
  else{
    selectedFarm.value = farm.name
    selectedfarmId.value = farm.id
  }
  toggleFarmSelect.value = false
}

</script>

<style></style>