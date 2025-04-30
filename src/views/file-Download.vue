<template>
  <div id="app" style="height: 100vh;overflow: auto;display: flex">
  <el-container>
    <el-aside class="file_aside" :width="sideWidth + 'px'" style="box-shadow: 2px 0 6px rgb(0 21 41 / 35%)">
      <file_aside :is-collapse="isCollapse" :logotextshow="logotextshow" />
    </el-aside>
    <el-container style="overflow: auto">
      <el-header style="border-bottom: 1px solid #ccc;">
        <file_header :collapseBtnClass="collapseBtnClass" :collapse="collapse"></file_header>
      </el-header>
      <el-main class="file_main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
  </div>
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
      collapseBtnClass: 'el-icon-s-fold',
      logotextshow: true,
    };
  },
  methods: {
    // 切换侧边栏折叠
    collapse() {
      this.isCollapse = !this.isCollapse;
      if (this.isCollapse) {
        this.sideWidth = 64;
        this.collapseBtnClass = 'el-icon-s-unfold';
        this.logotextshow=false
      } else {
        this.sideWidth = 200;
        this.collapseBtnClass = 'el-icon-s-fold';
        this.logotextshow=true
      }
    }
  }
};
</script>

<style scoped>
.file_aside{
  top: 0;
  max-height: calc(100vh - 5.9rem);
  position: sticky;
  overflow: hidden;
}
.file_main{
  flex-grow: 1;
  overflow-y: auto;
}
</style>
