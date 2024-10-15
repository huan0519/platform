<template>
  <el-container>
    <Vue_aside></Vue_aside>
    <Cloud_main></Cloud_main>
  </el-container>
</template>

<script>
import Vue_aside from "@/components/vue_aside.vue";
import Cloud_main from "@/components/cloud_main.vue";

export default{
  components:{
    Vue_aside,
    Cloud_main
  }
}
</script>

<style scoped>
.cloud{
  display: inline-block;
}

</style>