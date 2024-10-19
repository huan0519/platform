<template>
  <div>
    <a style="margin-left: 8vw;font-size: 20px;font-style: italic">数据可视化</a>
    <div class="line-container">
      <div class="horizontal-line"></div>
    </div>
  </div>
</template>

<script>
import vue_header from "@/components/vue_header.vue";
import Vue from "vue";
import Component from "vue-class-component";
import Vue_header from "@/components/vue_header.vue";

@Component({
  components: {
    Vue_header
  }
})
export default class DataVisualization extends Vue {
}


</script>

<style>
.horizontal-line{
  width: 90vw;
  height: 2px;
  background-color: #E9EEF3;
}
.line-container{
  align-items: center;
  margin-top: 10px;
  display: flex;
  justify-content: center;
}
</style>