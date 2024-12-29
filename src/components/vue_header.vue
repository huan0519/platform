<template>
  <div class="scanline-header">
    <img src="../../public/image/logo.png" style="height: 60px; float: left" />

    <el-menu :default-active="activeIndex" class="el-menu" mode="horizontal">
      <p class="header_line"></p>
      <el-menu-item class="el-menu-item" index="homepage" @click="navigate('homepage')">首页</el-menu-item>
      <p class="header_line"></p>
      <el-menu-item class="el-menu-item" index="cloud_platform" @click="navigate('cloud_platform')">云平台</el-menu-item>
      <p class="header_line"></p>
      <el-menu-item class="el-menu-item" index="help" @click="navigate('help')">使用教程</el-menu-item>
      <p class="header_line"></p>
      <el-menu-item class="el-menu-item" index="applied" @click="navigate('applied')">应用统计</el-menu-item>
      <p class="header_line"></p>
      <div style="margin-left: 20px; margin-right: 20px">
        <userinfo @ChangePage="navigate('personal_center')"></userinfo>
      </div>
    </el-menu>
  </div>
</template>

<script>
import ElementUI from "element-ui";
import { mapState, mapActions } from "vuex";
import Vue from "vue";
import userinfo from "@/components/userinfo.vue";

Vue.use(ElementUI);

export default {
  components: {
    userinfo,
  },
  data() {
    return {
      activeIndex: "", // 默认选中项
    };
  },
  computed: {
    ...mapState(["activeIndex"]),
  },
  watch: {
    $route(to) {
      this.syncActiveIndex(to); // 路由变化时同步导航状态
    },
  },
  created() {
    this.syncActiveIndex(this.$route);
  },
  methods: {
    ...mapActions(["updateActiveIndex"]),
    navigate(page) {
      this.$router.push("/" + page).catch((err) => err);
    },
    syncActiveIndex(route) {
      const path = route.path;

      // 定义路径与导航索引的映射关系
      const pathMap = {
        "/homepage": "homepage",
        "/cloud_platform": "cloud_platform",
        "/help": "help",
        "/applied": "applied",
        "/personal_center": "personal_center",
      };

      // 特殊处理子路径匹配的逻辑
      let currentIndex = "homepage"; // 默认首页
      if (path.startsWith("/cloud_platform")) {
        currentIndex = "cloud_platform";
      } else if (path.startsWith("/help")) {
        currentIndex = "help";
      } else if (path.startsWith("/applied")) {
        currentIndex = "applied";
      } else if (path.startsWith("/personal_center")) {
        currentIndex = "personal_center";
      }

      // 更新高亮状态
      this.updateActiveIndex(currentIndex);
      this.activeIndex = currentIndex;
    },
  },
};
</script>


<style scoped>
.el-menu-item:hover {
  background-color: #000000; /* 悬停时的背景颜色 */
  color: #f6f5f5; /* 悬停时的文字颜色 */
}
.el-menu {
  float: right;
  height: 60px;
  display: flex;
  align-items: center; /* 垂直居中子元素 */
  justify-content: space-between;
  background-color: #0f172a;
}
.el-menu-item.is-active {
  position: relative; /* 为底部边框定位 */
  background-color: #e9eef3;
  border-radius: 5%;
}
.scanline-header {
  width: 100%;
  background-color: #0f172a;
  z-index: 1000;
}
.scanline-header:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, transparent, rgba(125, 215, 255, 0.2), transparent);
  animation: scanline 5s linear infinite;
}
@keyframes scanline {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}
.el-menu.el-menu--horizontal {
  height: 60px; /* 或者与 header 相同的高度 */
  background-color: rgba(0, 255, 0, 0);
}
.link {
  font-size: large;
  float: right;
  margin-top: 10px;
  color: rgb(141, 166, 158);
}
.el-menu-item {
  min-width: 90px; /* Use min-width instead of width */
  margin-bottom: 0;
  font-size: large;
  text-align: center;
  font-weight: bold;
  width: 130px;
}
.header_line {
  height: 30px;
  width: 1px;
  background-color: #77ddff;
}
</style>
