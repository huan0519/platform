<template>
  <div id="app">
      <Vue_header></Vue_header>
    <div>
    <el-card class="card">
      <img :src="cardimage" class="card_img"/>
      <div role="separator" class="card_line">
      </div>
      <el-descriptions>
        <el-descriptions-item label="用户名">kooriookami</el-descriptions-item>
        <el-descriptions-item label="手机号">10086</el-descriptions-item>
        <el-descriptions-item label="居住地">苏州市</el-descriptions-item>
        <el-descriptions-item label="备注">
          <el-tag size="small">学校</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="联系地址">江苏省苏州市吴中区吴中大道 1188 号</el-descriptions-item>
      </el-descriptions>
    </el-card>
    </div>

  </div>
</template>

<script>
import Vue_header from "@/components/vue_header.vue";
import card_img from '../assets/logo.png';

export default {
  components:{
    Vue_header
  },
  data(){
    return{
      cardimage: card_img,
    }
  }
}
</script>

<style scoped>
.card{
  height: 50vh;
  align-content: start;
  margin: 50px 250px 20px;
}
.card_img{
  width: 80px;
  height: 80px;
  border-radius: 50%;
  cursor: pointer;
}
.card_line{
  border-bottom: 1px solid #000; /* 黑色分割线 */
  margin: 20px 0;
}
</style>