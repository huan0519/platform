<template>
  <div id="app">
    <Vue_header></Vue_header>
    <div>
      <Vue_aside></Vue_aside>
      <Vue_main></Vue_main>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import vue_header from "@/components/vue_header.vue";
import vue_aside from "@/components/vue_aside.vue";
import Vue_main from "@/components/vue_main.vue";
import ElementUI from "element-ui";


Vue.component(ElementUI)

export default {
  components:{
    Vue_main,
    vue_header,
    vue_aside
  }
}
</script>

<style>

</style>