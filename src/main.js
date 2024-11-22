import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import store from "@/store";
import echarts from 'echarts'
import VueParticles from "vue2-particles";

Vue.prototype.$echarts = echarts;

Vue.config.productionTip = false;

Vue.use(VueRouter);

Vue.use(ElementUI);

Vue.use(VueParticles);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')//全局注册