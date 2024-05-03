
<template>
    

<div class="bg-gradient-to-br from-slate-100 to-slate-300 min-h-screen">
    <HeadMenu></HeadMenu>

    <div class="relative left-0">
        <slot />

    </div>
    
</div>

</template>

<script setup lang="ts">

import HeadMenu from '~/components/HeadMenu.vue'


  

</script>