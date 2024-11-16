<template>
  <div id="app">
    <el-container class="el-container">
      <el-main class="main">
        <el-row>
          <el-button-group>
            <el-button
                type="primary"
                :plain="activePage !== 'before'"
                @click="activePage = 'before'"
            >
              处理前
            </el-button>
            <el-button
                type="primary"
                :plain="activePage !== 'after'"
                @click="activePage = 'after'"
            >
              处理后
            </el-button>
          </el-button-group>
        </el-row>

        <el-container v-if="activePage === 'before'" class="table-container">
          <el-table :data="tableData" border>
            <el-table-column v-for="(value, key) in tableData[0]" :key="key" :prop="key" :label="key"></el-table-column>
          </el-table>
          <div style="flex-basis: 100%">
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
          </div>
        </el-container>

        <el-container v-if="activePage === 'after'" >
          <el-main class="main">
            <!--           显示文件内容 -->
            <div  class="table-container">
              <vue-good-table
                  :columns="columns"
                  :rows="paginatedData"
                  :paginate="true"
                  :per-page="perPage"
                  @on-page-change="handlePageChange"
                  :total-rows="totalRows"
                  style="width: 100%; margin-top: 20px;height: auto;  overflow-y: hidden"
                  :pagination-options="{ enabled: true, perPageOptions: [10, 20, 50] }"
              />
            </div>
            <div ref="boxPlotChart" style="width: 1200px; height: 600px;margin-top: 30px"></div>
          </el-main>
        </el-container>


        <div ref="boxPlotChart" style="width: 1200px; height: 600px;margin-top: 30px"></div>
      </el-main>
      <el-aside width="400px" class="aside">
        <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
        <el-button class="chart-button" @click="submitUpload">提交</el-button>
        <el-upload
            class="upload-demo"
            ref="upload"
            action="http://localhost:8000/get_data"
            :auto-upload="false"
            :on-change="handleFileChange"
            :before-upload="beforeUpload"
            :on-success="handleUploadSuccess"
            :on-error="handleUploadError"
            :file-list="fileList"
            accept=".txt,.csv,.xls,.xlsx">
          <div style="display: flex">
            <input class="chart-input" type="file" @change="handleFileUpload" accept=".xlsx, .xls" />
          </div>
          <button
              style="border: none; height: 40px; font-weight: normal; width: 300px; text-align: center; opacity: 0.5;">
            仅能上传txt, csv, xls, xlsx格式
          </button>
        </el-upload>
      </el-aside>
    </el-container>
  </div>
</template>

<script type="module">
import * as XLSX from 'xlsx';
import * as echarts from 'echarts'; // 引入ECharts
import dataTool from 'echarts/extension/dataTool'; // 引入数据工具
import { VueGoodTable } from 'vue-good-table';
import 'vue-good-table/dist/vue-good-table.css';

