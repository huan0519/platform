<!--云平台-->
<template>
  <div class="cloud_body">
      <Vue_aside  class="cloud-aside"></Vue_aside>
      <Cloud_main style="background-color: #E0F2FE;" class="cloud-main"/>
  </div>
</template>

<script>
import Vue_aside from "@/components/vue_aside.vue";
import Cloud_main from "@/components/cloud_main.vue";

export default {
  components: {
    Vue_aside,
    Cloud_main,
  },
  data() {
    return {
      //设置默认显示部分
      currentPart: 'Data_visualization',
    };
  },
  methods: {
    //从vue_aside中获取的页面赋值给currentPart
    handleNavigation1(page) {
      this.currentPart = page;
    }
  }
}
</script>

<style scoped>
.cloud_body{
  background-color: #E0F2FE;
  width: 100vw;
  overflow-y: hidden;
  height: 100px;
  display: flex;
}
.cloud-aside{
  position: sticky;
  height: 100vh;
}
.cloud-main{
  flex-grow: 1;
  overflow-y: auto;
  height: 100vh;
}
</style>