<template>
   
    <div v-if="code" 
        class="flex flex-row">
       
        <div class="h-full p-16 container mx-8">
            <div class="container mx-auto p-8 rounded-lg">
                <div class="container flex mx-auto my-6 justify-center md:justify-between">
                    <div class="flex flex-col gap-3 px-5 ">
                        <div class="text-4xl font-bold">{{ code }}</div>
                        <div class="grid md:grid-cols-3 gap-2 ">
                            <div class="text-xl">交易日：{{ start_date }}</div>
                            <div class="text-xl">觀察日：{{ start_trace_date }}</div>
                            <div class="text-xl">結束日：{{ end_date }}</div>
                            <div class="text-xl">上限價：{{ ko * 100 }}%</div>
                            <div class="text-xl">下限價：{{ ki * 100 }}%</div>
                        </div>
                    </div>
                </div>

                <div class="container flex mx-auto pb-8">
                    <div class="grid 2xl:grid-cols-4 xl:grid-cols-3 lg:grid-cols-2 md:grid-cols-1 gap-8 p-2 w-full justify-center ">
                        <div v-for="rp in report" 
                        class="rounded-lg flex flex-col justify-center p-10 shadow-slate-600 shadow-xl bg-slate-50">

                            <div class="text-xl mt-2">{{ rp.date }}</div>
                            <div class="flex flex-row gap-4 items-center justify-between">
                                <div class="text-3xl">{{ rp.stock }}</div>
                                <div class="flex flex-col">
                                <div class="text-lg">今日收盤價</div>
                                <div class="font-bold text-4xl">{{ rp.close }}</div>
                                </div>
                            </div>
                            
                            <div class="text-lg mt-2">上限價格</div>
                            <div class="flex flex-row gap-2 items-center">
                                <div class="font-bold text-3xl">{{ rp.ko_base }} </div>
                                <span v-if="rp.is_ko" 
                                class="bg-red-500 px-2 rounded-lg font-bold text-xl">已KO
                                </span>
                                <div v-else :class="['font-bold text-2xl flex flex-row items-center',
                                                    {'text-green-500': rp.ko_diff < 0},
                                                    {'text-red-500': rp.ko_diff > 0}]"> 
                                                    
                                <IconArrow :class="['h-5 w-5 mx-1',
                                                    {'rotate-180': rp.ko_diff > 0}, 
                                                    {'opacity-0': rp.ko_diff === 0}]"></IconArrow>
                                {{ rp.ko_diff }}%
                                </div>
                            </div>

                            <div class="text-lg mt-2">下限價格</div>
                            <div class="flex flex-row gap-2 items-center">
                                <div class="font-bold text-3xl">{{ rp.ki_base }} </div>
                                <span v-if="rp.is_ki" 
                                class="bg-red-500 px-2 rounded-lg font-bold">已KI
                                </span>
                                <div v-else :class="['font-bold text-2xl flex flex-row items-center',
                                                    {'text-green-500': rp.ki_diff < 0},
                                                    {'text-red-500': rp.ki_diff > 0}]"> 
                                                    
                                <IconArrow :class="['h-5 w-5 mx-1',
                                                    {'rotate-180': rp.ki_diff > 0}, 
                                                    {'opacity-0': rp.ki_diff === 0}]"></IconArrow>
                                {{ rp.ki_diff }}%
                                </div>
                            </div>
                            
                        </div>

                    </div>
                </div>

            </div>
            

        </div>
        

    </div>
    
</template>

<script setup>
import IconArrow from '~/assets/icons/arrow-down-solid.svg'

const selectedProductStore = useSelectedProductStore()
const { code, start_date, start_trace_date, end_date, ki, ko, report } = storeToRefs(selectedProductStore)




</script>