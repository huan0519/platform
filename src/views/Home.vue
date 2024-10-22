<template>
  <div id="app">
    <Vue_header style="position: fixed;"></Vue_header>
    <router-view :key="$route.path"></router-view>
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
  name:"App",


  components: {
    Vue_header,
    Vue_main,
  },
  data(){
    return{
      //默认页面：主页
      currentPage:'Homepage'
    };
  },
  methods:{

  }
}
</script>

<style>
#app{
  display: flex;
  flex-direction: column;
  height: 100%; /* 视口高度 */
}

</style>