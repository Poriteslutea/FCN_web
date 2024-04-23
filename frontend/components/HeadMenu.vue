<template>
    
   
    <div class="items-center bg-gradient-to-br from-blue-950 to-teal-600 w-screen">
        <div class="flex flex-row gap-2 p-3">
            <div class="text-3xl p-6 text-white font-bold">FCN</div>
            <div class="flex-grow"></div>
            <div class="text-2xl p-6 text-white items-center">Hi~! {{ username }}</div>
            <button class="rounded-lg bg-teal-500 hover:bg-teal-400 text-white text-center text-xl px-6 my-4 mr-4"
            @click="logoutAction">登出</button> 

        </div>
      
    </div>
    
</template>

<script setup>

const authStore = useAuthStore()
const username = ref('')
username.value = authStore.member.username

const logoutAction = () => {
  authStore.removeToken()
  console.log(authStore.isLoggedIn, authStore.userToken)
  return navigateTo('/login')
}


</script>