
<template>

<StockReport></StockReport>

  

 
</template>

<script setup lang="ts">

import StockReport from '~/components/StockReport.vue'

definePageMeta({
  middleware: ["auth"]
})





</script>