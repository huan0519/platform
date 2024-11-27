<template>
  <el-container style="overflow: hidden">
    <el-main class="main">
      <p style="line-height: 20px;justify-self: center; font-weight: bolder" class="glass-text">虚线柱状图</p>
      <div ref="line_bar" style="justify-self: center" class="glass-container"></div>
    </el-main>
    <el-aside width="400px" class="aside">
      <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
      <el-button class="chart-button" @click="submitUpload">提交</el-button>
      <el-upload
          class="upload-demo"
          ref="upload"
          action="http://localhost:8000/line_bar"
          :auto-upload="false"
          :on-change="handleFileChange"
          :before-upload="beforeUpload"
          :on-success="handleUploadSuccess"
          :on-error="handleUploadError"
          :file-list="fileList"
          accept=".txt,.csv,.xls,.xlsx"
      >
        <div style="display: flex">
          <button class="sel_button">选择</button>
          <button style="border: none;height: 40px;font-weight: normal;width: 300px;text-align: center;opacity: 0.5;">仅能上传txt,csv,xls,xlsx格式
          </button>
        </div>
        <div>
          <button @click="downloadFile" class="dl_button">下载示例</button>
        </div>
      </el-upload>
      <el-divider></el-divider>
      <div class="input-container">
        <p style="line-height: 40px;font-weight: bolder">图表样式</p>
        <div class="input-row">
          <label for="x_name">x轴名称:</label>
          <el-input id="x_name" style="width: 350px" type="text" v-model="x_name"></el-input>
        </div>
        <div class="input-row">
          <label for="y_name">y轴名称:</label>
          <el-input id="y_name" style="width: 350px" type="text" v-model="y_name"></el-input>
        </div>
        <div class="input-row">
          <label for="chart_title">标题名称:</label>
          <el-input id="chart_title" style="width: 350px" type="text" v-model="chart_title"></el-input>
        </div>
        <div class="input-row">
          <label for="chart_title2">副标题名称:</label>
          <el-input id="chart_title2" style="width: 350px" type="text" v-model="chart_title2"></el-input>
        </div>
        <el-divider></el-divider>
      </div>
    </el-aside>
  </el-container>
</template>

<script>
import * as echarts from "echarts";

