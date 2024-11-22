<template>
  <div id="splash-container" @click="createSplash($event)">
    <!-- 动画容器，点击触发水花效果 -->
  </div>
</template>

<script>
import anime from "animejs";

export default {
  methods: {
    createSplash(event) {
      const { clientX, clientY } = event;

      // 创建一个新的水花 DOM 元素
      const splash = document.createElement("div");
      splash.classList.add("splash");
      splash.style.left = `${clientX}px`;
      splash.style.top = `${clientY}px`;
      document.body.appendChild(splash);

      // 动画效果
      anime({
        targets: splash,
        scale: [0, 1],
        opacity: [1, 0],
        easing: "easeOutQuad",
        duration: 800,
        complete: () => {
          // 动画完成后移除 DOM 元素
          splash.remove();
        },
      });
    },
  },
};
</script>

<style>
#splash-container {
  width: 100%;
  height: 100vh;
  background-color: #282c34;
  position: relative;
  overflow: hidden;
  cursor: pointer;
}

.splash {
  position: absolute;
  width: 150px;
  height: 150px;
  background-color: rgba(0, 150, 255, 0.6);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none; /* 防止水花干扰点击事件 */
}
</style>
