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
      <input id="end_date" @input="checkCompletionStatus" v-model="end_date" type="datetime-local" class="text-black textfield" name="end_date"
        placeholder="End Date *">
      <div v-if="show_is_completed" class="flex flex-row gap-2">
        <input id="is_completed" v-model="is_completed" type="checkbox" class="text-black w-5" name="is_completed"
          placeholder="Is Completed">
        <label for="is_completed">Is Completed?</label>
      </div>
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

const event = ref(null)
const event_name = ref('')
const description = ref('')
const start_date = ref('')
const end_date = ref(new Date().toISOString().slice(0, 16))
const show_is_completed = ref(false)
const is_completed = ref(false)
const errorMsg = ref('')
const farmId = route.params.id

event.value = await getEvent()

if (route.params.event_id) {
  isUpdate.value = true
}

if (isUpdate.value) {
  show_is_completed.value = true
  event_name.value = event.value.name
  description.value = event.value.description
  start_date.value = new Date(event.value.start_date).toISOString().slice(0, 16)
  end_date.value = new Date(event.value.end_date).toISOString().slice(0, 16)
}

function checkCompletionStatus(){
  if (end_date.value < new Date()) {
    is_completed.value = true
  }
  else {
    is_completed.value = false
  }
}

const submitForm = () => {
  if (isUpdate.value) {
    updateEvent()
  } else {
    createEvent()
  }
}

async function getEvent() {
  try {
    const eventId = route.params.event_id
    let { data: event, error } = await client
      .from('events')
      .select('*')
      .eq('id', eventId)
      .single()
    if (error) {
      throw error
    }
    return event
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
        { user_id: user.value.id, farm_id: farmId, name: event_name.value, description: description.value, start_date: start_date.value, end_date: end_date.value, is_completed: is_completed.value }
      )
    if (error) {
      throw error
    }
    navigateTo('/app/farms/' + farmId + '/events')
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
      .eq('id', event.value.id).select()
    if (error) {
      throw error
    }
    console.log(data)
    navigateTo('/app/farms/' + farmId + '/events')
  } catch (error) {
    errorMsg.value = error.message
  }
}

</script>

<style></style>