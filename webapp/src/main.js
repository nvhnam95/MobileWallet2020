import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router'
import router from './routers'
import 'beautify-scrollbar/dist/index.css';
import 'v2-table/dist/index.css'; 
import V2Table from 'v2-table';

Vue.use(V2Table)
Vue.use(VueRouter)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

new Vue({router,
  render: h => h(App),
}).$mount('#app')

