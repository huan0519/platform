<template>
  <div style="display: flex;">
  <div style="display: flex;">
  <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isDrawerOpen">
    <el-menu-item index="0">
      <div slot="title">
        <i class="el-icon-document"></i>图表分类
      </div>
    </el-menu-item>
    <el-submenu index="1">
      <template slot="title">
        
        <span slot="title">数据可视化</span>
      </template>
      <el-menu-item-group>
        <span slot="title">数据预处理</span>
        <el-menu-item index="1-1">选项1</el-menu-item>
        <el-menu-item index="1-2">选项2</el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group title="分组2">
        <el-menu-item index="1-3">选项3</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-menu-item index="2">
      <span slot="title">数据归一化</span>
    </el-menu-item>
    <el-menu-item index="4">
      <span slot="title">AI辅助分析</span>
    </el-menu-item>
  </el-menu>
  
  </div>
  <button :label="false" @click="toggleDrawer" style="height: 5vh;width: 3vw;;border: none;padding: 0;"><i :class="iconClass"></i></button>
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
        iconClose:'el-icon-s-fold'
      };
    },
    computed:{
      iconClass() {
      return this.isDrawerOpen ? this.iconOpen : this.iconClose;
    },
    },

    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      toggleDrawer() {
      this.isDrawerOpen = !this.isDrawerOpen;
    }
    }
  }

</script>

<style>

.el-menu-vertical-demo{
  height: 100vh;
  width: 10vw;
  }




</style>