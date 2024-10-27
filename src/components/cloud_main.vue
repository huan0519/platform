<template>
  <div id="app" class="cloud_body">
<!--    <component :is="currentPartComponent1"></component>-->
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>

<script>
import Data_visualization from "@/views/Data_visualization.vue";
import AI_analysis from "@/views/AI-analysis.vue";
import Data_preprocess from "@/views/Data_preprocess.vue";
import Vue_header from "@/components/vue_header.vue";

export default {
  components:{
    Vue_header,
    Data_visualization,
    AI_analysis,
    Data_preprocess
  },
  props:['currentPart'],
  computed:{
    //换页面
    currentPartComponent1(){
      const parts={
        'Data_visualization': Data_visualization,
        'AI_analysis': AI_analysis,
        'Data_preprocess': Data_preprocess
      };
      return  parts[this.currentPart] || 'div';//若是没对应到，显示空内容
    }
  }
}


</script>

<style scoped>
.cloud_body{
  background-color: darkgrey;
  width: 100vw;
  overflow-y: auto;
  height: 100vh;
}
</style>