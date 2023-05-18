import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

// import ViewUIPlus from 'view-ui-plus';
// import 'view-ui-plus/dist/styles/viewuiplus.css';
Vue.use(ElementUI);
// Vue.use(ViewUIPlus);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
