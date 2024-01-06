// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@formkit/nuxt',
    'nuxt-svgo'
  ],
  formkit: {
    autoImport: true,
    configFile: './formkit.config.ts'
  }
})
