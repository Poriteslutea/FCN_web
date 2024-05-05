import { defineStore } from 'pinia'


export const useSelectedProductStore = defineStore({
    id: 'selectedProduct',
    state: () => ({
        code: '',
        start_date: '',
        end_date: '',
        start_trace_date: '',
        ko: null,
        ki: null,
        report: {} || undefined
    })
})