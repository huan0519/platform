<template>
  <div id="app" class="cloud_body">
    <component :is="currentPartComponent1"></component>
  </div>
</template>

<script>
import Data_visualization from "@/views/Data_visualization.vue";
import AI_analysis from "@/views/AI-analysis.vue";

export default {
  components:{
    Data_visualization,
    AI_analysis,
  },
  props:['currentPart'],
  computed:{
    //换页面
    currentPartComponent1(){
      const parts={
        'Data_visualization': Data_visualization,
        'AI_analysis': AI_analysis,
      };
      return  parts[this.currentPart] || 'div';//若是没对应到，显示空内容
    }
  }
}


</script>

<style scoped>
.cloud_body{
  background-color: darkgrey;
  width: 100%;
}
</style>