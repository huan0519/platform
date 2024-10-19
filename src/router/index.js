import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/LoginView.vue'
import Register from '@/views/Register.vue'
import Personal_center from "@/views/Personal_center.vue";
import Cloud_platform from "@/views/Cloud_Platform.vue";
import Homepage from '@/views/homepage.vue';
import Help from '@/views/Help.vue';
import Applied from '@/views/Applied.vue';

Vue.use(VueRouter)

const router = new VueRouter({
  mode: "history",
  routes:[
    {
      path: '/',
      name: 'home',
      component: Home,
      children:[
        {
          path:'/homepage',
          name:'Homepage',
          component: Homepage
        },
        {
          path: '/personal_center',
          name: 'Personal_center',
          component: Personal_center
        },
        {
          path: '/cloud_platform',
          name: 'Cloud_platform',
          component: Cloud_platform
        },
        {
          path:'/help',
          name:'Help',
          component: Help
        },
        {
          path:'/applied',
          name:'Applied',
          component: Applied
        }
      ]
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

  ]
})

export default router
