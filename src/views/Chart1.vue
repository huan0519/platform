<template>
  <div id="app">
    <el-container>
      <el-main class="main">
        <div class="table-container">
          <table>
            <thead>
            <tr>
              <th>mass</th>
              <th v-for="index in numberOfSamples" :key="index">{{ 'sample' + index }}</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(mass, index) in masses" :key="index">
              <td>{{ mass }}</td>
              <td v-for="sample in numberOfSamples" :key="sample">
                {{ getIntensity(mass) }}
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <el-pagination
            style="float: right;margin: 5px;"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page.sync="currentPage2"
            :page-sizes="[10, 20, 30, 300]"
            :page-size="10"
            layout="sizes, prev, pager, next"
            :total="length">
        </el-pagination>
        <div ref="boxPlotChart" style="width: 1200px; height: 600px;margin-top: 30px"></div>
      </el-main>
      <el-aside width="400px" class="aside">
        <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
        <el-button class="chart-button" @click="handleUpload">提交</el-button>
        <el-upload
            class="upload-demo"
            ref="upload"
            action="https://jsonplaceholder.typicode.com/posts/"
            :auto-upload="false"
            :on-change="handleFileChange"
            :file-list="fileList"><div style="display: flex">
          <button class="sel_button">选择</button>
          <button style="border: none;height: 40px;font-weight: normal;width: 300px;text-align: center;opacity: 0.5;">仅能上传txt,csv,xls,xlsx格式
        </button>
        </div>
        </el-upload>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import * as echarts from 'echarts'; // 引入ECharts
import dataTool from 'echarts/extension/dataTool'; // 引入数据工具

export default {
  data() {
    return {
      masses:'',
      ms_length: 10,
      currentPage1: 5,
      currentPage2: 5,
      currentPage3: 5,
      currentPage4: 4,
      chartInstance: null,
      numberOfSamples: 9, // 可以根据需要调整样本数量
      testSamples: [

      ],
      fileList: []
    };
  },
  created() {
    this.masses = Array.from({ length: this.ms_length }, (_, index) => 61 + index);
  },
  mounted() {
    this.initChart();

  },
  methods: {
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.ms_length = val;
      this.masses = Array.from({ length: this.ms_length }, (_, index) => 61 + index);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
    handleFileChange(file, fileList) {
      this.fileList = fileList;
      if (file.raw) {
        this.readFile(file.raw);
      }
    },
    getIntensity(mass) {
      // 根据mass值来计算intensity，这里只是一个示例，实际逻辑需要根据具体需求来实现
      const sample = this.testSamples.find(sample => sample.mass === mass);
      return sample ? sample.intensity : 0; // 如果找到对应的mass值，返回intensity，否则返回0
    },
    readFile(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const data = e.target.result;
        const workbook = XLSX.read(data, { type: 'array' });
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];
        const json = XLSX.utils.sheet_to_json(worksheet);
        this.columns = Object.keys(json[0]).map(key => ({ key, label: key }));
        this.rows = json;
      };
      reader.readAsArrayBuffer(file);
    },
    handleUpload() {
      this.$refs.upload.submit();
    },
    initChart() {
      // 基于准备好的dom，初始化echarts实例
      this.chartInstance = echarts.init(this.$refs.boxPlotChart);
      // 指定图表的配置项和数据
      const option = {
        title: {
          text: '箱线图示例'
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: {
          type: 'category',
          data: ['sample1', 'sample2', 'sample3'] // 这里可以根据实际数据动态设置
        },
        yAxis: {
          type: 'value',
          splitArea: {
            show: true
          }
        },
        series: [
          {
            name: 'boxplot',
            type: 'boxplot',
            data: [
              [650, 850, 940, 980, 1100], // 这里填写箱线图的数据，格式为[min, Q1, median, Q3, max]
              [690, 900, 950, 1000, 1130],
              [810, 870, 900, 940, 980]
            ],
            tooltip: {
              formatter: function (param) {
                return [
                  '上限: ' + param.data[5],
                  '上四分位数: ' + param.data[4],
                  '中位数: ' + param.data[3],
                  '下四分位数: ' + param.data[2],
                  '下限: ' + param.data[1]
                ].join('<br/>');
              }
            }
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      this.chartInstance.setOption(option);
    }
  }
};
</script>


<style>
.table-container {
  height: auto; /* 可以根据需要调整最大高度 */
  overflow-y: hidden; /* 垂直方向滚动条 */
  display: block; /* 防止默认的inline行为导致水平滚动条不出现 */
  overflow-x: auto;
  margin-right: 10px;
  margin-left: 30px;
}
table {
  width: 1400px;
  border-collapse: collapse;
}

th, td {
  line-height: 40px;
  box-sizing: content-box;
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
  white-space: nowrap;
  font-size: 14px;
}

.aside {
  background-color: #D3DCE6;
  color: #333;
  width: 100vw;
}

.chart-button {
  width: 400px;
  height: 40px;
  text-align: center;
  font-weight: bold;
  border-radius: 30px;
}

.main {
  background-color: #E9EEF3;
  color: #333;
  line-height: 160px;
  overflow: auto;
  height: 100vh;
}

.upload-demo {
  margin-top: 40px;
  margin-left: 3px;
}

.sel_button{
  color: #475669;
  font-weight: bold;
  width: 90px;
  border: none;
  border-radius: 5%;
}
.sel_button:hover{
  cursor: pointer;
  background-color: #CCEEFF;
  color: #00BBFF;
}
</style>