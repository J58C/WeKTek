import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      token: '',
      isAuthenticated: false
    }
  },
  mutations: {
    initializeStore(state) {
      state.user.token = ''
      state.user.isAuthenticated = false
    },
    setToken(state, token) {
      state.user.token = token
      state.user.isAuthenticated = true
    },
    removeToken(state) {
      state.user.token = ''
      state.user.isAuthenticated = false
    }
  },
  actions: {
    setToken({ commit }, token) {
      commit('setToken', token)
      localStorage.setItem('token', token)
    },
    removeToken({ commit }) {
      commit('removeToken')
      localStorage.removeItem('token')
    }
  },
  modules: {
  }
})
