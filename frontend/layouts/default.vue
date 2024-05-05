
<template>
    

<div class="bg-gradient-to-br from-slate-100 to-slate-300 min-h-screen">
    <HeadMenu></HeadMenu>

    <div class="flex flex-row h-screen bg-slate-100">
        <div class="bg-back w-20 h-screen">
        </div>
        <div class="h-full bg-slate-300 min-w-80  rounded-tr-lg rounded-br-lg transition"
        :class="{'tanslate-x-0': !isExpand, '-translate-x-full': isExpand}">
            <component :is="selectedPane"></component>
        </div>

        <div :class="{'tanslate-x-0 transition': !isExpand, '-translate-x-80 transition': isExpand}">
            <ClientOnly>
                <slot />
            </ClientOnly>
        </div>
        
      

        <ModalsContainer />
        

    </div>
    
</div>

</template>

<script setup lang="ts">


import HeadMenu from '~/components/HeadMenu.vue'
import ProductPane from '~/components/ProductPane.vue'
import { ModalsContainer } from 'vue-final-modal'


const asidePaneStore = useAsidePaneStore()
const { isExpand } = storeToRefs(asidePaneStore)
const selectedPane = shallowRef()
selectedPane.value = ProductPane


  

</script>