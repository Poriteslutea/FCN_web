import { defineStore } from 'pinia'


export const useAsidePaneStore = defineStore({
    id: 'asidePane',
    state: () => ({
        isExpand: false,
        component: null
    }),
    actions: {
        selectComponent(component: any){
            this.isExpand = true
            this.component = component
        },
        close(){
            this.isExpand = false
        }
    }
})