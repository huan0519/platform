<template>
  <div>
    <ParticlesEffect />
    <div class="content">
      <h1>欢迎使用 Vue 2 和 Particles.js</h1>
    </div>
  </div>
</template>

<script>
import ParticlesEffect from "@/components/demo.vue";

export default {
  components: {
    ParticlesEffect,
  },
};
</script>

<style>
.content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #fff;
  text-align: center;
}
</style>
