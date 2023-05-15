import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin:false,
    curUserID:''
  },
  getters: {
  },
  
  actions: {
    login(context,id){
      console.log('1')
      context.commit('LOGIN',id)
    }
  },
  mutations: {
    LOGIN(state,id){
      console.log('2'),
      this.state.isLogin=true,
      this.state.curUserID=id,
      console.log(this.state.curUserID)
    }
  },
  modules: {
  }
})
