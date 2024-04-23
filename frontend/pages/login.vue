<template>

    <div class="flex justify-center items-center bg-gradient-to-br from-blue-950 to-teal-400 bg-teal-400 h-screen">

  
            
            <div class="flex flex-col p-12 px-20 bg-white bg-opacity-10 shadow-2xl rounded-lg animate__animated animate__backInRight ">

                <IconFish class="text-white w-40 mb-8 mx-auto" :class="{'animate__animated': shakeFish === true, 'animate__tada': shakeFish === true}" :fontControlled="false"/>

                
                <div v-if="!register" class="flex justify-center">
                    <FormKit
                    type="form"
                    id="login-form"
                    :form-class="submitted ? 'hide' : 'show'"
                    @submit="loginAction"
                    :actions="false"
                    #default="{ value }"
                    >       
                    <FormKit
                        type="text"
                        name="email"
                        label="Email"
                        validation="required|email"
                        placeholder="example@example.com"
                        :classes="{
                            outer: 'mb-2',
                            label: 'mb-1 font-bold text-base text-white',
                            inner: 'rounded-lg',
                            input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                            message: 'text-sm mt-1 text-red-900'
                        }"
                        />
                                
                    <FormKit
                        type="password"
                        name="password"
                        label="Password"
                        validation="required|length:6"
                        :validation-messages="{
                        length: 'Please enter at least 6 characters',
                        }"
                        placeholder="Your password"
                        :classes="{
                            outer: 'mb-2',
                            label: 'mb-1 font-bold text-base text-white',
                            inner: 'rounded-lg',
                            input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                            message: 'text-sm mt-1 text-red-900'
                        }"
                    />
                    
                    <!-- <button class="w-full rounded-lg bg-teal-500 hover:bg-teal-400 py-2 font-bold text-gray-200 shadow-sm mt-3">Register</button>    -->
                
                    <div class="flex flex-col mt-3">
                        <button class="w-full rounded-lg bg-teal-500 hover:bg-teal-400 py-2 font-bold text-white shadow-sm mt-1 border-solid border-gray-500">Log in</button>
                        <div class="flex items-center justify-center mt-3">
                            <div class="border-t border-gray-400 border-s-2 flex-grow"></div>
                            <div class="mx-2 text-gray-300">or</div>
                            <div class="border-t border-gray-400 border-s-2 flex-grow"></div>
                        </div>
                        <a class="text-gray-300 text-center mt-1 hover:text-white hover:underline cursor-pointer" @click="goRegister"> create an account</a>
                    </div>

                </FormKit>  
                
                </div>
                
                <div v-if="register" class="flex justify-center">

                    <FormKit
                    type="form"
                    id="register-form"
                    :form-class="submitted ? 'hide' : 'show'"
                    @submit="registerAction"
                    :actions="false"
                    #default="{ value }"
                    >

                    <FormKit
                        type="text"
                        name="email"
                        label="Email"
                        validation="required|email"
                        placeholder="example@example.com"
                        :classes="{
                            outer: 'mb-2',
                            label: 'mb-1 font-bold text-base text-white',
                            inner: 'rounded-lg',
                            input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                            message: 'text-sm mt-1 text-red-900'
                        }"
                        />
                    
                        <FormKit
                        type="text"
                        name="name"
                        label="Name"
                        placeholder="enter your name"
                        :classes="{
                            outer: 'mb-2',
                            label: 'mb-1 font-bold text-base text-white',
                            inner: 'rounded-lg',
                            input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                            message: 'text-sm mt-1 text-red-900'
                        }"
                        />
                            
                    <div>
                        <FormKit
                            type="password"
                            name="password"
                            label="Password"
                            validation="required|length:6"
                            :validation-messages="{
                            length: 'Please enter at least 6 characters',
                            }"
                            placeholder="Your password"
                            :classes="{
                                outer: 'mb-2',
                                label: 'mb-1 font-bold text-base text-white',
                                inner: 'rounded-lg',
                                input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                                message: 'text-sm mt-1 text-red-900'
                            }"
                        />
                        
                    </div>

                    <div class="flex flex-col mt-3">
                        <button class="w-full rounded-lg bg-teal-500 hover:bg-teal-400 py-2 font-bold text-white shadow-sm mt-4 border-solid border-gray-500">Register</button>   
                        <div class="flex items-center justify-center mt-3">
                            <div class="border-t border-gray-400 border-s-2 flex-grow"></div>
                            <div class="mx-2 text-gray-300">or</div>
                            <div class="border-t border-gray-400 border-s-2 flex-grow"></div>
                        </div>
                        <a class="text-gray-300 text-center mt-1 hover:text-white hover:underline cursor-pointer" @click="goLogin">Log in</a>
                    </div>

                    </FormKit>

                

                </div>
                <!-- <button class="bg-teal-500 p-2 px-3 rounded-lg text-bold text-white" @click="testGet">click me</button> -->
            </div>
    
    </div>
 
  
</template>


<script setup>
import IconFish from '~/assets/icons/fish_icon.svg'
import { encodeURL } from '~/composables/utils.ts'
import 'animate.css'
const config = useRuntimeConfig()
const submitted = ref(false)
const register = ref(false)
const authStore = useAuthStore()
const router = useRouter()

definePageMeta({
  layout: false,
})


const loginAction = async (data) => {
  // Let's pretend this is an ajax request:

        const details = {
            'username': data.email,
            'password': data.password,
        }
        const formBody = encodeURL(details)

        const {data: tokenData, error} = await useFetch(`${config.public.apiBaseUrl}/member/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: formBody,
        })

        if (error.value) {
          alert(`登入失敗：${error.value}`)
        }

        if (tokenData.value) {
          authStore.storeToken(tokenData.value.access_token)
          await authStore.getMember()
          navigateTo('/') 
        }
        submitted.value = true
}

const shakeFish = ref(false)

const goRegister = async() => {
    register.value = true
    shakeFish.value = true
    await new Promise((r) => setTimeout(r, 1000))
    shakeFish.value = false
}

const goLogin = async() => {
    register.value = false
    shakeFish.value = true
    await new Promise((r) => setTimeout(r, 1000))
    shakeFish.value = false
}


const registerAction = async (data) => {

    try {
        const response = await fetch(`${config.public.apiBaseUrl}/member/register`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: data.email,
            username: data.name,
            password: data.password,
          }),
        })

        if (response.ok) {
          alert('Member created successfully');
        } else {
          const errorData = await response.json()
          console.error('Register failed!', errorData.detail)
          alert(errorData.detail)
        }
      } catch (error) {
        console.error('Error creating member:', error);
      }

}


</script>