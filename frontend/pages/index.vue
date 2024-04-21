
<template>
   <div class="flex flex-col items-center">
    <h2 class="text-3xl font-semibold mb-4 text-center text-white">Hi {{ username }}! You logged in successfully :) </h2>
    <button class="rounded-lg bg-teal-500 hover:bg-teal-400 text-white text-center text-2xl font-semibold px-3 py-1"
    @click="logoutAction">Log out</button> 
   </div>
    
</template>

<script setup>

definePageMeta({
  middleware: ["auth"]
})

// const { data, error } = await useAPI('/member/me')

const authStore = useAuthStore()
const username = ref('')
username.value = authStore.member.username

const logoutAction = () => {
  authStore.removeToken()
  console.log(authStore.isLoggedIn, authStore.userToken)
  return navigateTo('/login')
}


</script>