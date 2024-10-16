<template>
  <el-container>
<!--    设置监听事件实现页面跳转-->
    <Vue_aside @navigate1="handleNavigation1"></Vue_aside>
    <Cloud_main :current-part="currentPart"></Cloud_main>
  </el-container>
</template>

<script>
import Vue_aside from "@/components/vue_aside.vue";
import Cloud_main from "@/components/cloud_main.vue";

export default{
  components:{
    Vue_aside,
    Cloud_main
  },
  data(){
    return{
      //设置默认显示部分
      currentPart:'Data_visualization',
    };
  },
  methods:{
    //从vue_aside中获取的页面赋值给currentPart
    handleNavigation1(page) {
      this.currentPart = page;
    }
  }
}
</script>

<style scoped>
.cloud{
  display: inline-block;
}

</style>