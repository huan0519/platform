<template>
  <el-container style="min-height: 100vh;overflow: auto">
    <el-aside :width="sideWidth + 'px'" style="box-shadow: 2px 0 6px rgb(0 21 41 / 35%)">
      <file_aside :is-collapse="isCollapse" />
    </el-aside>
    <el-container style="overflow: auto">
      <el-header style="border-bottom: 1px solid #ccc;">
        <file_header :collapseBtnClass="collapseBtnClass" :collapse="collapse"></file_header>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import file_aside from "@/components/file_aside.vue";
import file_header from "@/components/file_header.vue";

export default {
  components: { file_aside, file_header },
  data() {
    return {
      // 侧边栏折叠相关
      isCollapse: false,
      sideWidth: 200,
      collapseBtnClass: 'el-icon-s-fold'
    };
  },
  methods: {
    // 切换侧边栏折叠
    collapse() {
      this.isCollapse = !this.isCollapse;
      if (this.isCollapse) {
        this.sideWidth = 64;
        this.collapseBtnClass = 'el-icon-s-unfold';
      } else {
        this.sideWidth = 200;
        this.collapseBtnClass = 'el-icon-s-fold';
      }
    }
  }
};
</script>

<style scoped>
</style>
