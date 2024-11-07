<!-- eslint-disable vue/first-attribute-linebreak -->
<template>
  <div class="w-full h-full flex flex-col gap-3 justify-between items-baseline p-2">
    <div class="flex flex-col gap-12 w-full items-start">
      <LogoItem />
      <ul class="w-full flex flex-col gap-2">
        <NuxtLink to="/app">
          <li>
            <svg width="28" height="28" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path class="svg-icon"
                d="M26.25 23.75V15.3338C26.25 14.6556 26.112 13.9845 25.8445 13.3613C25.577 12.7381 25.1854 12.1759 24.6937 11.7088L16.7225 4.13751C16.2579 3.69612 15.6415 3.45001 15.0006 3.45001C14.3598 3.45001 13.7434 3.69612 13.2788 4.13751L5.30625 11.7088C4.81457 12.1759 4.42304 12.7381 4.15551 13.3613C3.88797 13.9845 3.75 14.6556 3.75 15.3338V23.75C3.75 24.4131 4.01339 25.0489 4.48223 25.5178C4.95107 25.9866 5.58696 26.25 6.25 26.25H23.75C24.413 26.25 25.0489 25.9866 25.5178 25.5178C25.9866 25.0489 26.25 24.4131 26.25 23.75Z"
                stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <p>Dashboard</p>
          </li>
        </NuxtLink>
        <NuxtLink to="/app/chat">
          <li>
            <svg width="28" height="28" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path class="svg-icon"
                d="M7 24.9L8.905 23.3763L8.9175 23.3663C9.315 23.0475 9.51625 22.8875 9.74 22.7737C9.94083 22.6712 10.1525 22.5971 10.375 22.5513C10.6238 22.5 10.8825 22.5 11.4025 22.5H22.2537C23.6512 22.5 24.3513 22.5 24.885 22.2275C25.3554 21.9878 25.7378 21.6054 25.9775 21.135C26.25 20.6 26.25 19.9 26.25 18.505V8.99625C26.25 7.59875 26.25 6.89875 25.9775 6.365C25.7375 5.89443 25.3546 5.51197 24.8837 5.2725C24.35 5 23.65 5 22.25 5H7.75C6.35 5 5.65 5 5.115 5.2725C4.64462 5.51218 4.26218 5.89462 4.0225 6.365C3.75 6.9 3.75 7.6 3.75 9V23.3387C3.75 24.6712 3.75 25.3375 4.0225 25.6787C4.13968 25.8259 4.28854 25.9447 4.45801 26.0263C4.62747 26.1078 4.81317 26.1501 5.00125 26.15C5.43875 26.15 5.95875 25.7325 7 24.9Z"
                stroke="#848AA0" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <p>Chat</p>
          </li>
        </NuxtLink>
        <NuxtLink to="/app/farms">
          <li>
            <svg width="28" height="28" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path class="svg-icon-fill"
                d="M28.75 5.125V2.875L26.5 2.625C26.375 2.625 25.625 2.5 24.375 2.5C19.25 2.5 15.5 4 13.375 6.625C11.75 5.625 9.5 5 6.875 5C5.625 5 4.75 5.125 4.75 5.125L2.375 5.5L2.5 7.625C2.625 11.375 4.5 18.5 11 18.5H11.25V22.75C6.5 23.375 2.5 25 2.5 25V27.5H27.5V25C27.5 25 23.5 23.375 18.75 22.75V18.75C26.625 18.625 28.75 9.75 28.75 5.125ZM15 22.5H13.75V15.5C13.75 15.5 13.5 11.25 10 11.25C10 11.25 11.875 12.25 12.375 15.875C11.875 16 11.375 16 11 16C5.25 16 5 7.625 5 7.625C5 7.625 5.75 7.5 6.875 7.5C9.25 7.5 13.125 8 14.25 11.375C14.875 5.75 21.25 5 24.375 5C25.5 5 26.25 5.125 26.25 5.125C26.25 5.125 26.25 16.375 18.375 16.375H17.5C17.5 13.875 20 10.125 20 10.125C16.25 11.375 16.25 16.25 16.25 16.25V22.5H15Z"
                fill="#848AA0" />
            </svg>
            <p>Farms</p>
          </li>
        </NuxtLink>
        <NuxtLink to="/app/calendar">
          <li>
            <svg width="28" height="28" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path class="svg-icon" d="M10 2.5V7.5M20 2.5V7.5" stroke="#848AA0" stroke-width="3" stroke-linecap="round"
                stroke-linejoin="round" />
              <path class="svg-icon"
                d="M23.75 5H6.25C4.86929 5 3.75 6.11929 3.75 7.5V25C3.75 26.3807 4.86929 27.5 6.25 27.5H23.75C25.1307 27.5 26.25 26.3807 26.25 25V7.5C26.25 6.11929 25.1307 5 23.75 5Z"
                stroke="#848AA0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
              <path class="svg-icon" d="M3.75 12.5H26.25" stroke="#848AA0" stroke-width="3" stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
            <p>Calendar</p>
          </li>
        </NuxtLink>
        <NuxtLink to="/app/faq">
          <li>
            <svg width="28" height="28" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect class="svg-icon" x="3" y="3" width="24" height="24" rx="5" stroke="#848AA0" stroke-width="3"
                stroke-linecap="round" stroke-linejoin="round" />
              <path class="svg-icon"
                d="M14.9999 17.6239C14.9999 14.1192 18.4994 14.9941 18.4994 11.4894C18.4994 6.83687 11.5005 6.83687 11.5005 11.4894M14.9999 22V21.1251"
                stroke="#848AA0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <p>FAQs</p>
          </li>
        </NuxtLink>
      </ul>
    </div>
    <ul class="w-full flex flex-col gap-2">
      <NuxtLink to="/">
        <li>
          <svg width="32" height="32" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path class="svg-icon"
              d="M23.75 26.25V29.375C23.75 30.2038 23.4208 30.9987 22.8347 31.5847C22.2487 32.1708 21.4538 32.5 20.625 32.5H8.125C7.2962 32.5 6.50134 32.1708 5.91529 31.5847C5.32924 30.9987 5 30.2038 5 29.375V10.625C5 9.7962 5.32924 9.00134 5.91529 8.41529C6.50134 7.82924 7.2962 7.5 8.125 7.5H20C21.7258 7.5 23.75 8.89922 23.75 10.625V13.75M28.75 26.25L35 20L28.75 13.75M13.75 20H33.75"
              stroke="#848AA0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
          </svg>

          <p>Sign Out</p>
        </li>
      </NuxtLink>
    </ul>
  </div>
