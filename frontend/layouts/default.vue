
<template>
    

<div class="bg-gradient-to-br from-slate-100 to-slate-300 min-h-screen">
    <HeadMenu></HeadMenu>

    <div class="flex flex-row h-screen bg-slate-200">
        <div class="bg-back w-20 h-screen">
        </div>
        <div class="h-full bg-slate-300 w-80 rounded-tr-lg rounded-br-lg">
            <component :is="selectedPane"></component>
        </div>
        

        <ClientOnly>
            <slot />
        </ClientOnly>
        

    </div>
    
</div>

</template>

<script setup lang="ts">


import HeadMenu from '~/components/HeadMenu.vue'
import ProductPane from '~/components/ProductPane.vue'

const asidePaneStore = useAsidePaneStore()
const isAsideExpand = ref(false)
const selectedPane = shallowRef()
selectedPane.value = ProductPane
isAsideExpand.value = asidePaneStore.isExpand

  

</script>