export default {
  components: {},
  data() {
    return {
      fileList: [],
      option: {
        backgroundColor: '#0f375f',
        title: {
          left: 'center',
          text: '',
          textColor:{
            color: '#ccc',
          },
          subtext: '',
          subtextColor:{
            color: '#ccc',
          },
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: { type: 'shadow' },
          formatter: function (params) {
            // 过滤掉不需要显示的系列，比如 name 为 'bar' 的系列
            const filteredParams = params.filter(item => !['bar', 'dotted'].includes(item.seriesName));
            let tooltipContent = '';
            filteredParams.forEach(item => {
              tooltipContent += `${item.seriesName}: ${item.value}<br>`;
            });
            return tooltipContent;
          }
        },
        legend: {
          left: 'right',
          data: [],
          textStyle: {
            color: '#ccc'
          }
        },
        xAxis: {
          name:'',
          data: [],
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        yAxis: {
          name:'',
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        series: [
          {
            name: '',
            type: 'line',
            smooth: true,
            showAllSymbol: true,
            symbol: 'emptyCircle',
            symbolSize: 15,
            data: []
          },
          {
            name: '',
            type: 'bar',
            barWidth: 10,
            itemStyle: {
              borderRadius: 5,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#14c8d4' },
                { offset: 1, color: '#43eec6' }
              ])
            },
            data: []
          },
          {
            name: 'bar',
            type: 'bar',
            barGap: '-100%',
            barWidth: 10,
            show:false,
            itemStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgba(20,200,212,0.5)' },
                { offset: 0.2, color: 'rgba(20,200,212,0.2)' },
                { offset: 1, color: 'rgba(20,200,212,0)' }
              ])
            },
            z: -12,
            data: []
          },
          {
            name: 'dotted',
            type: 'pictorialBar',
            symbol: 'rect',
            itemStyle: {
              color: '#0f375f'
            },
            symbolRepeat: true,
            symbolSize: [12, 4],
            symbolMargin: 1,
            z: -10,
            data: []
          }
        ]
      },
      chartInstance:null,
      x_name:'',
      y_name:'',
      chart_title:'',
      chart_title2:'',
    }
  },
  mounted() {
    this.chartInstance = echarts.init(this.$refs.line_bar);
    // 使用刚指定的配置项和数据显示图表。
    this.chartInstance.setOption(this.option);
  },
  methods: {
    handleUploadSuccess(response) {
      const { date, data, data_columns } = response;
      this.option.xAxis.data = date;  // 设置横轴数据
      this.option.legend.data=data_columns; //标签
      this.option.series[0].name=data_columns[1];
      this.option.series[0].data = data[data_columns[1]];// 设置纵轴数据
      this.option.series[1].name=data_columns[0];
      this.option.series[1].data = data[data_columns[0]];
      this.option.series[2].data=data[data_columns[1]];
      this.option.series[3].data=data[data_columns[1]];
      // 使用新的配置项和数据更新图表
      this.chartInstance.setOption(this.option);
    },
    submitUpload() {
      this.option.xAxis.name=this.x_name;
      this.option.yAxis.name=this.y_name;
      this.option.title.text=this.chart_title;
      this.option.title.subtext=this.chart_title2;
      // 使用新的配置项和数据更新图表
      this.chartInstance.setOption(this.option);
      this.$refs.upload.submit(); // 提交上传
    },
    beforeUpload(file) {
      const isAcceptedFormat = /\.(txt|csv|xls|xlsx)$/i.test(file.name);
      if (!isAcceptedFormat) {
        this.$message.error('仅支持上传 txt, csv, xls, xlsx 格式的文件');
        return false;
      }
      return true;
    },
    handleFileChange(file, fileList) {
      this.fileList = fileList;
    },
    handleUploadError(err) {
      this.$message.error('文件上传失败');
      console.error('上传失败:', err);
    },
    async downloadFile() {
      const filename = '5.xlsx';  // 需要下载的 Excel 文件名
      try {
        // 使用 POST 请求生成并下载 Excel 文件
        const response = await axios.get('http://localhost:8000/download?filename='+filename, {
          responseType: 'blob',  // 设置响应类型为 blob（文件）
        });

        // 获取返回的文件内容
        const blob = response.data;
        // 创建临时的下载链接
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', '示例数据');  // 设置下载的文件名
        document.body.appendChild(link);
        link.click();  // 触发点击事件开始下载
        document.body.removeChild(link);  // 下载完成后清理链接
      } catch (error) {
        console.error('Error downloading file:', error);
      }
    }
  }
}
</script>

<style scoped>
.main {
  background-color: #E9EEF3;
  color: #333;
  line-height: 160px;
  overflow: auto;
  height: 100vh;
}
.aside {
  background-color: #D3DCE6;
  color: #333;
  width: 100vw;
  overflow: hidden;
}
.input-container {
  margin: 20px;
}

.input-row {
  display: flex;
  align-items: center;
  margin-bottom: 15px; /* 添加一些间距 */
}

.input-row label {
  margin-right: 10px; /* label 与输入框之间的间距 */
  width: 120px; /* 固定标签宽度 */
}

.input-row el-input {
  flex: 1; /* 使输入框占用剩余空间 */
}
.chart-button{
  width: 400px;
  height: 40px;
  text-align: center;
  font-weight: bold;
  border-radius: 30px;
}
.sel_button{
  color: #475669;
  font-weight: bold;
  width: 90px;
  border: none;
  border-radius: 5%;
}
.upload-demo {
  margin-top: 40px;
  margin-left: 3px;
}
.sel_button:hover{
  cursor: pointer;
  background-color: #CCEEFF;
  color: #00BBFF;
}
.dl_button{
  background: linear-gradient(45deg, #ff007f, #007fff, #7fff00);
  background-size: 200% 200%;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  animation: gradient-move 2s infinite;
  transition: transform 0.2s ease-in-out;
  float: right;
  margin-right: 20px;
  margin-top: 20px;
}
.dl_button:hover{
  transform: scale(1.1);
}
@keyframes dl_button-move {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.glass-text {
  font-size: 48px;
  font-weight: bold;
  color: rgba(255, 255, 255, 1);
  text-shadow: 0 4px 10px rgba(0, 0, 0, 0.2), 0 0 10px rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(5px);
}
.glass-container{
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  width: 1000px;
  height: 600px;
}
</style>
