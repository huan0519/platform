<!--数据加强-->
<template>
    <el-container class="el-container" style="display: flex">
      <el-main class="main">
        <el-row style="height: 70px;margin-left: 30px;width: 100%;">
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
        <div style="width: 100%">
          <el-container v-if="activePage === 'before'" class="table-container">
            <el-pagination
                style="float: left;flex-basis: 100%;padding: 0;margin-bottom: 10px;height: 20px"
                @size-change="handleSizeChange1"
                @current-change="handleCurrentChange1"
                :current-page.sync="currentPage1"
                :page-sizes="[10, 20, 50, 100]"
                :page-size="pageSize1"
                layout=" sizes"
                :total="total1">
            </el-pagination>
            <el-table :data="paginatedTableData" :default-sort = "{prop: 'date', order: 'descending'}" border style="flex-basis: 100%;margin-top: 1px;">
              <el-table-column
                  v-for="(value, key) in tableData1[0] || {}"
                  :key="key"
                  :prop="key"
                  :label="key"
                  align="center"
                  sortable
              >
              </el-table-column>
            </el-table>
            <div style="flex-basis: 100%">
              <el-pagination
                  style="float: right;padding: 4px;margin-top: 15px;flex-basis: 100%;"
                  @size-change="handleSizeChange1"
                  @current-change="handleCurrentChange1"
                  :current-page.sync="currentPage1"
                  :page-sizes="[10, 20, 50, 100]"
                  :page-size="pageSize1"
                  layout="total, prev, pager, next, jumper"
                  :total="total1">
              </el-pagination>
            </div>
          </el-container>
        </div>
        <div v-show="activePage==='before'">
          <div class="glass-container">
            <div ref="box_chart" style="width: 1000px; height: 600px;"></div>
          </div>
        </div>
        <div style="width: 100%">
          <el-container v-if="activePage === 'after'" class="table-container">
            <el-pagination
                background
                layout="sizes"
                :page-size="perPage"
                :page-sizes="[10, 20, 50, 100]"
                :current-page.sync="currentPage"
                :total="totalRows"
                @current-change="handlePageChange"
                @size-change="handleSizeChange"
                style="float: left;flex-basis: 100%;padding: 0;margin-bottom: 10px;height: 20px"
            />
            <!-- 表格显示 -->
            <el-table :data="tableData" :default-sort = "{prop: 'date', order: 'descending'}" border style="flex-basis: 100%;margin-top: 1px;">
              <!-- 动态生成表头 -->
              <el-table-column
                  v-for="col in columns"
                  :key="col.field"
                  :label="col.label"
                  :prop="col.field.toString()"
                  align="center"
                  sortable
              />
            </el-table>
            <!-- 分页组件 -->
            <div style="flex-basis: 100%">
              <el-pagination
                  background
                  layout="total, prev, pager, next, jumper"
                  :page-size="perPage"
                  :page-sizes="[10, 20, 50, 100]"
                  :current-page.sync="currentPage"
                  :total="totalRows"
                  @current-change="handlePageChange"
                  @size-change="handleSizeChange"
                  style="float: right;padding: 4px;margin-top: 15px;flex-basis: 100%;"
              />
            </div>
          </el-container>
        </div>
        <div v-show="activePage==='after'">
          <div class="glass-container">
           <div ref="hot_chart" style="width: 900px;height: 600px"></div>
          </div>
        </div>
      </el-main>
      <el-aside width="400px" class="aside">
        <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
        <el-button class="chart-button" @click="submitUpload">提交</el-button>
        <div class="upload-demo">
          <el-button @click="dialogVisible = true" class="sel_button">选择文件</el-button>
          <button
              style="border: none; height: 40px; font-weight: normal; width: 280px; text-align: center; opacity: 0.5;">
            仅能上传txt, csv, xls, xlsx格式
          </button>
        </div>
        <el-dialog
            title="数据降维"
            :visible.sync="dialogVisible"
            width="40%"
            :before-close="handleClose">
          <el-upload
              drag
              action="https://jsonplaceholder.typicode.com/posts/"
              :auto-upload="false"
              :on-change="handleFileUpload"
              :before-upload="beforeUpload"
              :file-list="fileList"
              accept=".txt,.csv,.xls,.xlsx"
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          </el-upload>
          <div style="margin-top: 10px">
            <span style="font-size: medium">数据来源：</span>
            <el-input style="width: 350px" v-model="data_source" placeholder="请输入内容"></el-input>
          </div>
          <div style="margin-top: 10px">
            <span style="font-size: medium">是否保存结果：</span>
            <el-radio v-model="radio" label="1">是</el-radio>
            <el-radio v-model="radio" label="2">否</el-radio>
          </div>
          <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="read_file">确 定</el-button>
        </span>
        </el-dialog>
        <div>
          <button @click="downloadFile" class="dl_button"><i class="el-icon-download"></i> 下载示例</button>
        </div>
      </el-aside>
    </el-container>
