export default defineNuxtRouteMiddleware(async (to) => {

    const authStore = useAuthStore()

    if(!authStore.isLoggedIn){
        return navigateTo('/login')
    }else{
        authStore.getMember()
    }
  })