<template>
    <div class="header">
    <el-menu :default-active="activeIndex" class="el-menu" mode="horizontal">
      <el-menu-item @click="GoToPage('homepage')" class="el-menu-item" index="1">首页</el-menu-item>
        <el-menu-item @click="GoToPage('Cloud_platform')" class="el-menu-item" index="2">云平台</el-menu-item>
        <el-menu-item @click="GoToPage('Help')" style="width: 100px" index="3">使用教程</el-menu-item>
        <el-menu-item @click="GoToPage('Applied')" style="width: 100px" index="4">应用统计</el-menu-item>
      <div style="margin-left: 20px;margin-right: 20px">
        <userinfo @ChangePage="GoToPage('Personal_center')"></userinfo>
      </div>
    </el-menu>
         
    </div>

</template>

<script>
import ElementUI from 'element-ui';
import Vue from 'vue';
import userinfo from "@/components/userinfo.vue";

Vue.use(ElementUI);

export default{
    components:{
      userinfo,
    },
    watch: {
      '$route' (to, from) {
        this.setActiveIndex(to);
      },
    },
    data() {
      return {
        //默认
        activeIndex: '',
        page: ''
      };
    },
    methods: {
    //点击事件，通过emit告知父组件要跳转的界面
      GoToPage(page)  {
        this.$router.push(page).catch(err => err);
      },
      setActiveIndex(route){
        const routes = {
          'homepage': '1',
          'Cloud_platform': '2',
          'Help': '3',
          'Applied': '4',
          'Personal_center': '5',
        };
        this.activeIndex = routes[route.name] || '1';
      }
    },
  created() {
    this.setActiveIndex(this.$route);
  },

}
</script>

<style scoped>
.el-menu-item:hover {
  background-color: #000000; /* 悬停时的背景颜色 */
  color: #f6f5f5; /* 悬停时的文字颜色 */
}
.el-menu{
    float: right;
    height: 60px;
    display: flex;
    align-items: center; /* 垂直居中子元素 */
    justify-content: space-between;
    background-color: #66FFFF;
}
.el-menu-item.is-active {
  position: relative; /* 为底部边框定位 */
}

.header{
  width: 100%;
  background-color: #66FFFF;
  z-index: 1000;
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
    min-width: 90px; /* Use min-width instead of width */
    margin-bottom: 0;
    font-size: medium;
    text-align: center;
}


</style>
