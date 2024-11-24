<template>
  <div id="app" style="display: flex">
    <Vue_header style="position: sticky;min-width: 80%;flex-shrink: 0;height: 60px"></Vue_header>
    <router-view :key="$route.path" style="background-color: #E0F2FE;height: calc(100vh - 60px)"></router-view>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue_header from '@/components/vue_header.vue';
import Vue_main from '@/components/vue_main.vue';


export default {
  components: {
    Vue_header,
    Vue_main
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