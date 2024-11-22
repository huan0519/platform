<template>
  <div id="app" class="cloud_body">
    <!--    设置监听事件实现页面跳转-->
    <div class="cloud_pf">
      <div class="cloud-aside">
        <Vue_aside></Vue_aside>
      </div>
      <Cloud_main style="background-color: #E0F2FE;" class="cloud-main"/>
    </div>
  </div>
</template>

<script>
import Vue_header from "@/components/vue_header.vue";
import Vue_aside from "@/components/vue_aside.vue";
import Cloud_main from "@/components/cloud_main.vue";

export default {
  components: {
    Vue_aside,
    Cloud_main,
    Vue_header,
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
.cloud_pf {
  display: flex;
}
.cloud_body{
  background-color: #E0F2FE;
  width: 100vw;
  overflow-y: hidden;
  height: 100px;
}
.cloud-aside{
  position: sticky;
  height: 100vh;
}
.cloud-main{
  min-height: 100vh;
  overflow: auto;
  padding: 20px;
  height: calc(100vh - 20px);
}
</style>