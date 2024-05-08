
<template>
    


    <HeadMenu></HeadMenu>
    <div class="fixed h-screen top-0 left-20 overflow-y-auto transition bg-slate-100"
    :class="{'translate-x-80': isExpand, 'translate-x-0': !isExpand}"
    :style="isExpand ? {'width': 'calc(100vw - 400px)'} : {'width':'calc(100vw - 80px)'}">
    
        <ClientOnly>
            <slot />
        </ClientOnly>
    </div>

 
   
    
   

    <ModalsContainer />
    


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