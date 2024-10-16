import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/LoginView.vue'
import Register from '@/views/Register.vue'
import Personal_center from "@/views/Personal_center.vue";
import Cloud_platform from "@/views/Cloud_Platform.vue";

Vue.use(VueRouter)

const router = new VueRouter({
  mode: "history",
  routes:[
    {
      path: '/',
      name: 'home',
      component: Home
    },

    {
      path:'/login',
      name:'Login',
      component: Login
    },

    {
      path:'/register',
      name:'Register',
      component: Register
    },

    {
      path: '/personal_center',
      name: 'Personal_center',
      component: Personal_center
    },

    {
      path: '/cloud_platform',
      name: 'Cloudform',
      component: Cloud_platform
    },
  ]
})

export default router
