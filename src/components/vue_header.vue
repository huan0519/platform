<template>
<!--  <div class="scanline-header">-->
  <div>
      <div class="loading" style="float: left;margin-left: 1rem;padding: 1.25rem">
        <svg width="64px" height="48px">
          <polyline points="0.157 23.954, 14 23.954, 21.843 48, 43 0, 50 24, 64 24" id="back"></polyline>
          <polyline points="0.157 23.954, 14 23.954, 21.843 48, 43 0, 50 24, 64 24" id="front"></polyline>
        </svg>
      </div>
    <el-menu :default-active="activeIndex" class="h-el-menu" mode="horizontal">
      <p class="header_line"></p>
      <el-menu-item class="h-el-menu-item" index="cloud_platform" @click="navigate('cloud_platform')">
        <div class="h-item-group1">云平台</div>
        <div class="h-item-group2">icloud</div>
      </el-menu-item>
      <p class="header_line"></p>
      <el-menu-item class="h-el-menu-item" index="ai_analysis" @click="navigate('ai_analysis')">
        <div class="h-item-group1">大模型</div>
        <div class="h-item-group2">AI</div>
      </el-menu-item>
      <p class="header_line"></p>
      <el-menu-item class="h-el-menu-item" index="file_download" @click="navigate('file_download')">
        <div class="h-item-group1">文件下载</div>
        <div class="h-item-group2">download</div>
      </el-menu-item>
      <p class="header_line"></p>
      <el-menu-item class="h-el-menu-item" index="help" @click="navigate('help')">
        <div class="h-item-group1">帮助</div>
        <div class="h-item-group2">help</div>
      </el-menu-item>
      <p class="header_line"></p>
      <div style="margin-left: 70px; margin-right: 40px">
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
        "/personal_center": "personal_center",
        "/ai_analysis": "ai_analysis",
        "/file_download": "file_download"
      };

      // 特殊处理子路径匹配的逻辑
      let currentIndex = "cloud_platform"; // 默认首页
      if (path.startsWith("/cloud_platform")) {
        currentIndex = "cloud_platform";
      } else if (path.startsWith("/help")) {
        currentIndex = "help";
      } else if (path.startsWith("/personal_center")) {
        currentIndex = "personal_center";
      } else if (path.startsWith("/ai_analysis")) {
        currentIndex = "ai_analysis";
      } else if (path.startsWith("/file_download")) {
        currentIndex = "file_download";
      }

      // 更新高亮状态
      this.updateActiveIndex(currentIndex);
      this.activeIndex = currentIndex;
    },
  },
};
</script>


<style scoped>
.h-el-menu {

  float: right;
  display: flex;
  align-items: center; /* 垂直居中子元素 */
}
.h-el-menu-item.is-active {
  border-radius: 5%;
  height: 100%;
}
.scanline-header {
  background-repeat: no-repeat;
  background-position: 70%;
  background-size: cover;
  color: black;
  flex: none;
  width: 100%;
  background-color: #f6f5f5;
  z-index: 20;
}
.scanline-header::after{
  background-image: linear-gradient(180deg, #0003, #00000005 40%, #0000);
  background-position: top;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  content: "";
  display: block;
  height: 3rem;
  left: 0;
  pointer-events: none;
  position: absolute;
  top: 100%;
  width: 100%;
}
.h-el-menu.el-menu--horizontal {
  margin-left: auto;
  margin-right: 40px;
  height: 100%; /* 或者与 header 相同的高度 */
  background-color: rgba(0, 255, 0, 0);
}
.el-menu--horizontal .el-menu-item:hover {
  border-bottom: 3px solid #fb923c !important; /* 自定义颜色 */
  background-color: transparent !important;
  border-radius: 5%;
}
.el-menu--horizontal > .el-menu-item.is-active {
  border-bottom: 3px solid 	#fb923c; /* 自定义激活状态横条颜色 */
  background-color: transparent !important;
}
.el-menu--horizontal > .el-menu-item{
  height: 100%;
  align-items: center; /* 垂直居中子元素 */
}
.h-el-menu-item {
  height: 100%;
  min-width: 90px; /* Use min-width instead of width */
  font-weight: bold;
  width: 150px;
  transition: border-color 0.3s; /* 添加过渡动画 */
}
.header_line {
  height: 30px;
  width: 1px;
  background-color: #77ddff;
}
.h-item-group1{
  color: whitesmoke;
  font-size: 19px;
  padding: 0;
  height: 40%;
  margin-top: 10px;
}
.h-item-group2{
  color: #8c8c8c;
  font-family: "AniMe Vision - MB_EN";
  font-size: .9375rem;
  height: 1rem;
  margin-top: -10px;
}
.loading svg polyline {
  fill: none;
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.loading svg polyline#back {
  fill: none;
  stroke: #ff4d5033;
}

.loading svg polyline#front {
  fill: none;
  stroke: #ff4d4f;
  stroke-dasharray: 48, 144;
  stroke-dashoffset: 192;
  animation: dash_682 1.4s linear infinite;
}

@keyframes dash_682 {
  72.5% {
    opacity: 0;
  }

  to {
    stroke-dashoffset: 0;
  }
}

</style>
