const baseUrl = `${import.meta.env.NUXT_PUBLIC_API_BASE_URL}`;


export const useTokenStore = defineStore({
  id: 'token',
  state: () => ({
    userToken:useCookie('token')
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
      },
  }
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