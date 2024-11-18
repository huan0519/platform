<template>
  <div id="app" style="height: 100vh">
    <header style="margin-top: 1em">
      <a style="margin: 55px;font-size: 28px;font-style: italic;font-weight: bolder">数据前处理</a>
    </header>
    <el-divider></el-divider>
    <div class="ant-row">
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%;">
              <img src="../../public/image/a.png" @click="GoToPage('data_normalization')" style="height: 100%;width: 100%;box-sizing: border-box;">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">数据归一化</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart2"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/b.png" class="block-hold" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">补值</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart3"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/b.png" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">数据对齐</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart4"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/b.png" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">数据增强（PCA）</p>
        </main>
      </div>
    </div>

  </div>
</template>

<script>
export default {


  methods:{
    GoToPage(page) {
      this.$router.push(page)
    }
  }
}
</script>

<style>
body{
  min-width: 100vw;
  overflow: hidden;
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
  transition: box-shadow 0.25s ease-in-out;
}
.ant-card-hover:hover{
  box-shadow: 0 8px 8px rgba(0, 0, 0, 1);
  border-top: 1mm double #334155;
}
</style>
