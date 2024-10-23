<template>
  <div id="app" style="height: 100vh">
    <header style="margin-top: 1em">
      <a style="margin: 10em;font-size: 20px;font-style: italic">数据前处理</a>
    </header>
    <el-divider></el-divider>
    <div class="ant-row">
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: darkgrey">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%">
              <img src="../../public/image/a.png" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center">数据归一化</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: darkgrey">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%">
              <img src="../../public/image/b.png" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center">补值</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: darkgrey">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%">
              <img src="../../public/image/b.png" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center">补值</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: darkgrey">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%">
              <img src="../../public/image/b.png" style="height: 100%;width: 100%;box-sizing: border-box">
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
body{
  min-width: 100vw;
}
.ant-row{
  box-sizing: border-box;
  display: block flex;
  position: relative;
  overflow-x: hidden;
  flex-wrap: wrap;
}

.ant-row-line{
  padding-left: 10px;
  padding-right: 10px;
  width: calc(25% - 20px);
  min-width: 220px;
}
.ant-card-hover{
  cursor: pointer;
  transition: box-shadow 0.3s ease-in-out;
}
.ant-card-hover:hover{
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}
</style>
