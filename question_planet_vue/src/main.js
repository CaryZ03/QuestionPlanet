import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import api from './api';
import Cookies from 'js-cookie'

const token = Cookies.get('token')
axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
axios.defaults.withCredentials = true;

Vue.prototype.$api = api;


Vue.use(ElementUI);
// Vue.use(ViewUIPlus);

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
