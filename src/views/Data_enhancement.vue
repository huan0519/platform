<template>
  <div id="app">
    <el-container class="el-container">
      <el-main class="main">
        <el-row style="height: 150px;margin-left: 30px">
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
        <div>
          <el-container v-if="activePage === 'before'" class="table-container">
            <el-pagination
                style="float: left;flex-basis: 100%;padding: 0;margin-bottom: 10px;height: 20px"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page.sync="currentPage"
                :page-sizes="[10, 20, 30, 50]"
                :page-size="pageSize"
                :hide-on-single-page="true"
                layout=" sizes"
                :total="total">
            </el-pagination>
            <el-table :data="paginatedTableData" border style="flex-basis: 100%;margin-top: 1px;">
              <el-table-column
                  v-for="(value, key) in tableData[0] || {}"
                  :key="key"
                  :prop="key"
                  :label="key">
              </el-table-column>
            </el-table>
            <div style="flex-basis: 100%">
              <el-pagination
                  style="float: right;padding: 4px;margin-top: 15px;flex-basis: 100%;"
                  @size-change="handleSizeChange"
                  @current-change="handleCurrentChange"
                  :current-page.sync="currentPage"
                  :page-sizes="[10, 20, 30, 50]"
                  :page-size="pageSize"
                  :hide-on-single-page="true"
                  layout="total ,prev, pager, next"
                  :total="total">
              </el-pagination>
            </div>
          </el-container>
        </div>
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
            :on-change="handleFileUpload"
            :before-upload="beforeUpload"
            :on-success="handleUploadSuccess"
            :on-error="handleUploadError"
            :file-list="fileList"
            accept=".txt,.csv,.xls,.xlsx">
          <div>
            <el-button class="sel_button">选择文件</el-button>
            <button
                style="border: none; height: 40px; font-weight: normal; width: 300px; text-align: center; opacity: 0.5;">
              仅能上传txt, csv, xls, xlsx格式
            </button>
          </div>
        </el-upload>
      </el-aside>
    </el-container>
  </div>
</template>

<script type="module">
import * as XLSX from 'xlsx';
import * as echarts from 'echarts'; // 引入ECharts
// import dataTool from 'echarts/extension/dataTool'; // 引入数据工具
import { VueGoodTable } from 'vue-good-table';
import 'vue-good-table/dist/vue-good-table.css';

export default {
  components:{
    VueGoodTable
  },
  data() {
    return {
      paginatedTableData: [], // 当前页显示的数据
      pageSize: 10, // 每页条数
      total: 0, // 数据总量
      currentPage: 1,
      length:'',
      activePage: "before",
      tableData:[],
      selectedFile: null,  // 当前选中文件
      paginatedData: [],
      columns: [],
      perPage: 10,
      totalRows: 0,
      chartInstance: null,
      fileList: []
    };
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
    updatePaginatedData() {
      // 根据当前页和每页行数计算显示数据的范围
      const start = (this.currentPage - 1) * this.pageSize;
      const end = start + this.pageSize;
      console.log("111");
      // 更新当前页数据
      this.paginatedTableData = this.tableData.slice(start, end);

      // 更新总行数
      this.total = this.tableData.length;
    },
    handleSizeChange(newSize) {
      // 每页行数改变时，更新当前页码和显示数据
      this.pageSize = newSize;
      this.currentPage = 1; // 每页行数调整后从第一页重新开始
      this.updatePaginatedData();
    },
    handleCurrentChange(newPage) {
      // 页码改变时，更新当前页数据
      this.currentPage = newPage;
      this.updatePaginatedData();
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
    handleUploadError(err) {
      this.$message.error('文件上传失败');
      console.error('上传失败:', err);
    },
    handleFileUpload(file) {
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
            return index === 0 ? col : `Sample_${index + 0}`;
          });

          // 构建表格数据
          const tableData = jsonData.slice(1).map((row) =>
              headers.reduce((acc, key, i) => ({ ...acc, [key]: row[i] || null }), {})
          );

          // 更新表格数据
          this.tableData = tableData;
          this.updatePaginatedData();
        } catch (error) {
          console.error("文件处理出错:", error.message);
          alert("文件处理失败，请检查文件内容是否正确！");
        }
      };

      reader.onerror = () => {
        console.error("文件读取出错！");
        alert("文件读取失败，请重试！");
      };

      reader.readAsArrayBuffer(file.raw); // 以二进制数组格式读取
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
  },
};
</script>


<style scoped>
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
  line-height: 20px;
  box-sizing: content-box;
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
  white-space: nowrap;
  font-size: 14px;
  text-overflow: ellipsis; /* 超出部分显示省略号 */
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