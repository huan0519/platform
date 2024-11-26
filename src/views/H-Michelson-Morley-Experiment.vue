<template>
  <el-container>
    <el-main class="main">
      <p style="line-height: 20px; margin-left:20px; font-weight: bolder">箱线图</p>
      <div ref="boxplot" style="width: 830px; height: 550px"></div>
    </el-main>
    <el-aside width="400px" class="aside">
      <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
      <el-button class="chart-button" @click="submitUpload">提交</el-button>
      <el-upload
          class="upload-demo"
          ref="upload"
          action="http://localhost:8000/boxplot"
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
      </el-upload>
      <div>
        <button @click="downloadFile">下载示例</button>
      </div>
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
        title: {
          text: '',
          subtext: '',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        grid: {
          left: '10%',
          right: '10%',
          bottom: '15%'
        },
        xAxis: {
          type: 'category',
          data: [],
          boundaryGap: true,
          nameGap: 30,
          splitLine: { show: false },
          axisLabel: {
            formatter: function (value) {
              return value;
            }
          }
        },
        yAxis: {
          type: 'value',
          splitLine: { show: true }
        },
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: 0,
            start: 10,
            end: 100
          },
          {
            type: 'slider',
            xAxisIndex: 0,
            bottom: 10,
            start: 10,
            end: 100
          }
        ],
        series: [
          {
            type: "boxplot",
            data: [], // 使用后端返回的箱线图数据
          },
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
    this.chartInstance = echarts.init(this.$refs.boxplot);
    // 使用刚指定的配置项和数据显示图表。
    this.chartInstance.setOption(this.option);
  },
  methods: {
    handleUploadSuccess(response) {
      const { columns, boxplot_data } = response;
      // 更新数据到图表
      this.option.series[0].data = boxplot_data; // 设置箱线图数据
      this.option.xAxis.data = columns; // 设置 X 轴分类标签
      // 使用新的配置项和数据更新图表
      this.chartInstance.setOption(this.option);
    },
    async submitUpload() {
      this.option.xAxis.name=this.x_name;
      this.option.yAxis.name=this.y_name;
      this.option.title.text=this.chart_title;
      this.option.title.subtext=this.chart_title2;
      // 使用新的配置项和数据更新图表
      this.chartInstance.setOption(this.option);
      await this.$refs.upload.submit(); // 提交上传
      this.$message.success("图表更新成功");
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
      const filename = '9.xlsx';  // 需要下载的 Excel 文件名
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
  overflow: auto;
  height: calc(100vh - 40px); /* 动态计算高度 */
}
.aside {
  background-color: #D3DCE6;
  color: #333;
  width: 100vw;
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

</style>
