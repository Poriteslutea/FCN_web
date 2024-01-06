<template>
    <div class="bg-gradient-to-br from-blue-950 to-teal-400 h-screen flex bg-teal-400 justify-center items-center ">
        <div class="container flex items-center flex-col">
            <div class="bg-white bg-opacity-10 shadow-2xl rounded-lg p-8 justify-center">

                <IconFish class="text-white w-40 my-8 mx-auto hover:translate-x-3" :fontControlled="false"/>
                <div v-if="!register">
                    <FormKit
                    type="form"
                    id="registration-example"
                    :form-class="submitted ? 'hide' : 'show'"
                    submit-label="Register"
                    @submit="submitHandler"
                    :actions="false"
                    #default="{ value }"
                    >
                    <!-- <h2 class="text-2xl font-semibold mb-4 text-center text-white">LogIn</h2>  -->
                
                    <FormKit
                        type="email"
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
                
                    </FormKit>

                    <div class="flex flex-col mt-3">
                        <button class="w-full rounded-lg bg-teal-400 hover:translate-y-1 py-2 font-bold text-white shadow-sm mt-1 border-solid border-gray-500">Log in</button>
                        <div class="flex items-center justify-center mt-3">
                            <div class="border-t border-gray-400 border-s-2 flex-grow"></div>
                            <div class="mx-2 text-gray-300">or</div>
                            <div class="border-t border-gray-400 border-s-2 flex-grow"></div>
                        </div>
                        <a class="text-gray-300 text-center mt-1 hover:text-white hover:underline cursor-pointer" @click="createAccount"> create an account</a>
                    </div>
                
                </div>
                
                <div v-if="register">

                    <FormKit
                        type="email"
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
                            
                    <div class="double">
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
                        <FormKit
                            type="password"
                            name="password_confirm"
                            label="Confirm password"
                            placeholder="Confirm password"
                            validation="required|confirm"
                            :classes="{
                                outer: 'mb-2',
                                label: 'mb-1 font-bold text-base text-white',
                                inner: 'rounded-lg',
                                input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                                message: 'text-sm mt-1 text-red-900'
                            }"
                        />
                    </div>
                
            
                    <button class="w-full rounded-lg bg-teal-400 hover:bg-teal-500 py-2 font-bold text-white shadow-sm mt-4 border-solid border-gray-500">Register</button>   
                          
                </div>
            </div>
        </div>
    </div>
  
</template>


<script setup>
import IconFish from '~/assets/icons/fish_icon.svg'
const submitted = ref(false)
const register = ref(false)

const submitHandler = async () => {
  // Let's pretend this is an ajax request:
  await new Promise((r) => setTimeout(r, 1000))
  submitted.value = true
}

const createAccount = () => {
    console.log(register.value)
    register.value = true
}

</script>