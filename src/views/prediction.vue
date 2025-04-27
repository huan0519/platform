<template>
  <div id="app">
    <el-container>
      <el-main class="pre-main">
        <p style="justify-self: center; font-weight: bolder" class="glass-text">分析报告</p>
        <el-card style="height: 1200px" v-if="report && Object.keys(report).length > 0">
          <div style="font-size: 14px;">
            <!-- 准确率 -->
            <div v-if="report.accuracy" style="margin-bottom: 8px"><strong>准确率:</strong> {{ report.accuracy }}</div>

            <!-- 预测结果 -->
            <div v-if="report.predictions && report.predictions.length > 0">
              <strong>预测结果:</strong> {{ report.predictions.join(', ') }}
            </div>
            <div v-else>暂无预测结果</div>

            <!-- 混淆矩阵 -->
            <p v-if="report.confusion_matrix && report.confusion_matrix.length > 0">
              <strong>混淆矩阵:</strong>
            </p>
            <el-table v-if="report.confusion_matrix && report.confusion_matrix.length > 0" :data="formatConfusionMatrixData(report.confusion_matrix)" border>
              <el-table-column label="预测\\真实" width="120"></el-table-column>
              <el-table-column
                  v-for="(col, colIndex) in report.confusion_matrix[0]"
                  :key="'col-' + colIndex"
                  :label="'类别 ' + colIndex">
                <template slot-scope="scope">
                  {{ scope.row[`类别 ${colIndex}`] }}
                </template>
              </el-table-column>
            </el-table>

            <!-- 分类报告 -->
            <p v-if="report.classification_report && report.classification_report.length > 0">
              <strong>分类报告:</strong>
            </p>
            <el-table v-if="report.classification_report && report.classification_report.length > 0"
                      :data="formatClassificationReportData(report.classification_report)"
                      border>
              <el-table-column label="类别" prop="类别"></el-table-column>
              <el-table-column label="精准度" prop="精准度"></el-table-column>
              <el-table-column label="召回率" prop="召回率"></el-table-column>
              <el-table-column label="F1得分" prop="F1得分"></el-table-column>
              <el-table-column label="支持度" prop="支持度"></el-table-column>
            </el-table>


            <!-- ROC AUC -->
            <div v-if="report.roc_auc" style="margin-bottom: 8px; margin-top: 15px"><strong>ROC AUC:</strong> {{ report.roc_auc }}</div>

            <!-- 特征重要性 -->
            <div v-if="report.feature_importance.GradientBoosting">
              <strong>GradientBoosting 特征重要性:</strong>
            </div>
            <div ref="gradientBoostingChart" style="width: 100%; height: 300px;"></div>

            <div v-if="report.feature_importance.RandomForest">
              <strong>RandomForest 特征重要性:</strong>
            </div>
            <div ref="randomForestChart" style="width: 100%; height: 300px;"></div>
          </div>
        </el-card>
      </el-main>

      <el-aside width="400px" class="pre-aside">
        <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
        <el-button class="chart-button" @click="submitUpload">提交</el-button>
        <el-upload
            class="upload-demo"
            ref="upload"
            :before-remove="beforeRemove"
            :on-change="handleFileChange"
            :before-upload="beforeUpload"
            :on-success="handleUploadSuccess"
            :on-error="handleUploadError"
            :auto-upload="false"
            :file-list="fileList"
            accept=".txt,.csv,.xls,.xlsx"
        >
          <div style="display: flex">
            <button class="sel_button">选择</button>
            <button style="border: none;height: 40px;font-weight: normal;width: 280px;text-align: center;opacity: 0.5;">仅能上传txt,csv,xls,xlsx格式
            </button>
          </div>
        </el-upload>
        <div>
          <button @click="downloadFile" class="dl_button"><i class="el-icon-download"></i> 下载示例</button>
        </div>
      </el-aside>
    </el-container>
  </div>
</template>


<script>
import axios from 'axios';
import * as echarts from "echarts";

