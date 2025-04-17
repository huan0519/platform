<!--页面框架-->
<template>
  <div id="app" style="display: flex">
    <Vue_header style="  background-color: #0f172a;;position: relative;min-width: 80%;flex-shrink: 0;height: 6.25rem"></Vue_header>
    <router-view :key="$route.path" style="height: calc(100vh - 9vh)"></router-view>
    <div style="height: 1.25rem;background: #0f172a"></div>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue_header from '@/components/vue_header.vue';


export default {
  components: {
    Vue_header,
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