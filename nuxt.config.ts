import type { NuxtPage } from "nuxt/schema"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxt/fonts',
    '@nuxtjs/supabase',
    '@nuxt/eslint'
  ],
  supabase: {
    redirect: false,
  },
  runtimeConfig: {
    // The private keys which are only available within server-side
    // mapboxAccessToken: '',
    // Keys within public, will be also exposed to the client-side
    public: {
      mapboxAccessToken: process.env.MAPBOX_ACCESS_TOKEN,
    }
  }
})