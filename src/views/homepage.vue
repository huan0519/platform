<template>
  <div style="margin: 0; height: 100vh; width: 100vw; display: flex; justify-content: center;">
    <div class="image-card">
      <img src="../../public/image/home_show.jpg" class="image" />
      <div class="overlay">
        <span class="home_font">欢迎使用云平台</span>
        <div style="margin-top: 66px; color: whitesmoke; font-size: large; font-style: oblique">
          助力科学探索，精彩研究成果
        </div>
        <div style="margin-top: 80px;display: flex">
          <button @click="navigate('/cloud_platform', '2')" class="home-button">
            <span>一键做图</span>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 74 74"
                height="34"
                width="34"
            >
              <circle stroke-width="3" stroke="black" r="35.5" cy="37" cx="37"></circle>
              <path
                  fill="black"
                  d="M25 35.5C24.1716 35.5 23.5 36.1716 23.5 37C23.5 37.8284 24.1716 38.5 25 38.5V35.5ZM49.0607 38.0607C49.6464 37.4749 49.6464 36.5251 49.0607 35.9393L39.5147 26.3934C38.9289 25.8076 37.9792 25.8076 37.3934 26.3934C36.8076 26.9792 36.8076 27.9289 37.3934 28.5147L45.8787 37L37.3934 45.4853C36.8076 46.0711 36.8076 47.0208 37.3934 47.6066C37.9792 48.1924 38.9289 48.1924 39.5147 47.6066L49.0607 38.0607ZM25 38.5L48 38.5V35.5L25 35.5V38.5Z"
              ></path>
            </svg>
          </button>

          <el-button class="left-button" style="margin-left: 50px;height: 55px; width: 148px" type="primary" @click="navigate('/help', '3')">快速入门</el-button>

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
  height: 58px;
  width: 148px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  border: none;
  border-radius: 8px;
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

.home-button {
  width: 160px;
  cursor: pointer;
  font-weight: 700;
  transition: all 0.2s;
  padding: 10px 20px;
  background: white;
  border-radius: 100px;
  border: 1px solid transparent;
  display: flex;
  align-items: center;
  font-size: 15px;
}

.home-button:hover {
  background: whitesmoke;
}

.home-button > svg {
  width: 34px;
  margin-left: 10px;
  transition: transform 0.3s ease-in-out;
}

.home-button:hover svg {
  transform: translateX(5px);
}

.home-button:active {
  transform: scale(0.95);
}
</style>
