// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@formkit/nuxt',
    'nuxt-svgo',
    '@pinia/nuxt'
  ],
  formkit: {
    autoImport: true,
    configFile: './formkit.config.ts'
  },
  runtimeConfig: {
    public: {
      webHost: process.env.WEB_HOST,
      apiBaseUrl: process.env.API_BASE_URL,
    }   
  }
})
