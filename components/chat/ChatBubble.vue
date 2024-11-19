<template>
  <div v-if="isUser" class="w-full flex justify-end">
    <div class="flex flex-col w-fit h-full">
      <div class="w-full max-w-[38rem] h-fit p-5 bg-[#848AA04D] rounded-2xl">
        <p class="whitespace-pre-line">{{ message }}</p>
      </div>
    </div>
  </div>
  <div v-else class="w-full flex justify-start">
    <div class="flex flex-col w-fit h-full">
      <div class="w-full xl:max-w-[38rem] h-fit p-5">
        <p class="whitespace-pre-line"><MDC :value="message" tag="ai-response" /></p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  message: {
    type: String,
    required: false,
    default: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt ducimus odit nulla minus necessitatibus. Dolore debitis nam exercitationem itaque fugiat eos impedit corrupti nihil molestias consequatur deleniti error quas dolorum ipsum ad culpa, adipisci minima quasi, consequuntur vero. Accusamus, reiciendis?'
  },
  isUser: {
    type: Boolean,
    required: false,
    default: true
  }
})
</script>

<style></style>