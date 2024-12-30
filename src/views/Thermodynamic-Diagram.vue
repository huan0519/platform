<template>
  <el-container style="overflow: hidden">
    <el-main class="main">
      <p style="line-height: 10px;justify-self: center; font-weight: bolder" class="glass-text">热力图</p>
      <div ref="hot_chart" style="justify-self: center" class="glass-container"></div>
    </el-main>
    <el-aside width="400px" class="aside">
      <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
      <el-button class="chart-button" @click="submitUpload">提交</el-button>
      <el-upload
          class="upload-demo"
          ref="upload"
          action="http://localhost:8000/hot_chart"
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
          <button @click="downloadFile" class="dl_button"><i class="el-icon-download"></i> 下载示例</button>
        </div>
      </el-upload>
      <el-divider></el-divider>
      <div style="margin: 20px">
        <p style="line-height: 20px;font-weight: bolder">选择计算相关性的方法</p>
        <el-select style="width: 350px" v-model="value" placeholder="请选择">
          <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
          </el-option>
        </el-select>
      </div>
      <div class="input-container">
        <p style="line-height: 20px;font-weight: bolder">图表样式</p>
        <div class="input-row">
          <label for="chart_title">标题名称:</label>
          <el-input id="chart_title" style="width: 350px" type="text" v-model="chart_title"></el-input>
        </div>
        <div class="input-row">
          <label for="chart_title2">副标题名称:</label>
          <el-input id="chart_title2" style="width: 350px" type="text" v-model="chart_title2"></el-input>
        </div>
      </div>
      <el-divider></el-divider>
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
      uniqueSamples:[],
      heatmapData:[],
      value:'',
      options: [{
        value: '1',
        label: 'pearson'
      },
        {
          value: '2',
          label: 'spearman'
        }],
      option: {
        title:{
          text:'',
          subtext:'',
          left:'center',
        },
        tooltip: {
          position: "top",
          formatter: (params) =>
              `${this.uniqueSamples[params.value[1]]} vs ${this.uniqueSamples[params.value[0]]}: ${params.value[2].toFixed(2)}`,
        },
        xAxis: {
          type: "category",
          data: [],
          splitArea: { show: true },
        },
        yAxis: {
          type: "category",
          data: [],
          splitArea: { show: true },
        },
        visualMap: {
          min: -1,
          max: 1,
          calculable: true,
          orient: "horizontal",
          left: "center",
          bottom: "2%",
        },
        series: [
          {
            name: "Correlation",
            type: "heatmap",
            data: [],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      },
      chartInstance:null,
      chart_title:'',
      chart_title2:'',
    }
  },
  mounted() {
    this.chartInstance = echarts.init(this.$refs.hot_chart);
    // 使用刚指定的配置项和数据显示图表。
    this.chartInstance.setOption(this.option);
  },
  methods: {
    handleUploadSuccess(response) {
      if (response) {
        if(this.value==='1'){
          this.renderHeatmap(response.pearson_matrix);
        }
        else if(this.value==='2'){
          this.renderHeatmap(response.spearman_matrix);
        }
        this.$message.success("数据加载成功");
      } else {
        this.$message.error("返回数据格式有误");
      }
    },
    submitUpload() {
      this.option.title.text = this.chart_title;
      this.option.title.subtext = this.chart_title2;
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
      const filename = '1.xlsx';  // 需要下载的 Excel 文件名
      try {
        // 使用 POST 请求生成并下载 Excel 文件
        const response = await axios.get('http://localhost:8000/download?filename=' + filename, {
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
    },
    renderHeatmap(matrix) {
      this.heatmapData = [];
      // 提取样本编号并排序
      const samples = Object.keys(matrix)
          .map((key) => key.split("-")) // 拆分键名，提取编号
          .flat()
          .map(Number); // 转换为数字
      this.uniqueSamples = [...new Set(samples)].sort((a, b) => a - b); // 去重并按升序排序
      this.uniqueSamples.forEach((sample1, i) => {
        this.uniqueSamples.forEach((sample2, j) => {
          const key = `${sample1}-${sample2}`;
          const value = matrix[key] || matrix[`${sample2}-${sample1}`] || 0;
          this.heatmapData.push([j, i, value]);
        });
      });

      this.option.xAxis.data = this.uniqueSamples;
      this.option.yAxis.data = this.uniqueSamples;
      this.option.series[0].data = this.heatmapData;
      this.chartInstance.setOption(this.option);
    },
  }
}
</script>

<style scoped>
.main {
  background-color: #E9EEF3;
  color: #333;
  overflow: auto;
  height: calc(100vh - 40px); /* 动态计算高度 */
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
  font-size: 40px;
  font-weight: bold;
  color: rgba(255, 255, 255, 1);
  text-shadow: 0 4px 10px rgba(0, 0, 0, 0.2), 0 0 10px rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(5px);
}
.glass-container{
  padding: 15px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  width: 900px;
  height: 550px;
}
</style>
