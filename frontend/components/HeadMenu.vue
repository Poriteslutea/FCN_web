<template>
    
   
   
    <div class="fixed top-0 left-0 z-10 w-20 h-screen transition-transform bg-gradient-to-br from-blue-950 to-teal-600 rounded-tr-lg rounded-br-lg">
        <div class="flex flex-col h-full items-end pr-3">
            <div class="grow-0 mb-8">
                <IconFish class="text-6xl text-white p-1 mx-auto mt-2 cursor-pointer" @click="toggleMenu"/>
            </div>
            <div class="grow flex flex-col justify-start">
                <IconDashboard class="grow-0 mt-2 text-6xl text-teal-200 hover:text-teal-100 p-2 mx-auto cursor-pointer"
                    @click="selectPane('product')"/>
            </div>
            
            <div class="relative inline-block pt-8" @mouseover="isHoverUser = true" @mouseleave="isHoverUser = false">
                <button class="mx-auto">
                    <IconUser class="text-6xl text-teal-200 hover:text-teal-100 p-2"/>
                </button>
                <div v-if="isHoverUser" 
                    class="absolute left-6 -top-5 min-w-40 z-20">
                    <button class="text-xl text-center bg-teal-500 hover:bg-teal-400 px-10 py-3 rounded-lg" @click="logoutAction"> 登出 </button>
                </div>
            </div>
                
           
        </div> 
    </div>

    <!-- <div :class="[{'translate-x-20': isMenuOpen, '-translate-x-full': !isMenuOpen}, 
         'fixed top-0 left-0 w-64 z-40 transition-transform bg-teal-500']">
    
    </div> -->

    
</template>

<script setup>
import IconFish from '~/assets/icons/fish_icon.svg'
import IconMenu from '~/assets/icons/menu.svg'
import IconDashboard from '~/assets/icons/dashboard.svg'
import IconUser from '~/assets/icons/user.svg'
import IconArrowLeft from '~/assets/icons/double_arrow.svg'
import ProductPane from '~/components/ProductPane.vue'

const asidePaneStore = useAsidePaneStore()
const { isExpand } = storeToRefs(asidePaneStore)
const authStore = useAuthStore()
const username = ref('')
username.value = authStore.member.username
const isHoverUser = ref(false)

const logoutAction = () => {
  authStore.removeToken()
  console.log(authStore.isLoggedIn, authStore.userToken)
  return navigateTo('/login')
}

const isMenuOpen = ref(false)
const toggleMenu = ()=>{
    isMenuOpen.value = !isMenuOpen.value
}

const selectPane = (tag) => {
    if (tag === 'product') {
        // asidePaneStore.selectComponent(ProductPane)
        isExpand.value = !isExpand.value
        asidePaneStore.isExpand = isExpand.value
        console.log(asidePaneStore.isExpand)
        // console.log(asidePaneStore.component)
    }
}


</script>