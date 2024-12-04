import type { NuxtPage } from "nuxt/schema"

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  ssr: true,
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxt/fonts',
    '@nuxtjs/supabase',
    '@nuxt/eslint',
    '@formkit/auto-animate/nuxt',
    '@nuxtjs/mdc'
  ],
  supabase: {
    redirect: false,
  },
  // image: {
  //   domains: ['openweathermap.org'], // Allow OpenWeatherAPI images to be used directly
  //   providers: {
  //     openWeather: {
  //       name: 'openWeather',
  //       provider: 'static',
  //     },
  //   },
  // },
  runtimeConfig: {
    // The private keys which are only available within server-side
    // mapboxAccessToken: '',
    // Keys within public, will be also exposed to the client-side
    public: {
      mapboxAccessToken: process.env.MAPBOX_ACCESS_TOKEN,
      openWeatherMapApiKey: process.env.OPEN_WEATHER_MAP_API_KEY,
      huggingFaceApiToken: process.env.HUGGINGFACE_API_TOKEN
    }
  }
})