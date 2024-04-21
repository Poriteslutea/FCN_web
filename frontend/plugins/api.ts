


export default defineNuxtPlugin(() => {

    const authStore = useAuthStore()
    const config = useRuntimeConfig()

    const $api = $fetch.create({
      baseURL: config.public.apiBaseUrl,
      onRequest({ request, options, error }) {
        if (authStore.userToken) {
          // Add Authorization header
          options.headers = options.headers || {}
          options.headers.Authorization = `Bearer ${authStore.userToken}`
        }
      },
      onResponseError({ request, response }) {
        if (response.status === 401) {
          return navigateTo('/login')
        }
      }
    })
    return {
      provide: {
        api: $api
      }
    }
  })