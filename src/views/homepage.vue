<!--主页-->
<template>
  <div id="app">
    <div class="image-card">
      <img src="../../public/image/home_show.jpg" class="image" />
      <div class="overlay">
        <span class="home_font">欢迎使用云平台</span>
        <div style="margin-top: 100px">
          <!-- 跳转到云平台并高亮 -->
          <el-button style="height: 48px;width: 148px; border-radius: 15px" type="primary" @click="navigate('/help', '3')" >快速入门</el-button>
          <!-- 跳转到使用教程并高亮 -->
          <el-button style="margin-left: 80px;border-radius: 15px;height: 48px;width: 148px" @click="navigate('/cloud_platform', '2')">一键做图</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  methods: {
    ...mapActions(['updateActiveIndex']), // 调用 Vuex 的 action
    navigate(route, index) {
      this.updateActiveIndex(index); // 更新导航的高亮状态
      this.$router.push(route).catch((err) => err); // 路由跳转
    },
  },
};
</script>

<style scoped>
.image-card {
  position: relative;
  overflow: hidden;
  margin-top: 50px;
  width: 1400px;
  height: 800px;
  align-self: center;
}

.image {
  justify-self: center;
  display: block;
  width: 1400px;
  height: 800px;
  border-radius: 5%;
}

.overlay {
  position: absolute;
  top: 250px;
  left: 100px;
}

.home_font {
  color: whitesmoke;
  font-size: 70px;
}
</style>
