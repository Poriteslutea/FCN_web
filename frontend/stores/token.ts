import { defineStore } from 'pinia'


export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    userToken: useCookie('token'),
    isLoggedIn: false,
    member: null
  }),
  getters: {
      getUserToken: state => {
          return state.userToken
      }
  },
  actions: {
      storeToken(token: string){
          this.userToken = token
          const newCookie = useCookie('token', {
              maxAge: 60*24*28,
              sameSite: true,
              secure: true,
          })
          newCookie.value = this.userToken
          this.isLoggedIn = true
        },

      removeToken(){
        this.userToken = null
        this.isLoggedIn = false
        this.member = null
      },

      async getMember(){
        const config = useRuntimeConfig()
        const response = await fetch(`${config.public.apiBaseUrl}/member/me`, {
            method: 'GET',
            headers: {
            'Authorization': `Bearer ${this.userToken}`
            },
        })
        if (response.ok) {
            const data = await response.json()
            this.member = data
        } 
      }
  },
  persist: true
})

// export const useAuthStore = defineStore({
//     id: 'auth',
//     state: () => ({
//       /* Initialize state from local storage to enable user to stay logged in */
//       user: JSON.parse(localStorage.getItem('user')),
//       token: JSON.parse(localStorage.getItem('token')),
//     }),
//     actions: {
//       async login(loginForm) {
//         await $fetch(`${baseUrl}/member/login`, {
//           method: 'POST',
//           headers: {
//             'Content-Type': 'application/x-www-form-urlencoded',
//           },
//           body: loginForm
//         })
//           .then(response => {
//             /* Update Pinia state */
//             this.user = response.json().email
//             this.token = response.json().access_token
//             /* Store user in local storage to keep them logged in between page refreshes */
//             localStorage.setItem('user', JSON.stringify(this.user))
//             localStorage.setItem('token', JSON.stringify(this.token))
//           })
//           .catch(error => { throw error })
//       },
//       logout() {
//         this.user = null
//         this.token = null
//         localStorage.removeItem('user')
//         localStorage.removeItem('token')
//       }
//     }
//   })