</template>

<script type="module">
import * as XLSX from 'xlsx';
import * as echarts from 'echarts'; // 引入ECharts
// import dataTool from 'echarts/extension/dataTool'; // 引入数据工具

export default {
  components:{
  },
  data() {
    return {
      paginatedTableData: [], // 当前页显示的数据
      pageSize1: 10, // 每页条数
      total1: 0, // 数据总量
      currentPage1: 1,
      length:'',
      activePage: "before",
      tableData1:[],
      selectedFile: null,  // 当前选中文件
      chartInstance1: null,
      chartInstance2:null,
      fileList: [],
      file:"",
      formData:{},
      tableData: [], // 用于存储完整的表格数据
      columns: [],
      perPage: 10, // 每页条数
      totalRows: 0, // 数据总条数，用于分页
      currentPage: 1, // 当前页码
      force_update:0,
      hot_option: {
        tooltip: {
          position: "top",
          formatter: (params) =>
              `${this.hot_option.xAxis.data[params.value[0]]} 对 ${this.hot_option.yAxis.data[params.value[1]]}: ${params.value[2].toFixed(2)}`,
        },
        xAxis: {
          type: "category",
          data: [], // 原始特征名
          splitArea: { show: true },
        },
        yAxis: {
          type: "category",
          data: [], // 主成分列
          splitArea: { show: true },
        },
        visualMap: {
          min: 0,
          max: 1,
          calculable: true,
          orient: "horizontal",
          left: "center",
          bottom: "2%",
        },
        series: [
          {
            name: "Loadings Matrix",
            type: "heatmap",
            data: [], // 热图的数据格式 [x, y, value]
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      },
      box_option: {
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
      dialogVisible:false,
      data_source:"",
      radio:'1',
    };
  },
  mounted() {
    this.chartInstance1 = echarts.init(this.$refs.box_chart);
    this.chartInstance1.setOption(this.box_option);
    this.chartInstance2 = echarts.init(this.$refs.hot_chart);
    this.chartInstance2.setOption(this.hot_option);
  },
  methods: {
    updatePaginatedData() {
      // 根据当前页和每页行数计算显示数据的范围
      const start = (this.currentPage1 - 1) * this.pageSize1;
      const end = start + this.pageSize1;
      // 更新当前页数据
      this.paginatedTableData = this.tableData1.slice(start, end);

      // 更新总行数
      this.total1 = this.tableData1.length;
    },
    handleSizeChange1(newSize) {
      // 每页行数改变时，更新当前页码和显示数据
      this.pageSize1 = newSize;
      this.currentPage1 = 1; // 每页行数调整后从第一页重新开始
      this.updatePaginatedData();
    },
    handleCurrentChange1(newPage) {
      // 页码改变时，更新当前页数据
      this.currentPage1 = newPage;
      this.updatePaginatedData();
    },
    handlePageChange(newPage) {
      this.force_update=0;
      this.currentPage = newPage;
      this.fetchData(); // 请求新分页数据
    },
    handleSizeChange(pagesize) {
      console.log(pagesize);
      this.force_update=0;
      this.perPage = pagesize;
      this.fetchData();
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
    // 页面加载时请求第一页数据
    fetchData() {
      console.log(this.force_update)
      const params = {
        page: this.currentPage,
        per_page: this.perPage,
        force_update: this.force_update,
      };
      axios
          .post(
              `http://localhost:8000/pca`,
              this.formData, // 包括分页数据和文件
              {
                headers: {
                  "Content-Type": "multipart/form-data",
                },
                params: params,
              }
          )
          .then((response) => {
            const data = response.data;
            if (data.columns && data.rows) {
              // 转换列定义
              this.columns = data.columns.map((col) => ({
                label: col.toString(), // 确保是字符串
                field: col.toString(), // 确保是字符串
              }));
              // 转换行数据为对象数组
              this.tableData = data.rows.map((row) => {
                const rowData = {};
                data.columns.forEach((col, index) => {
                  rowData[col] = row[index];
                });
                return rowData;
              });

              this.totalRows = data.total; // 更新总条数
            } else {
              this.$message.error("后端返回数据格式错误");
            }
            if(this.force_update===1){
              if (data.loadings_matrix && data.features) {
                const loadingsMatrix = data.loadings_matrix;

                // 使用原始特征名 (features) 初始化 X 轴
                this.hot_option.xAxis.data = data.features;

                // 使用主成分 (PC1, PC2, ...) 初始化 Y 轴
                this.hot_option.yAxis.data = data.columns.slice(1); // 跳过 'id'

                // 格式化 loadings_matrix 为热图需要的 [xIndex, yIndex, value] 数据
                this.hot_option.series[0].data = loadingsMatrix.flatMap((row, rowIndex) =>
                    row.map((value, colIndex) => [colIndex, rowIndex, value]) // 确保数据的每个值都能被遍历
                );

                console.log(this.hot_option.series[0].data);

                // 更新热图
                this.chartInstance2.setOption(this.hot_option);
                this.$message.success("热图已生成！");
              } else {
                this.$message.error("后端返回数据格式错误！");
              }
            }
          })
          .catch((err) => {
            console.error("数据加载失败:", err);
            this.$message.error("数据加载失败");
          });
    },
    submitUpload() {
      const len = this.fileList.length;
      if (len === 0) {
        this.$message.warning('请先选择文件');
        return;
      }
      const formData = new FormData();
      formData.append("file", this.fileList[len - 1].raw);
      this.formData = formData;
      this.force_update=1;
      this.fetchData();
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
    initBoxplot(){
      const params = {
        box_update: 1,
      };
      axios
          .post(
              `http://localhost:8000/boxplot`,
              this.formData, // 包括分页数据和文件
              {
                headers: {
                  "Content-Type": "multipart/form-data",
                },
                params: params,
              }
          )
          .then((response) => {
            const { columns, boxplot_data } = response.data;
            // 更新数据到图表
            this.box_option.series[0].data = boxplot_data; // 设置箱线图数据
            this.box_option.xAxis.data = columns; // 设置 X 轴分类标签
            // 使用新的配置项和数据更新图表
            this.chartInstance1.setOption(this.box_option);
          })
    },
    handleFileUpload(file,filelist) {
      this.file=file;
      this.fileList = filelist;
      const len = this.fileList.length;
      if (len === 0) {
        this.$message.warning('请先选择文件');
        return;
      }
      const formData = new FormData();
      formData.append("file", this.fileList[len - 1].raw);
      this.formData = formData;

    },
    read_file(){
      this.dialogVisible = false;
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
          console.log(jsonData)
          // 修改列名：保留第一列原始名称，从第二列开始简化
          const headers = jsonData[0].map((col, index) => {
            return index === 0 ? col : `Sample_${index + 0}`;
          });

          // 构建表格数据
          const tableData = jsonData.slice(1).map((row) =>
              headers.reduce((acc, key, i) => ({ ...acc, [key]: row[i] || null }), {})
          );

          // 更新表格数据
          this.tableData1 = tableData;
          console.log(this.tableData1);
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

      reader.readAsArrayBuffer(this.file.raw); // 以二进制数组格式读取
      this.initBoxplot();
    },
    async downloadFile() {
      const filename = 'pca.xlsx';  // 需要下载的 Excel 文件名
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
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
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
.chart-button {
  width: 380px;
  margin-left: 10px;
  height: 40px;
  text-align: center;
  font-weight: bold;
  border-radius: 30px;
}

.main {
  background-color: #E9EEF3;
  color: #333;
  line-height: 70px;
  overflow-y: auto;
  overflow-x: hidden;
  height: calc(100vh - 60px); /* 假设顶部按钮占150px */
  align-items: center;
  justify-items: center;
  padding: 20px;
  flex: 1;
}

.upload-demo {
  margin-top: 40px;
  margin-left: 3px;
}

.sel_button{
  color: #475669;
  font-weight: bold;
  width: 90px;
  margin-left: 10px;
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
.glass-container{
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  width: 900px;
  height: 600px;
  display: flex;
  align-items: center;
  justify-items: center;
}

</style>
