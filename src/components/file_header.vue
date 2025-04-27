<template>
  <div style="line-height: 60px;display: flex; overflow: hidden;">
    <div style="flex:1">
      <span :class="collapseBtnClass" style="cursor: pointer; font-size: 18px" @click="collapse"></span>
      <el-breadcrumb separator="/" style="display: inline-block; margin-left: 10px">
        <el-breadcrumb-item :to="{ path: '/' }">文件</el-breadcrumb-item>
        <el-breadcrumb-item>{{ currentPathName }}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
  </div>
</template>

<script>
export default {
  name: "file_header",
  props: {
    collapseBtnClass: String,
    collapse: Function,
  },
  methods: {
  },
  computed: {
    currentPathName () {
      return this.$store.state.currentPathName
    }
  },
  watch: {
    currentPathName (newVal, oldVal) {
      console.log(newVal)
    }
  }
};
</script>

<style scoped>
</style>
