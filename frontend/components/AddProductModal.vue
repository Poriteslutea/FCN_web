<template>
    <VueFinalModal
      class="flex justify-center items-center"
      content-class="flex flex-col w-96 mx-4 p-4 bg-white bg-gradient-to-br from-blue-950 to-teal-400 bg-teal-400
       rounded-lg space-y-2"
    >
      <h1 class="text-xl text-white text-center">
        新增產品
      </h1>
      <div class="mx-4">
        <FormKit
            type="form"
            id="add-product"
            font-class="w-full"
            @submit="addProduct"
            :actions="false"
            :disabled="pending"
            #default="{ value }"
            >       
            <FormKit
                type="text"
                name="code"
                label="產品編號"
                validation="required"
                placeholder="請輸入產品編號"
                :classes="{
                    outer: 'mb-2',
                    label: 'mb-1 text-base text-white',
                    inner: 'rounded-lg',
                    input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                    message: 'text-sm mt-1 text-red-900'
                }"
                />
                        
            <FormKit
                type="date"
                name="start_date"
                validation="required"
                label="起始日期(交易日)"
                placeholder="請輸入起始交易日"
                :classes="{
                    outer: 'mb-2',
                    label: 'mb-1 text-base text-white',
                    inner: 'rounded-lg',
                    input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                    message: 'text-sm mt-1 text-red-900'
                }"
            />

            <FormKit
                type="date"
                name="start_trace_date"
                validation="required"
                label="觀察日"
                placeholder="請輸入觀察日"
                :classes="{
                    outer: 'mb-2',
                    label: 'mb-1 text-base text-white',
                    inner: 'rounded-lg',
                    input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                    message: 'text-sm mt-1 text-red-900'
                }"
            />

            <FormKit
                type="date"
                name="end_date"
                validation="required"
                label="結束日"
                placeholder="請輸入產品結束日"
                :classes="{
                    outer: 'mb-2',
                    label: 'mb-1 text-base text-white',
                    inner: 'rounded-lg',
                    input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                    message: 'text-sm mt-1 text-red-900'
                }"
            />

            <FormKit
                type="number"
                name="ko_limit"
                validation="required"
                label="上限價"
                placeholder="請輸入上限價比例，範圍1~100 ex.100"
                :classes="{
                    outer: 'mb-2',
                    label: 'mb-1 text-base text-white',
                    inner: 'rounded-lg',
                    input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                    message: 'text-sm mt-1 text-red-900'
                }"
            />

            <FormKit
                type="number"
                name="ki_limit"
                validation="required"
                label="下限價"
                placeholder="請輸入下限價比例，範圍1~100 ex.60"
                :classes="{
                    outer: 'mb-2',
                    label: 'mb-1 text-base text-white',
                    inner: 'rounded-lg',
                    input: 'w-full text-sm appearance-none border-none focus:outline-none focus:bg-transparent bg-transparent',
                    message: 'text-sm mt-1 text-red-900'
                }"
            />
            
            <FormKit
                type="checkbox"
                name="stocks"
                label="股票代碼"
                :options="stocks"
                :classes="{
                    legend: 'text-white',
                    outer: 'mb-2',
                    label: 'mb-1 text-base text-white',
                    inner: 'rounded-lg',
                    message: 'text-sm mt-1 text-red-900',
                    options: 'grid grid-cols-3 gap-0 h-[120px] overflow-y-scroll mt-2'
                }"
            />

            <p class="text-sm text-red-400">{{ submitText }}</p>

            <div class="flex flex-row text-sm gap-2 justify-end items-center">
                <div class="mt-1 px-5 bg-teal-300 text-gray-800 py-1 hover:bg-teal-200 rounded-lg cursor-pointer" @click="emit('confirm')">
                    取消
                </div>
                <button :disabled="isSubmit" class="mt-1 px-5 bg-teal-300 text-gray-800 py-1 hover:bg-teal-200 rounded-lg">
                    確認
                </button>
            </div>

            

        </FormKit>  

      </div>
      
      
    </VueFinalModal>
  </template>

<script setup lang="ts">
import { VueFinalModal } from 'vue-final-modal'
import { stocksList } from 'assets/static_data'
const stocks = ref()
stocks.value = stocksList


defineProps<{
title?: string
}>()

const emit = defineEmits<{
(e: 'confirm'): void
}>()

const pending = ref(false)
const isSubmit = ref(false)
const submitText = ref('')
const productListStore = useProductListStore()

const addProduct = async (formData: any) => {
    pending.value = true
    formData.ki_limit = formData.ki_limit / 100
    formData.ko_limit = formData.ko_limit / 100


    const {data:apiData, error:apiError, refresh} = await useAPI('/product/create', 
            {method: 'POST', body: JSON.stringify(formData)})
    if (apiError.value) {
        submitText.value = '系統異常：產品新增失敗！'
        console.log(apiError.value)
    }
    if (apiData.value) {
        submitText.value = '產品已成功新增'
        console.log(typeof(formData))
        console.log(formData)
        const addItem = formData
        console.log(addItem)
        productListStore.list.push(addItem)
        console.log(productListStore.list)
        pending.value = false
        isSubmit.value = true
    }

    setTimeout(()=>{
        emit('confirm')
    }, 1000)

}



</script>