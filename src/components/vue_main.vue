<template>
    <div class="main_body">
      <component :is="currentPageComponent"> </component>
    </div>
</template>

<style>
.main_body {
    overflow-y: auto; /* 如果内容超出屏幕高度，显示滚动条 */
  }
</style>

<script>
import Homepage from "@/views/homepage.vue";
import Cloud_platform from "@/views/cloud_platform.vue";
import Help from "@/views/Help.vue";
import Applied from "@/views/Applied.vue";

export default {
  components:{
    Homepage,
    Cloud_platform,
    Help,
    Applied
  },
  props:['currentPage'],
  computed:{
    //实现动态切换页面
    currentPageComponent(){
      const pages = {
        'Homepage': Homepage,
        'Cloud_platform': Cloud_platform,
        'Help': Help,
        'Applied': Applied
      };
      return pages[this.currentPage] || 'div';
    }
  }
}
</script>
