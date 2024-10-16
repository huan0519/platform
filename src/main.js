import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueRouter from 'vue-router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VueParticles from '@tsparticles/vue2';

Vue.config.productionTip = false

Vue.use(VueRouter);

Vue.use(ElementUI);

Vue.use(VueParticles);

// export default new VueRouter({
//   routes: [
//     {
//       path: '/',
//       name: 'Home',
//       component: Home
//     },
//   ]
// });

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')//全局注册