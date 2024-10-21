<template>
  <div id="app">
    <border></border>
    <div>
      <el-carousel :interval="4000" type="card" height="400px" class="el-carousel">
      <el-carousel-item v-for="item in 6" :key="item">
        <h3 class="medium">{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>
    </div>
  </div>
</template>

<script>
import vue_header from "@/components/vue_header.vue";
import border from "@/components/header-border.vue"

export default {
  components:{
    vue_header,
    border
  }
}
</script>

<style scoped>
.el-carousel{
  margin: 5em;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>