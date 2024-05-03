<template>


    
   
    <div class="flex flex-row">
        <div class="h-screen bg-slate-300 w-80 rounded-tr-lg rounded-br-lg">
            dsfdf

        </div>
        <div class="h-screen slate-200 p-16 container mx-auto">
            <div class="container mx-auto bg-white p-8 rounded-lg">
                <div class="container flex mx-auto my-6 justify-center md:justify-between">
                    <div class="flex flex-col gap-3 px-5 ">
                        <div class="text-4xl font-bold">SLN35</div>
                        <div class="grid md:grid-cols-3 gap-2 ">
                            <div class="text-xl">交易日：2023-12-21</div>
                            <div class="text-xl">觀察日：2024-01-29</div>
                            <div class="text-xl">結束日：2024-07-01</div>
                            <div class="text-xl">上限價：100%</div>
                            <div class="text-xl">下限價：60%</div>
                        </div>
                    </div>
                </div>

                <div class="container flex mx-auto pb-8">
                    <div class="grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 gap-8 p-2 w-full justify-center ">
                        <div v-for="rp in report" 
                        class="rounded-lg flex flex-col justify-center p-10 shadow-slate-600 shadow-xl bg-slate-100">

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

const report = ref()


const getReport = async function(product) {
  const {data, error} = await useAPI(`/report/latest/${product}`, {method: 'GET'})
  if (data) {
    report.value = data.value
    console.log(data.value);
  }
}

getReport('SLN35')

</script>