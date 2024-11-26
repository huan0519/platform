<!--帮助侧边导航-->
<template>
  <div>
    <div style="height: 50px;display: flex;align-items: center;margin: 15px">
      <el-input style="" v-model="input" placeholder="请输入内容"></el-input>
      <el-button style=""><i class="el-icon-search"></i></el-button>
    </div>
    <el-divider></el-divider>
    <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        background-color="#D3DCE6"
        @open="handleOpen"
        @close="handleClose">
      <el-menu-item index="1">
        <span slot="title">云平台入门介绍</span>
      </el-menu-item>
      <el-menu-item index="2">
        <span slot="title">常见问题</span>
      </el-menu-item>
      <el-menu-item index="3">
        <span slot="title">图</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  data(){
    return{
      input:''
    }
  }
}

</script>

<style scoped>

.el-menu-item{
}
</style>