<template>
  <div id="app">
    <Vue_header></Vue_header>
    <div>
      <Vue_main></Vue_main>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue_header from '@/components/vue_header.vue';
import Vue_main from '@/components/vue_main.vue';
import ElementUI from 'element-ui';
import Vue from 'vue';

Vue.component(ElementUI)

export default {

  components: {
    Vue_header,
    Vue_main
  }
}
</script>

<style>
#app{
  display: flex;
  flex-direction: column;
  height: 100vh; /* 视口高度 */
}



</style>