export default {
  data() {
    return {
      fileList: [],
      formData: [],
      report: {},
      options: {
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          data: [],
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [],
          type: 'bar',
          showBackground: true
        }]
      },
    };
  },
  mounted() {
  },
  methods: {
    renderChart(data, chartId) {
      this.chartInstance = echarts.init(this.$refs[chartId]);
      const featureNames = data.map((_, index) => `Feature ${index + 1}`);  // 假设特征名是 Feature 1, Feature 2, ...
      this.options.xAxis.data = featureNames
      this.options.series[0].data = data;
      this.chartInstance.setOption(this.options)
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${file.name}？`);
    },
    handleUploadSuccess(response) {
      // 上传成功后，处理返回的报告数据
      this.report = response.data; // 假设后端返回的是一个JSON对象
      console.log('报告数据:', this.report);
      // 图表渲染在数据返回后进行
      this.$nextTick(() => {
        if (this.report.feature_importance.GradientBoosting) {
          this.renderChart(this.report.feature_importance.GradientBoosting, 'gradientBoostingChart');
        }
        if (this.report.feature_importance.RandomForest) {
          this.renderChart(this.report.feature_importance.RandomForest, 'randomForestChart');
        }
      });
    },
    submitUpload() {
      // 确保 fileList 中有至少两个文件
      if (this.fileList.length < 2) {
        this.$message.warning('请至少选择两个文件');
        return;
      }

      // 获取第一个文件和第二个文件
      const file1 = this.fileList[0].raw;  // 第一个文件
      const file2 = this.fileList[1].raw;  // 第二个文件

      // 创建 FormData 实例
      const formData = new FormData();
      formData.append('file1', file1);
      formData.append('file2', file2);

      // 使用 axios 发送 POST 请求
      axios.post('http://localhost:8000/predict', formData)
          .then(response => {
            // 处理上传成功后的响应
            this.handleUploadSuccess(response);
          })
          .catch(error => {
            this.$message.error('文件上传失败');
            console.error('上传失败:', error);
          });
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
    // 处理单个文件下载的逻辑
    downloadSingleFile(filename) {
      return new Promise((resolve, reject) => {
        axios.get(`http://localhost:8000/download?filename=${filename}`, {
          responseType: 'blob',  // 设置响应类型为 blob（文件）
        })
            .then(response => {
              const blob = response.data;
              const url = window.URL.createObjectURL(blob);
              const link = document.createElement('a');
              link.href = url;
              link.setAttribute('download', filename);  // 设置下载的文件名
              document.body.appendChild(link);
              setTimeout(() => {
                link.click();  // 触发点击事件开始下载
                document.body.removeChild(link);  // 下载完成后清理链接
                resolve();  // 下载完成
              }, 100);  // 延迟一定时间，避免浏览器阻塞
            })
            .catch(error => {
              reject(error);  // 下载失败
            });
      });
    },
    async downloadFile() {
      const filenames = ['训练数据.xlsx', '预测数据.xlsx'];  // 两个需要下载的文件名
      try {
        // 使用 Promise.all 并行下载多个文件
        await Promise.all(filenames.map(filename => this.downloadSingleFile(filename)));
      } catch (error) {
        console.error('Error downloading files:', error);
      }
    },

    // 格式化混淆矩阵数据为适合表格显示的格式
    formatConfusionMatrixData(matrix) {
      return matrix.map((row, rowIndex) => {
        let rowData = {};
        rowData["类别"] = `类别 ${rowIndex}`;
        row.forEach((value, colIndex) => {
          rowData[`类别 ${colIndex}`] = value;
        });
        return rowData;
      });
    },

    // 格式化分类报告为适合表格显示的格式
    formatClassificationReportData(report) {
      return report.map(row => {
        return {
          类别: row[0],
          精准度: row[1],
          召回率: row[2],
          "F1得分": row[3],
          支持度: row[4]
        };
      });
    },

    // 格式化特征重要性为字符串
    formatFeatureImportance(featureImportance) {
      return featureImportance.join(', ');
    }
  }
};
</script>

<style scoped>
.pre-aside {
  background-color: #D3DCE6;
  color: #333;
}

.pre-main {
  background-color: #E9EEF3;
  color: #333;
}

.chart-button {
  width: 380px;
  margin-left: 10px;
  height: 40px;
  text-align: center;
  font-weight: bold;
  border-radius: 30px;
}

.dl_button {
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

.dl_button:hover {
  transform: scale(1.1);
}

.sel_button {
  color: #475669;
  font-weight: bold;
  width: 90px;
  margin-left: 10px;
  border: none;
  border-radius: 5%;
}

.upload-demo {
  margin-top: 40px;
  margin-left: 3px;
}

.sel_button:hover {
  cursor: pointer;
  background-color: #CCEEFF;
  color: #00BBFF;
}
.glass-text {
  font-size: 48px;
  font-weight: bold;
  color: rgba(255, 255, 255, 1);
  text-shadow: 0 4px 10px rgba(0, 0, 0, 0.2), 0 0 10px rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(5px);
}

</style>