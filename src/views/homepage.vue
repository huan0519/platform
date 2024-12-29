<template>
  <div style="margin: 0; height: 100vh; width: 100vw; display: flex; justify-content: center;">
    <div class="image-card">
      <img src="../../public/image/home_show.jpg" class="image" />
      <div class="overlay">
        <span class="home_font">欢迎使用云平台</span>
        <div style="margin-top: 66px; color: whitesmoke; font-size: large; font-style: oblique">
          助力科学探索，精彩研究成果
        </div>
        <div style="margin-top: 80px">
          <!-- 跳转到使用教程并高亮 -->
          <el-button class="right-button" style=" border-radius: 15px; height: 48px; width: 148px" @click="navigate('/cloud_platform', '2')">一键做图</el-button>
          <!-- 跳转到云平台并高亮 -->
          <el-button class="left-button" style="margin-left: 50px;height: 48px; width: 148px" type="primary" @click="navigate('/help', '3')">快速入门</el-button>
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
  width: 1200px;
  height: 700px;
  border-radius: 5%;
  margin-top: 60px;
}

.image {
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 5%;
}

.overlay {
  position: absolute;
  top: 220px;
  left: 100px;
}

.home_font {
  color: whitesmoke;
  font-size: 70px;
}
.left-button {
  height: 48px;
  width: 148px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  border: none;
  border-radius: 8px;
  background: linear-gradient(90deg, #4ade80, #2563eb);
  background-size: 300% 100%;
  transition: background-position 0.5s ease, transform 0.3s ease;
}

.left-button:hover {
  background-position: 100% 0;
  transform: scale(1.05);
}

.left-button:active {
  transform: scale(1);
}
.right-button {
  height: 48px;
  width: 148px;
  font-size: 16px;
  font-weight: bold;
  background: linear-gradient(45deg, #2563eb, #4ade80);
  color: #fff;
  border: none;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.right-button:hover {
  color: whitesmoke;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}

.right-button:active {
  transform: translateY(0);
}
</style>
