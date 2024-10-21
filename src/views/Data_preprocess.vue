<template>
  <div id="app" style="height: 100%">
    <header style="margin-top: 1em">
      <a style="margin: 10em;font-size: 20px;font-style: italic">数据前处理</a>
    </header>
    <el-divider></el-divider>
    <div class="ant-row" style="margin-left: -15px;margin-right: -15px">
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: rgb(239,241,245)">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%">
              <img src="../../public/image/a.png" style="height: 100%;width: 100%;object-fit: contain">
            </div>
          </div>
          <p style="text-align: center">数据归一化</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: rgb(239,241,245)">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%">
              <img src="../../public/image/b.png" style="height: 100%;width: 100%;object-fit: contain">
            </div>
          </div>
          <p style="text-align: center">补值</p>
        </main>
      </div>
    </div>

  </div>
</template>

<script>

</script>

<style>
.ant-row{
  display: block flex;
  zoom: 1;
  position: relative;
}
.ant-row-line{
  padding-left: 15px;
  padding-right: 15px;
  width: 25%;
}
.ant-card-hover{
  cursor: pointer;
}
</style>
