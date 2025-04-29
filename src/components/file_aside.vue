<template>
  <el-menu :default-openeds="['1', '2']"
           :collapse="isCollapse"
           :collapse-transition="false"
           style="min-height: 100vh;overflow: hidden"
           background-color="#545c64"
           text-color="#fff"
           active-text-color="#ffd04b"
           router
  >
    <div style="height: 60px; line-height: 60px; text-align: center">
      <img src="../assets/1.png" alt="" style="width: 25px;height: 25px; margin-right: 5px; position: relative; top: 5px"/>
      <b style="color: white" v-show="logotextshow">文件管理</b>
    </div>
    <el-menu-item index="/file_download/file_sum">
      <i class="el-icon-s-data"></i>
      <span slot="title">数据总览</span>
    </el-menu-item>
    <el-menu-item index="/file_download/file_info_sum">
      <i class="el-icon-document"></i>
      <span slot="title">数据信息总览</span>
    </el-menu-item>
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-s-cooperation"></i>
        <span slot="title">数据管理</span>
      </template>
      <el-menu-item index="/file_download/normalization_file">
        <span slot="title">归一化数据</span>
      </el-menu-item>
      <el-menu-item index="/file_download/reinforce_file">
        <span slot="title">补值后数据</span>
      </el-menu-item>
      <el-menu-item index="/file_download/alignment_file">
        <span slot="title">对齐后数据</span>
      </el-menu-item>
      <el-menu-item index="/file_download/dimension_file">
        <span slot="title">降维后数据</span>
      </el-menu-item>
      <el-menu-item index="/file_download/result_file">
        <span slot="title">训练结果数据</span>
      </el-menu-item>
    </el-submenu>
    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-notebook-2"></i>
        <span slot="title">数据信息管理</span>
      </template>
      <el-menu-item index="/file_download/normalization_info_file">
        <span slot="title">归一化信息</span>
      </el-menu-item>
      <el-menu-item index="/file_download/reinforce_info_file">
        <span slot="title">补值后信息</span>
      </el-menu-item>
      <el-menu-item index="/file_download/alignment_info_file">
        <span slot="title">对齐后信息</span>
      </el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<script>
export default {
  name: "file_aside",
  props:{
    isCollapse: Boolean,
    logotextshow: Boolean
  },
  data() {
    return {

    };
  },
  methods: {
  }
};
</script>

<style scoped>
</style>
