<template>
  <form class="w-full h-full flex xl:flex-row flex-col gap-3" @submit.prevent="submitForm">
    <div class="flex flex-col gap-3 max-w-[64rem] w-full">
      <p>(*) Required Field</p>
      <input id="name" v-model="event_name" type="text" class="text-black textfield" name="event_name"
        placeholder="Event Name *">
      <input id="description" v-model="description" type="text" class="text-black textfield" name="description"
        placeholder="Description">
      <p>Start Date</p>
      <input id="start_date" v-model="start_date" type="datetime-local" class="text-black textfield" name="start_date"
        placeholder="Start Date">
      <p>End Date *</p>
      <input id="end_date" v-model="end_date" type="datetime-local" class="text-black textfield" name="end_date"
        placeholder="End Date *">
    </div>
    <div class="xl:max-w-[25rem] w-full">
      <p v-if="errorMsg" class="text-red-500 w-full text-center">{{ errorMsg }}</p>
      <button class="text-white button h-min xl:max-w-[25rem] w-full">{{ isUpdate ? 'Update Event' : 'Add Event' }}</button>
    </div>
  </form>
</template>

<script lang="ts" setup>
const isUpdate = ref(false)
const route = useRoute()
const client = useSupabaseClient()
const user = useSupabaseUser()

const farm = ref(null)
const event_name = ref('')
const description = ref('')
const start_date = ref('')
const end_date = ref(new Date())
const is_completed = ref(false)
const errorMsg = ref('')

farm.value = await getFarm()

if (route.path.includes('edit')) {
  isUpdate.value = true
}

if (isUpdate.value) {
  event_name.value = farm.value.name
  description.value = farm.value.description
  start_date.value = farm.value.start_date
  end_date.value = farm.value.end_date
}

const submitForm = () => {
  if (end_date.value > new Date()) {
    is_completed.value = false
  }
  else {
    is_completed.value = true
  }

  if (isUpdate.value) {
    updateEvent()
  } else {
    createEvent()
  }
}

async function getFarm() {
  try {
    const farmId = route.params.id
    let { data: farm, error } = await client
      .from('farms')
      .select('*')
      .eq('id', farmId)
      .single()
    if (error) {
      throw error
    }
    return farm
  } catch (error) {
    console.log(error)
  }
}

async function createEvent() {
  // TODO:: Need to add validation
  try {
    const { error } = await client
      .from('events')
      .insert(
        { user_id: user.value.id, farm_id: farm.value.id, name: event_name.value, description: description.value, start_date: start_date.value, end_date: end_date.value, is_completed: is_completed.value }
      )
    if (error) {
      throw error
    }
    navigateTo('/app/farms/' + farm.value.id + '/events')
  } catch (error) {
    errorMsg.value = error.message
  }
}

async function updateEvent() {
  // TODO:: Need to add validation
  try {
    const { data, error } = await client
      .from('events')
      .update({ name: event_name.value, description: description.value, start_date: start_date.value, end_date: end_date.value, is_completed: is_completed.value, updated_at: new Date() })
      .eq('id', farm.value.id).select()
    if (error) {
      throw error
    }
    console.log(data)
    navigateTo('/app/farms/' + farm.value.id + '/events')
  } catch (error) {
    errorMsg.value = error.message
  }
}

</script>

<style></style>