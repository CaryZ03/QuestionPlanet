import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin:false
  },
  getters: {
  },
  
  actions: {
    login(context){
      console.log('1')
      context.commit('LOGIN')
    }
  },
  mutations: {
    LOGIN(){
      console.log('2')
      this.state.isLogin=true
    }
  },
  modules: {
  }
})
