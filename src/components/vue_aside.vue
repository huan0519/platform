<template>
  <div id="app">
  <div style="display: flex;">
      <el-aside :width="sidewidth + 'px'" :collapse="isDrawerOpen" class="el-aside">
        <el-menu default-active="1-4-1">
          <el-menu-item index="1">
            <div slot="title">
              <i class="el-icon-document"></i>图表分类
            </div>
          </el-menu-item>
          <el-menu-item index="2" @click="goToPart('Data_visualization')">
            <span slot="title">数据可视化</span>
          </el-menu-item>
          <el-menu-item index="3" @click="goToPart('Data_preprocess')">
            <span slot="title">数据前处理</span>
          </el-menu-item>
          <el-menu-item index="4" @click="goToPart('AI_analysis')">
            <span slot="title">AI辅助分析</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
    <div>
      <button :label="false" @click="toggleDrawer" style="height:5vh;width: 3vw;;border: none;padding: 0;border-bottom-right-radius: 30%;position: fixed"><i :class="iconClass" style="font-size: 25px"></i></button>
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
        sidewidth:200
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
        this.sidewidth=0
      }else {
        this.sidewidth=200
        }
      },
      //页面跳转方法
      goToPart(page){
        this.$emit('navigate1', page);
        console.log(page);
      }
    }
  }

</script>

<style>
body{
  height: 100vh;
  position: fixed;
  margin-top: -1px;
  padding-top: -1px;
}

.button{
  height: 5vh;
}
.el-aside{
  width: 199px;
  height: 94vh;
  padding: 0;
}
</style>