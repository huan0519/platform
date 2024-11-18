import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home.vue'
import Login from '@/views/LoginView.vue'
import Register from '@/views/Register.vue'
import Personal_center from "@/views/Personal_center.vue"
import Cloud_platform from "@/views/Cloud_Platform.vue"
import Homepage from '@/views/homepage.vue'
import Help from '@/views/Help.vue'
import Applied from '@/views/Applied.vue'
import Data_normalization from '@/views/Data_normalization.vue'
import Data_preprocess from '@/views/Data_preprocess.vue'
import Data_visualization from "@/views/Data_visualization.vue"
import ai_analysis from '@/views/AI-analysis.vue'
import demo from "@/views/demo.vue";
import Prediction from "@/views/prediction.vue";

Vue.use(VueRouter)

const router = new VueRouter({
  mode: "history",
  routes:[
    {
      path: '/',
      name: 'home',
      component: Home,
      redirect: '/homepage',
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
          path: '/cloud_platform/',
          name: 'Cloud_platform',
          component: Cloud_platform,
          redirect: 'cloud_platform/data_visualization',
          children:[
            {
              path:'data_normalization',
              name:'data_normalization',
              component: Data_normalization
            },
            {
              path:'data_preprocess',
              name:'data_preprocess',
              component: Data_preprocess,
            },
            {
              path:'data_visualization',
              name:'data_visualization',
              component: Data_visualization
            },
            {
              path:'prediction',
              name:'prediction',
              component: Prediction
            },
            {
              path:'ai_analysis',
              name:'ai_analysis',
              component: ai_analysis
            }
          ]
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

    {
      path:'/demo',
      name:'demo',
      component:demo
    }
  ]
})

export default router
