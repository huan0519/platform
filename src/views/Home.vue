<template>
  <div id="app">
    <Vue_header @navigate="handleNavigation"></Vue_header>
      <Vue_main :current-page="currentPage"></Vue_main>
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
    Vue_main,
  },
  data(){
    return{
      //默认页面：主页
      currentPage:'Homepage'
    };
  },
  methods:{
    //将header中取到的页面赋值给currentPage
    handleNavigation(page){
      this.currentPage = page;
    }
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