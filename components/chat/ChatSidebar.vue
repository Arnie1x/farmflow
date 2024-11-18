<template>
  <div class="h-full w-[18.75rem] xl:flex hidden flex-col gap-2 overflow-y-scroll">
    <p class="text-2xl font-bold">Recent Chats</p>
    <!-- <p class="text-xl font-bold">Today</p> -->
    <ChatHistoryItem v-for="chat in allChats" :id="chat.id" :key="chat.id" :title="chat.title" />
  </div>
</template>

<script lang="ts" setup>
import ChatService from '~/types/chat_service';

const chatService = new ChatService();
const allChats = ref([])

allChats.value = await chatService.getAllChats()
</script>

<style></style>