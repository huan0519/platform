<!--数据可视化模块-->
<template>
  <div style="height: 100vh">
    <header style="margin-top: 1em">
      <a style="margin: 55px;font-size: 28px;font-style: italic;font-weight: bolder">数据可视化</a>
    </header>
    <el-divider></el-divider>
    <div class="ant-row" style="">
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Stacked-Line.png" @click="GoToPage('stacked_line')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">堆叠折线图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Stacked-Bar-Chart.png" @click="GoToPage('stacked_barchart')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">堆叠柱状图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Rose.png" @click="GoToPage('rose')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">玫瑰图 </p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Scatter-Diagram.png" @click="GoToPage('scatter_diagram')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">散点图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Michelson-Morley-Experiment.png" @click="GoToPage('michelson')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">箱线图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Large-Area-Chart.png" @click="GoToPage('large-area-chart')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">大数据折线图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/H-Michelson-Morley-Experiment.png" @click="GoToPage('H_michelson')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">大数据量箱线图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Thermodynamic-Diagram.png" @click="GoToPage('thermodynamic')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">热力图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/Dashed-Bar-Chart.png" @click="GoToPage('dashed-bar-chart')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">虚线柱状图</p>
        </main>
      </div>
      <div class="ant-row-line">
        <main class="shadow" style="padding: 24px 0 0 0;margin: 0;min-height: 248px; min-width: 248px;background: #334155;border-radius: 20px">
          <div class="ant-card-hover" style="width: 100%;height: 220px;overflow: hidden">
            <div class="ant-body" style="padding: 0;height: 100%;width: 98%;margin-left: 1%">
              <img src="../../public/image/3D.png" @click="GoToPage('3D')" style="height: 100%;width: 100%;box-sizing: border-box">
            </div>
          </div>
          <p style="text-align: center;color: #E9EEF3">3D柱状图</p>
        </main>
      </div>
    </div>
  </div>

</template>

<script>

export default{
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
}
.ant-row{
  box-sizing: border-box;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.ant-row-line{
  padding-left: 10px;
  padding-right: 10px;
  width: calc(25% - 20px);
}
.shadow{
  cursor: pointer;
  transition: box-shadow 0.3s ease-in-out;
}
.shadow:hover{
  box-shadow: 0 4px 8px rgba(0, 0, 0, 1);
  border-radius: 5%;
}
</style>