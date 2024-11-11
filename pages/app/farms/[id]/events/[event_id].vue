<template>
  <NuxtLayout name="app">
    <template #header>
      <h1 class="text-3xl font-bold">Edit Farm Event</h1>
      <div class="button-outlined flex flex-row gap-3 justify-center items-center cursor-pointer" @click="deleteEvent">
        <svg width="28" height="29" viewBox="0 0 28 29" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path class="delete-btn-svg"
            d="M22.75 6.91665L22.281 14.507M5.25 6.91665L5.95583 18.6125C6.1355 21.6073 6.2265 23.1041 6.9755 24.1821C7.34533 24.7141 7.8225 25.1645 8.3755 25.5016C9.15833 25.98 10.1278 26.1235 11.6667 26.1666M23.3333 18L15.1667 26.1666M23.3333 26.1666L15.1667 18M3.5 6.91665H24.5M18.732 6.91665L17.9352 5.27398C17.4067 4.18198 17.1418 3.63715 16.6857 3.29648C16.5843 3.22101 16.477 3.15391 16.3648 3.09581C15.8597 2.83331 15.253 2.83331 14.0408 2.83331C12.7972 2.83331 12.1753 2.83331 11.6608 3.10631C11.5471 3.16723 11.4386 3.23747 11.3365 3.31631C10.8757 3.66981 10.6178 4.23565 10.1022 5.36615L9.39517 6.91665"
            stroke="#D7263D" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <p class="text-xl">Delete</p>
      </div>
    </template>
    <FarmEventsForm />
  </NuxtLayout>
</template>

<script lang="ts" setup>

const route = useRoute()
const eventId = route.params.event_id
const farmId = route.params.id
const client = useSupabaseClient()

async function deleteEvent() {
  try {
    let { error } = await client
      .from('events')
      .delete()
      .eq('id', eventId)
    if (error) {
      throw error
    }
    navigateTo('/app/farms/' + farmId + '/events')
  } catch (error) {
    console.log(error)
  }
}
</script>

<style scoped>

.delete-btn-svg {
  stroke: #D7263D;
  transition: 0.1s all ease;
}

.delete-btn-svg:hover {
  stroke: #FFFFFF;
}

.button-outlined {
  padding-left: 1rem;
  padding-right: 1rem;
  outline: auto;
  outline-color: #D7263D;
  color: #D7263D;
  stroke: #D7263D;
  border-radius: 1.25rem;
  min-height: 3.125rem;
  border-radius: 1rem;
  font-size: 1.25rem;
  font-weight: 500;
  transition: 0.5s all ease;
}

.button-outlined:hover {
  background-color: #D7263D;
  color: #fff;
  stroke: #fff;
}

.button-outlined:hover .delete-btn-svg {
  stroke: #fff;
}

.button-outlined:active {
  background-color: #D7263D;
  color: #fff;
}

</style>