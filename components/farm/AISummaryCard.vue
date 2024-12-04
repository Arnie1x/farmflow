<template>
  <div class="w-full min-w-[18.75rem] rounded-2xl border-2 p-5 flex flex-col justify-between gap-5">
    <div class="flex flex-row gap-2 justify-start items-center">
      <NuxtImg src="/images/icons/ai.svg" alt="ai" class="w-[2rem]" />
      <h1 class="text-3xl font-bold text-[#058ED9]">AI Summary</h1>
    </div>
    <p v-if="summary !== ''" class="">{{ summary }}</p>
    <p v-else-if="loading" class="text-xl">Generating Summary... <span class="animate-spin">⠋</span></p>
    <p v-else class="text-lg">There is insufficient data to create your personalized summary. Please begin recording activities for the Summary creation to begin.</p>
  </div>
</template>

<script lang="ts" setup>
import ChatService from '~/types/chat_service';
const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const chatService = new ChatService()
const summary = ref('')
const loading = ref(true)

onMounted(async () => {
  summary.value = await getAISummary()
})

async function getAISummary() {
  try {
    loading.value = true
    const farmSummary = await chatService.getFarmAISummary(props.id)
    loading.value = false
    return farmSummary
  } catch (error) {
    loading.value = false
    console.log(error)
    return ''
  }
}

</script>

<style>

</style>