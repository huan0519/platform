<!--数据预处理-->
<template>
  <div style="height: 100vh;margin-left: 18px">
    <header style="margin-top: 1em">
      <a style="margin: 55px;font-size: 28px;font-style: italic;font-weight: bolder">数据前处理</a>
    </header>
    <el-divider></el-divider>
    <div class="ant-row">
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart1"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%;">
              <img src="../../public/image/a.jpg" @click="GoToPage('data_normalization')" style="height: 100%;width: 100%;box-sizing: border-box;">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">数据归一化</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart2"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/b.jpg" @click="GoToPage('reinforce')" class="block-hold" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">补值</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart3"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/c.jpg" @click="GoToPage('alignment')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">数据对齐</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px;background: #334155;border-radius: 20px">
          <a id="chart4"></a>
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/d.jpg" @click="GoToPage('data_enhancement')" style="height: 100%;width: 100%;box-sizing: border-box">
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
  min-height: 100vh;
}
.ant-row{
  box-sizing: border-box;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.ant-row-line{
  box-sizing: border-box;
  min-width: 248px;
}
.ant-card-hover{
  cursor: pointer;
  transition: box-shadow 0.1s ease-in-out;
}

</style>
