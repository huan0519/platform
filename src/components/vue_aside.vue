<!--云平台侧面导航栏-->
<template>
  <div id="app">
    <div style="display: inline-flex;">
      <el-aside :width="side_width + 'px'" :collapse="isDrawerOpen" class="el-aside">
        <el-menu
            :default-active="currentActive"
            style="height: 100%; overflow: hidden; background-color: #FFFFFF;">
          <el-menu-item class="disabled">
            <div slot="title">
              <i class="el-icon-document"></i
              ><span
                style="font-weight: bolder; font-family: '微软雅黑 Light', serif; font-size: 15px; color: #93C5FD; margin-left: 4px"
            >模块分类</span
            >
            </div>
          </el-menu-item>
          <el-menu-item
              index="/cloud_platform/data_visualization"
              @click="goToPart('data_visualization')"
          >
            <span slot="title">数据可视化</span>
          </el-menu-item>
          <el-submenu index="/cloud_platform/data_preprocess">
            <template>
              <span slot="title" style="color: #00bbff">数据预处理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/cloud_platform/data_normalization" @click="goToPart('data_normalization')">数据归一化</el-menu-item>
              <el-menu-item index="/cloud_platform/reinforce" @click="goToPart('reinforce')">补值</el-menu-item>
              <el-menu-item index="/cloud_platform/alignment" @click="goToPart('alignment')">数据对齐</el-menu-item>
              <el-menu-item index="/cloud_platform/data_enhancement" @click="goToPart('data_enhancement')">数据降维</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item
              index="/cloud_platform/prediction"
              @click="goToPart('prediction')"
          >
            <span slot="title">疾病预测</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <div>
        <button :label="false" @click="toggleDrawer" class="button">
          <i :class="iconClass" style="font-size: 25px"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import ElementUI from "element-ui";
import Vue from "vue";

Vue.component(ElementUI);

export default {
  data() {
    return {
      isDrawerOpen: false,
      iconOpen: "el-icon-s-unfold",
      iconClose: "el-icon-s-fold",
      side_width: 200,
      currentActive: this.$route.path, // 当前激活的菜单路径
      validPaths: [
        "/cloud_platform/data_visualization/",
        "/cloud_platform/data_preprocess/",
        "/cloud_platform/prediction/",
        "/cloud_platform/"
      ], // 合法路径列表
    };
  },
  computed: {
    // 改变图标方法
    iconClass() {
      return this.isDrawerOpen ? this.iconOpen : this.iconClose;
    },
  },
  watch: {
    // 监听路由变化
    "$route.path"(newPath) {
      if (this.validPaths.includes(newPath)) {
        this.currentActive = newPath; // 更新激活状态
      }
    },
  },
  methods: {
    // aside栏完全收回方法
    toggleDrawer() {
      this.isDrawerOpen = !this.isDrawerOpen;
      this.side_width = this.isDrawerOpen ? 0 : 200;
    },
    // 页面跳转方法
    goToPart(page) {
      this.$router.push("/cloud_platform/" + page).catch((err) => err);
    },
  },
};
</script>

<style scoped>
.el-menu{
  height: 100%;
  overflow: hidden;
}
.aside_line {
  margin: 1px;
  height: 1px;
  width: calc(100% - 10px);
  background-color: #666666;
  align-self: center;
}
.button {
  height: 50px;
  padding: 0;
  position: fixed;
  width: 40px;
  border: none;
  border-bottom-right-radius: 30%;
}
.button :hover{
  cursor: pointer;
}
.el-aside {
  transition: width 0.3s ease-in-out;
  width: 200px;
  height: 100vh;
  overflow-y: hidden;
}
.disabled {
  pointer-events: none; /* 禁止鼠标事件 */
  cursor: default; /* 改变鼠标样式 */
}
.disabled:hover {
  background-color: transparent; /* 移除背景色变化 */
}
.el-menu-item {
  color: #00bbff;
}
::v-deep(.el-menu-item.is-active) {
  color: #fb923c !important;
  background-color: #e9eef3;
  border-right-style: groove;
}
</style>
