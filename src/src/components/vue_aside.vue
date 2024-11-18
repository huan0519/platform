<template>
  <div id="app">
    <div style="display: inline-flex;">
      <el-aside :width="side_width + 'px'" :collapse="isDrawerOpen" class="el-aside">
        <el-menu
            :default-active="currentActive"
            style="height: 100%; overflow: hidden; background-color: #334155;"
        >
          <el-menu-item class="disabled">
            <div slot="title">
              <i class="el-icon-document"></i
              ><span
                style="font-weight: bolder; font-family: '微软雅黑 Light', serif; font-size: 15px; color: #93C5FD; margin-left: 4px"
            >图表分类</span
            >
            </div>
          </el-menu-item>
          <p class="aside_line"></p>
          <el-menu-item
              index="/cloud_platform/data_visualization"
              @click="goToPart('data_visualization')"
          >
            <span slot="title">数据可视化</span>
          </el-menu-item>
          <p class="aside_line"></p>
          <el-menu-item
              index="/cloud_platform/data_preprocess"
              @click="goToPart('data_preprocess')"
          >
            <span slot="title">数据前处理</span>
          </el-menu-item>
          <p class="aside_line"></p>
          <el-menu-item
              index="/cloud_platform/prediction"
              @click="goToPart('prediction')"
          >
            <span slot="title">疾病预测</span>
          </el-menu-item>
          <p class="aside_line"></p>
          <el-menu-item
              index="/cloud_platform/ai_analysis"
              @click="goToPart('ai_analysis')"
          >
            <span slot="title">AI辅助分析</span>
          </el-menu-item>
          <p class="aside_line"></p>
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
        "/cloud_platform/data_visualization",
        "/cloud_platform/data_preprocess",
        "/cloud_platform/prediction",
        "/cloud_platform/ai_analysis",
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
body {
  height: 100vh;
  position: fixed;
  margin-top: -1px;
  padding-top: -1px;
}
.aside_line {
  margin: 1px;
  height: 1px;
  width: 9vw;
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
.el-aside {
  width: 199px;
  height: 94vh;
  padding: 0;
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