</template>

<script lang="ts" setup>
const route = useRoute()
const path = route.path

const isDashboard = ref(false)
const isChat = ref(false)
const isFarms = ref(false)
const isFaq = ref(false)

if (path.includes('app')) {
  isDashboard.value = true
  isChat.value = false
  isFarms.value = false
  isFaq.value = false
}
else if (path.includes('chat')) {
  isChat.value = true
  isDashboard.value = false
  isFarms.value = false
  isFaq.value = false
}
else if (path.includes('farms')) {
  isDashboard.value = false
  isChat.value = false
  isFarms.value = true
  isFaq.value = false
}
else if (path.includes('faq')) {
  isDashboard.value = false
  isChat.value = false
  isFarms.value = false
  isFaq.value = true
}

</script>

<style scoped>
li {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border-radius: 1rem;
  color: #F8F8F8;
  width: 100%;

  background-color: transparent;

  font-size: 1.25rem;

  transition: 0.5s all ease;
}

li:hover {
  background-color: #848aa04D;
}

li:focus {
  background-color: #848aa080;
}

li:hover .svg-icon {
  stroke: #2B9B3C;
}

li:hover .svg-icon-fill {
  fill: #2B9B3C;
}

.svg-icon {
  stroke: #848AA0;
  transition: 0.5s all ease;
}

.svg-icon-fill {
  fill: #848AA0;
  transition: 0.5s all ease;
}

.router-link-active li {
  background-color: #848aa04D;
}

.router-link-active .svg-icon {
  stroke: #2B9B3C;
}

.router-link-active .svg-icon-fill {
  fill: #2B9B3C;
}
</style>