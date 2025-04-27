<template>
  <div id="app">
    <div style="display: inline-flex;">
      <el-aside :width="side_width + 'px'" :collapse="isDrawerOpen" class="el-aside">
        <el-menu
            :default-openeds="['1', '3']" style="min-height: 100vh;overflow: hidden"
            text-color="#00bbff"
            active-text-color="#fb923c"
            background-color="#FFFFFF"
            :default-active="currentActive"
            @select="handleSelect"
            router
        >
          <el-menu-item class="disabled">
            <div slot="title">
              <i class="el-icon-document"></i>
              <span
                  style="font-weight: bolder; font-family: '微软雅黑 Light', serif; font-size: 15px; color: #93C5FD; margin-left: 4px">
                模块分类
              </span>
            </div>
          </el-menu-item>

          <el-menu-item index="/cloud_platform/data_visualization">
            <span slot="title">数据可视化</span>
          </el-menu-item>

          <el-submenu index="3">
            <template slot="title">
              <span>数据预处理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/cloud_platform/data_normalization">
                <span>数据归一化</span>
              </el-menu-item>
              <el-menu-item index="/cloud_platform/reinforce">
                <span>补值</span>
              </el-menu-item>
              <el-menu-item index="/cloud_platform/alignment">
                <span>数据对齐</span>
              </el-menu-item>
              <el-menu-item index="/cloud_platform/data_enhancement">
                <span>数据降维</span>
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu>

          <el-menu-item index="/cloud_platform/prediction">
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
export default {
  data() {
    return {
      isDrawerOpen: false,
      iconOpen: "el-icon-s-unfold",
      iconClose: "el-icon-s-fold",
      side_width: 200,
      currentActive: this.$route.path,
    };
  },
  computed: {
    iconClass() {
      return this.isDrawerOpen ? this.iconOpen : this.iconClose;
    },
  },
  watch: {
    '$route.path'(newPath) {
      this.currentActive = newPath;
    }
  },
  methods: {
    toggleDrawer() {
      this.isDrawerOpen = !this.isDrawerOpen;
      this.side_width = this.isDrawerOpen ? 0 : 200;
    },
    handleSelect(index) {
      if (this.$route.path !== index) {
        this.$router.push(index).catch(err => err);
      }
    }
  }
};
</script>

<style scoped>
.el-menu {
  height: 100%;
  overflow: hidden;
}
.button {
  height: 50px;
  padding: 0;
  position: fixed;
  width: 40px;
  border: none;
  border-bottom-right-radius: 30%;
}
.button :hover {
  cursor: pointer;
}
.el-aside {
  transition: width 0.3s ease-in-out;
  width: 200px;
  height: 100vh;
  overflow-y: hidden;
}
.disabled {
  pointer-events: none;
  cursor: default;
}
.disabled:hover {
  background-color: transparent;
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
