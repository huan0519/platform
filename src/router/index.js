import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home.vue'
import Login from '@/views/LoginView.vue'
import Register from '@/views/Register.vue'
import Personal_center from "@/views/Personal_center.vue"
import Cloud_platform from "@/views/cloud_platform.vue"
import Homepage from "@/views/homepage.vue"
import Help from "@/views/Help.vue"
import Data_normalization from "@/views/Data_normalization.vue"
import Data_preprocess from "@/views/Data_preprocess.vue"
import Data_visualization from "@/views/Data_visualization.vue"
import ai_analysis from "@/views/AI-analysis.vue"
import demo from "@/views/demo.vue";
import Prediction from "@/views/prediction.vue";
import Demo1 from "@/views/demo1.vue";
import StackedBarChart from "@/views/Stacked-Bar-Chart.vue";
import StackedLine from "@/views/Stacked-Line.vue";
import Rose from "@/views/Rose.vue";
import ScatterDiagram from "@/views/Scatter-Diagram.vue";
import MichelsonMorleyExperiment from "@/views/Michelson-Morley-Experiment.vue";
import HMichelsonMorleyExperiment from "@/views/H-Michelson-Morley-Experiment.vue";
import LargeAreaChart from "@/views/Large-Area-Chart.vue";
import DashedBarChart from "@/views/Dashed-Bar-Chart.vue";
import three_D from "@/views/3D.vue";
import ThermodynamicDiagram from "@/views/Thermodynamic-Diagram.vue";
import Reinforce from "@/views/reinforce.vue";
import Alignment from "@/views/alignment.vue";
import Data_enhancement from "@/views/Data_enhancement.vue";
import file_Download from "@/views/file-Download.vue"
import alignment_info_file from "@/views/info/alignment_info_file.vue";
import normalization_file from "@/views/file/normalization_file.vue";
import reinforce_file from "@/views/file/reinforce_file.vue";
import file_sum from "@/views/file/file_sum.vue";
import alignment_file from "@/views/file/alignment_file.vue";
import file_info_sum from "@/views/info/file_info_sum.vue";
import normalization_info_file from "@/views/info/normalization_info_file.vue";
import reinforce_info_file from "@/views/info/reinforce_info_file.vue";
import result_file from "@/views/file/result_file.vue";
import dimension_file from "@/views/file/dimension_file.vue";
import store from "@/store";

Vue.use(VueRouter)


const router = new VueRouter({
  mode: "history",
  routes:[
    {
      path: '/',
      name: 'home',
      component: Home,
      redirect: '/cloud_platform',
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
              path:'reinforce',
              name:'reinforce',
              component: Reinforce
            },
            {
              path:'alignment',
              name:'alignment',
              component: Alignment
            },
            {
              path:'data_enhancement',
              name:'data_enhancement',
              component: Data_enhancement
            },
            {
              path:'stacked_line',
              name:'stacked_line',
              component: StackedLine
            },
            {
              path:'stacked_barchart',
              name:'stacked_barchart',
              component: StackedBarChart
            },
            {
              path:'rose',
              name:'rose',
              component: Rose
            },
            {
              path:'scatter_diagram',
              name:'scatter_diagram',
              component: ScatterDiagram
            },
            {
              path:'michelson',
              name:'michelson',
              component: MichelsonMorleyExperiment
            },
            {
              path:'H_michelson',
              name:'H_michelson',
              component: HMichelsonMorleyExperiment
            },
            {
              path:'large-area-chart',
              name:'large-area-chart',
              component: LargeAreaChart
            },
            {
              path:'thermodynamic',
              name:'thermodynamic',
              component: ThermodynamicDiagram
            },
            {
              path:'dashed-bar-chart',
              name:'dashed-bar-chart',
              component: DashedBarChart
            },
            {
              path:'3D',
              name:'3D',
              component: three_D
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
          ]
        },
        {
          path:'/help',
          name:'Help',
          component: Help
        },
        {
          path:'/ai_analysis',
          name:'ai_analysis',
          component: ai_analysis
        },
        {
          path:'/file_download',
          name:'文件',
          component: file_Download,
          children:[
            {
              path:'file_sum',
              name:'数据总览',
              component: file_sum,
            },
            {
              path:'file_info_sum',
              name:'数据信息总览',
              component: file_info_sum,
            },
            {
              path:'normalization_info_file',
              name:'归一化信息',
              component: normalization_info_file,
            },
            {
              path:'reinforce_info_file',
              name:'补值后信息',
              component: reinforce_info_file,
            },
            {
              path:'alignment_info_file',
              name:'对齐后信息',
              component: alignment_info_file,
            },
            {
              path:'normalization_file',
              name:'归一化数据',
              component: normalization_file,
            },
            {
              path:'reinforce_file',
              name:'补值后数据',
              component: reinforce_file,
            },
            {
              path:'alignment_file',
              name:'对齐后数据',
              component: alignment_file,
            },
            {
              path:'dimension_file',
              name:'降维后数据',
              component: dimension_file,
            },
            {
              path:'result_file',
              name:'训练结果数据',
              component: result_file,
            },
          ]
        },
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
    },

    {
      path:'/demo1',
      name:'demo1',
      component:Demo1
    }
  ]
})

// 路由守卫
router.beforeEach((to, from, next) => {
  localStorage.setItem('currentPathName', to.name)
  store.commit('setPath')
  next()
})

export default router
