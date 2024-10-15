<template>
    <div class="header">
    <el-menu :default-active="activeIndex" class="el-menu" mode="horizontal">
        <el-menu-item @click="GoToPage('Homepage')" class="el-menu-item" index="1">首页</el-menu-item>
        <el-menu-item @click="GoToPage('Cloud_platform')" class="el-menu-item" index="2">云平台</el-menu-item>
        <el-menu-item @click="GoToPage('Help')" style="width: 100px" index="3">使用教程</el-menu-item>
        <el-menu-item @click="GoToPage('Applied')" style="width: 100px" index="4">应用统计</el-menu-item>
      <div style="margin-left: 20px;margin-right: 20px">
        <userinfo></userinfo>
      </div>
    </el-menu>
         
    </div>

</template>

<script>
import ElementUI from 'element-ui';
import Vue from 'vue';
import userinfo from "@/components/userinfo.vue";


Vue.component(ElementUI);

export default{
  components:{
    userinfo
  },
    data() {
      return {
        activeIndex: '1'
      };
    },
    methods: {
      GoToPage(page)  {
        this.$emit('navigate',page);
      }
    }

}
</script>

<style scoped>
.el-menu-item:hover {
  background-color: #000000; /* 悬停时的背景颜色 */
  color: #f6f5f5; /* 悬停时的文字颜色 */
}
.el-menu{
    float: right;
    height: 100%;
    display: flex;
    align-items: center; /* 垂直居中子元素 */
    justify-content: space-between;
    background-color: #66FFFF;
}
.el-menu-item.is-active {
  position: relative; /* 为底部边框定位 */
}
.el-menu-item.is-active::after {
  content: ''; /* 伪元素内容 */
  display: block; /* 使其占据空间 */
  position: absolute; /* 绝对定位 */
  bottom: 0; /* 底部对齐 */
  left: 0; /* 左侧对齐 */
  width: 100%; /* 宽度100% */
  height: 1px; /* 蓝线高度 */
  background-color: rgb(255, 255, 255);
}
.header{
    height: 60px;
    width: 100%;
    background-color: #66FFFF;
}
.el-menu.el-menu--horizontal {
  height: 100%; /* 或者与 header 相同的高度 */
}
.link{
    font-size: large;
    float: right;
    margin-top: 10px;
    color: rgb(141, 166, 158);
    
}
.el-menu-item{
    height: 100vh;
    width: 90px;
    margin-bottom: 0;
    font-size: medium;
    text-align: center;
}


</style>
