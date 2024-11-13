<template>
  <div class="w-full flex xl:flex-row flex-col justify-between items-center p-3 rounded-2xl border-2">
    <div class="flex flex-row justify-center gap-5 items-center w-full xl:py-0 py-3">
      <div class="flex flex-col justify-center items-center px-3 pl-8">
        <p class="font-bold">Mon</p>
        <p class="text-3xl font-bold text-[#2B9B3C]">28</p>
      </div>
      <div class="border h-[2.5rem] mx-4" />
      <div class="flex flex-col min-w-[10rem]">
        <div class="flex flex-row gap-2 justify-start">
          <NuxtImg src="/images/icons/location.svg" alt="location" class="w-[1.25rem]" />
          <p class="text-base text-ellipsis line-clamp-1">Sunny Fields</p>
        </div>
        <div class="flex flex-row gap-2 justify-start">
          <NuxtImg src="/images/icons/location.svg" alt="location" class="w-[1.25rem]" />
          <p class="text-base">09:00</p>
        </div>
      </div>
    </div>
    <div class="border h-[2.5rem] mx-4 xl:block hidden" />
    <div>
      <p class="text-ellipsis line-clamp-2">Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore impedit
        doloribus dolorem numquam similique vitae, illo dolores. Amet sunt blanditiis rem pariatur eum unde incidunt
        consectetur praesentium! Id repellat deleniti vitae aliquid, repellendus exercitationem delectus dolor
        fugiat
        qui quos consequuntur iure dolorem numquam minus aut sequi mollitia magni. Ea nihil sint mollitia eligendi
        laborum!</p>
    </div>
    <div>
      <!-- <NuxtLink :to="{ name: 'app-farms-id-events-event_id', params: { id: farmId, event_id: event.id } }" -->
      <NuxtLink class="link flex flex-row gap-3 justify-center items-center p-4 min-w-[8rem]">
        <p class="text-xl">Edit</p>
        <svg width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.5 5.25L10 12.75L2.5 5.25L1 6.75L10 15.75L19 6.75L17.5 5.25Z" fill="#104547" class="link-svg" />
        </svg>
      </NuxtLink>
    </div>
  </div>
</template>

<script lang="ts" setup>

</script>

<style scoped>

.link-svg {
  fill: #104547;
  transition: 0.5s all ease;
}

.link {
  color: #104547;
  transition: 0.5s all ease;
}

.link:hover {
  cursor: pointer;
  color: #2ac241;
  fill: #2ac241;
}

.link:hover .link-svg {
  fill: #2ac241;
}

</style>