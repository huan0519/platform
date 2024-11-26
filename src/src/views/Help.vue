<!--帮助-->
<template>
  <div id="app" class="help">
    <Help_aside class="help-aside"/>
    <Help_main class="help-main"/>
  </div>
</template>

<script>
import Help_main from "@/components/help_main.vue";
import Help_aside from "@/components/help_aside.vue";

export default {
  components:{
    Help_main,
    Help_aside
  }
}
</script>

<style scoped>
.help{
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}
.help-aside{
  width: 248px;
  height: 100vh;
  background-color: #D3DCE6;
}
.help-main{
  flex: 1;
}
</style>