export default {
  components:{
    VueGoodTable
  },
  data() {
    return {
      activePage: "before",
      tableData: [],
      masses:'',
      ms_length: 10,
      paginatedData: [],
      columns: [],
      perPage: 10, // 每页条数
      totalRows: 0, // 数据总条数，用于分页
      currentPage: 1, // 当前页码
      currentPage1: 5,
      currentPage2: 5,
      currentPage3: 5,
      currentPage4: 4,
      chartInstance: null,
      numberOfSamples: 299, // 可以根据需要调整样本数量
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
    handlePageChange(newPage) {
      this.currentPage = newPage;
      this.loadPaginatedData();
    },
    loadPaginatedData() {
      // 根据 currentPage 和 perPage 获取当前页的数据
      const start = (this.currentPage - 1) * this.perPage;
      const end = start + this.perPage;
      this.paginatedData = this.tableData.slice(start, end);
    },
    handleSizeChange(val) {
      this.ms_length = val;
      this.masses = Array.from({ length: this.ms_length }, (_, index) => 61 + index);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
    submitUpload() {
      console.log('File list:', this.fileList);
      this.$refs.upload.submit();
    },
    beforeUpload(file) {
      const isAcceptedFormat = /\.(txt|csv|xls|xlsx)$/i.test(file.name);
      if (!isAcceptedFormat) {
        this.$message.error('仅支持上传 txt, csv, xls, xlsx 格式的文件');
        return false;
      }
      return true;
    },
    handleUploadSuccess(response) {
      this.$message.success('文件上传成功');
      this.tableData = JSON.parse(response.data); // 假设返回的数据是数组
      this.totalRows = JSON.parse(response.total);
      this.columns = Object.keys(this.tableData[0]).map(key => ({
        label: key,
        field: key
      }));
      console.log('Total Rows:', this.totalRows); // 查看 totalRows 是否为数字
      console.log('Table Data:', this.tableData);  // 查看 tableData 是否有数据
      // 加载第一页数据
      this.loadPaginatedData();
    },
    handleUploadError(err) {
      this.$message.error('文件上传失败');
      console.error('上传失败:', err);
    },
    handleFileUpload(event) {
      const file = event.target.files[0]; // 获取上传的文件
      if (!file) return;

      const reader = new FileReader();

      // 文件加载完成事件
      reader.onload = (e) => {
        try {
          const fileData = new Uint8Array(e.target.result); // 读取文件内容
          const workbook = XLSX.read(fileData, { type: "array" }); // 使用 SheetJS 解析 Excel 数据

          // 确保存在工作表
          if (!workbook.SheetNames || workbook.SheetNames.length === 0) {
            throw new Error("Excel 文件中没有可用的工作表！");
          }

          // 获取第一个工作表
          const sheetName = workbook.SheetNames[0];
          const worksheet = workbook.Sheets[sheetName];

          // 转换工作表内容为 JSON
          const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

          // 确保数据非空
          if (!jsonData || jsonData.length === 0) {
            throw new Error("工作表为空或数据格式错误！");
          }

          // 修改列名：保留第一列原始名称，从第二列开始简化
          const headers = jsonData[0].map((col, index) => {
            return index === 0 ? col : `Col_${index + 1}`;
          });

          // 构建表格数据
          const tableData = jsonData.slice(1).map((row) =>
              headers.reduce((acc, key, i) => ({ ...acc, [key]: row[i] || null }), {})
          );

          // 更新表格数据
          this.tableData = tableData;
        } catch (error) {
          console.error("文件处理出错:", error.message);
          alert("文件处理失败，请检查文件内容是否正确！");
        }
      };

      reader.onerror = () => {
        console.error("文件读取出错！");
        alert("文件读取失败，请重试！");
      };

      reader.readAsArrayBuffer(file); // 以二进制数组格式读取
    },



    handleFileChange(event) {
      // let file = ev.raw;
      // if (!file) return;
      //
      // this.readFile(file).then(data => {
      //   let workbook = xlsx.read(data, { type: "binary" });
      //   console.log(workbook);
      // });

    },
    getIntensity(mass) {
      // 根据mass值来计算intensity，这里只是一个示例，实际逻辑需要根据具体需求来实现
      const sample = this.testSamples.find(sample => sample.mass === mass);
      return sample ? sample.intensity : 0; // 如果找到对应的mass值，返回intensity，否则返回0
    },
    readFile(file) {
      return new Promise((resolve, reject) => {
        let reader = new FileReader();
        reader.readAsBinaryString(file);
        reader.onload = ev => {
          resolve(ev.target.result);
        };
        reader.onerror = err => {
          reject(err);
        };
      });
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
  display: flex block; /* 防止默认的inline行为导致水平滚动条不出现 */
  overflow-x: auto;
  margin-right: 10px;
  margin-left: 30px;
  flex-wrap: wrap;
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
input {
  margin-bottom: 16px;
}
.chart-input{
  width: 200px;
  font-size: 15px;
}
</style>