import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    curUserID: '',
    curUsername: '',
    my_naire_num: 0,
    my_bin_num: 0,
    is_creating: false,
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
