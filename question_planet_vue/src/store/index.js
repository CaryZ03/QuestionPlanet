import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    curUserID: -1,
    curUsername: '',
    my_naire_num: 0,
    my_bin_num: 0,
    is_creating: false,
    token_key: ''
  },
  getters: {
  },

  actions: {

  },
  mutations: {

  },
  modules: {
  }
})
