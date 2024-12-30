<!--应用统计-->
<template>
  <div id="app" class="app-body">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>应用统计</span>
        <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
      </div>
      <div v-for="o in 4" :key="o" class="text item">
        {{'列表内容 ' + o }}
      </div>
    </el-card>
  </div>
</template>

<script>


export default {
  components:{

  }
}
</script>


<style>
.app-body{
  display: flex;
  justify-content: center;
  align-items: center;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}

.box-card {
  width: 980px;
  height: 800px;
}

</style>