<template>
    <div class="header">
      <img src="../../public/image/logo.png" style="height: 60px;float: left">

    <el-menu :default-active="activeIndex" class="el-menu" mode="horizontal">
      <p class="header_line"></p>
        <el-menu-item class="el-menu-item" index="homepage" @click="navigate('homepage','1')">首页</el-menu-item><p class="header_line"></p>
        <el-menu-item class="el-menu-item" index="cloud_platform" @click="navigate('cloud_platform')">云平台</el-menu-item><p class="header_line"></p>
        <el-menu-item style="width: 130px" index="help" @click="navigate('help')">使用教程</el-menu-item><p class="header_line"></p>
        <el-menu-item style="" index="applied" @click="navigate('applied')">应用统计</el-menu-item><p class="header_line"></p>
      <div style="margin-left: 20px;margin-right: 20px">
        <userinfo @ChangePage="GoToPage('Personal_center')"></userinfo>
      </div>
    </el-menu>

    </div>

</template>

<script>
import ElementUI from 'element-ui';
import {mapState,mapActions} from "vuex";
import Vue from 'vue';
import userinfo from "@/components/userinfo.vue";

Vue.use(ElementUI);

export default{
    components:{
      userinfo,
    },
  computed:{
    ...mapState(['activeIndex']),
  },
    watch: {
      $route(to) {
        this.syncActiveIndex(to); // 路由变化时同步导航状态
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
      ...mapActions(['updateActiveIndex']), // 调用 Vuex 的 actions
      navigate(page, index) {
        this.updateActiveIndex(index); // 更新激活状态
        this.$router.push('/' + page).catch((err) => err); // 跳转路由
      },
      syncActiveIndex(route) {
        const routes = {
          '/homepage': '1',
          '/cloud_platform': '2',
          '/help': '3',
          '/applied': '4',
          '/personal_center': '5',
        };
        const index = routes[route.path] || '1';
        this.updateActiveIndex(index);
      },
    },
  created() {
    this.syncActiveIndex(this.$route);
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
    background-color: 	#0F172A;
}
.el-menu-item.is-active {
  position: relative; /* 为底部边框定位 */
  background-color: #E9EEF3;
  border-radius: 5%;
}

.header{
  width: 100%;
  background-color: 	#0F172A;
  z-index: 1000;
}
.el-menu.el-menu--horizontal {
  height: 60px; /* 或者与 header 相同的高度 */
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
    font-size: large;
    text-align: center;
    font-weight: bold;
    width: 130px;

}
.header_line{
  height: 30px;
  width: 1px;
  background-color: #77DDFF;
}

</style>
