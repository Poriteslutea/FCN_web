<template>
    <div class="container p-5 w-full ">
        <div class="flex flex-col items-center justify-center text-lg text-center">
            <p class="py-2"> 追蹤產品</p>
            <hr class="border-gray-600 border-2 w-full my-2"/>
            <button v-for="item in productList"
                class="py-2  w-full hover:bg-slate-200"
                :class="{'bg-teal-100': selectedProductStore.code === item.code, '': selectedProductStore.code !== item.code}"
                @click="selectProduct(item)">
                {{ item?.code }}
            </button>

            
            <button class="mt-4 py-2 bg-teal-400 hover:bg-teal-300 w-full rounded-lg ">
                新增產品
            </button>

        </div>
        
    </div>


</template>

<script setup lang="ts">
const productList = ref()
const selectedProductStore = useSelectedProductStore()


const selectProduct = async function(item:any) {
    selectedProductStore.code = item.code
    selectedProductStore.start_date = item.start_date
    selectedProductStore.end_date = item.end_date
    selectedProductStore.start_trace_date = item.start_trace_date
    selectedProductStore.ko = item.ko_limit
    selectedProductStore.ki = item.ki_limit
    selectedProductStore.report = await getReport(item.code)
}



const getProduct = async function() {
    const {data, error, refresh} = await useAPI('/product/all', {method: 'GET'})
    if (error.value) {
        console.log(error.value)
        productList.value = []
    }
    if (data.value) {
        productList.value = data.value
        selectProduct(productList.value[0])
    }
}

const getReport = async function(productCode: any){
    const {data, error} = await useAPI(`/report/latest/${productCode}`, {method: 'GET'})
    if (error.value) {
        console.log(error.value)
        return []
    }
    if (data.value) {
        return data.value
    }
}

await getProduct()



</script>





