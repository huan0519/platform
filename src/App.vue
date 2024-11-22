<template>
  <div id="app" @click="createSplash($event)">
    <router-view></router-view>
</div>
</template>

<script>


import anime from "animejs";

export default{
    name:'App',

  methods:{
    createSplash(event) {
      const { clientX, clientY } = event;

      // 创建一个新的水花 DOM 元素
      const splash = document.createElement("div");
      splash.classList.add("splash");

      // 设置初始位置并考虑宽高居中
      const size = 40; // 水花大小
      splash.style.width = `${size}px`;
      splash.style.height = `${size}px`;
      splash.style.left = `${clientX - size / 2}px`;
      splash.style.top = `${clientY - size / 2}px`;

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
  }
  }

</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  padding: 0;
  width: 100vw;
  height: 100vh;
}
.splash {
  position: absolute;
  background-color: rgba(0, 150, 255, 0.6);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none; /* 防止水花干扰点击事件 */
}
</style>