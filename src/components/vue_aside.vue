<template>
  <div id="app">
    <div style="display: inline-flex;">
      <el-aside :width="side_width + 'px'" :collapse="isDrawerOpen" class="el-aside">
        <el-menu :default-active="$route.path">
          <el-menu-item class="disabled">
            <div slot="title">
              <i class="el-icon-document"></i>图表分类
            </div>
          </el-menu-item>
          <el-menu-item index="/cloud_platform/data_visualization" @click="goToPart('data_visualization')">
            <span slot="title">数据可视化</span>
          </el-menu-item>
          <el-menu-item index="/cloud_platform/data_preprocess" @click="goToPart('data_preprocess')">
            <span slot="title">数据前处理</span>
          </el-menu-item>
          <el-menu-item index="/cloud_platform/ai_analysis" @click="goToPart('ai_analysis')">
            <span slot="title">AI辅助分析</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <div>
        <button :label="false" @click="toggleDrawer" class="button"><i :class="iconClass" style="font-size: 25px"></i></button>
      </div>
    </div>
  </div>
</template>

<script>
import ElementUI from 'element-ui';
import Vue from 'vue';

Vue.component(ElementUI)

export default {
  data() {
    return {
      isDrawerOpen: false,
      iconOpen:'el-icon-s-unfold',
      iconClose:'el-icon-s-fold',
      side_width:200,
    };
  },
  computed:{
    //改变图标方法
    iconClass() {
      return this.isDrawerOpen ? this.iconOpen : this.iconClose;
    },
  },

  methods: {
    //aside栏完全收回方法
    toggleDrawer() {
      this.isDrawerOpen = !this.isDrawerOpen
      if (this.isDrawerOpen){
        this.side_width=0
      }else {
        this.side_width=200
      }
    },
    //页面跳转方法
    goToPart(page){
      // this.$emit('navigate1', page);
      // console.log(page);
      this.$router.push('/cloud_platform/'+page).catch(err => err);
    }
  }
}

</script>

<style>
body{
  height: 1400px;
  position: fixed;
  margin-top: -1px;
  padding-top: -1px;
}

.button{
  height: 50px;
  padding: 0;
  position: fixed;
  width: 40px;
  border: none;
  border-bottom-right-radius: 30%;
}
.el-aside{
  width: 199px;
  height: 94vh;
  padding: 0;
}
.disabled{
  pointer-events: none; /* 禁止鼠标事件 */
  cursor: default; /* 改变鼠标样式 */
}
.disabled:hover{
  background-color: transparent; /* 移除背景色变化 */
}
</style>