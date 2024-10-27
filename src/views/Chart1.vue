<template>
  <div>
    <el-container>
      <el-main class="main">
        <div class="table-container">
          <table class="chart-table">
            <thead>
            <tr>
              <th v-for="column in columns" :key="column.key" class="table-header">{{ column.label }}</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="row in rows" :key="row.name" class="table-row">
              <td v-for="column in columns" :key="column.key" class="table-cell">{{ row[column.key] }}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </el-main>
      <el-aside width="400px" class="aside">
        <p style="margin: 10px">控制台</p>
        <el-button class="chart-button" @click="handleUpload">提交</el-button>
        <el-upload
            class="upload-demo"
            ref="upload"
            action="https://jsonplaceholder.typicode.com/posts/"
            :auto-upload="false"
            :on-change="handleFileChange"
            :file-list="fileList">
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">仅能上传txt,csv,xls,xlsx格式</div>
        </el-upload>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import * as XLSX from 'xlsx';

export default {
  data() {
    return {
      columns: [],
      rows: [],
      fileList: []
    };
  },
  methods: {
    handleFileChange(file, fileList) {
      this.fileList = fileList;
      if (file.raw) {
        this.readFile(file.raw);
      }
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
    }
  }
}
</script>

<style>
.chart-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed; /* 使表格布局固定 */
}

.table-container {
  overflow: auto;
  max-height: 600px;
  margin-right: 10px;
  margin-left: 30px;
}

.aside {
  background-color: #D3DCE6;
  color: #333;
}

.chart-button {
  width: 340px;
  height: 40px;
}

.main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

.upload-demo {
  margin-top: 20px;
  margin-right: 20px;
}

.table-header {
  background-color: #42b983;
  color: white;
  box-sizing: border-box; /* 边框盒模型 */
  width: 150px; /* 设置固定宽度 */
  height: 30px; /* 设置固定高度 */
}

.table-row {
  background-color: #f9f9f9;
}

.table-cell, .table-header {
  border: 1px solid #ddd;
  padding: 1px;
  font-size: 15px;
  text-align: center;
  box-sizing: border-box; /* 边框盒模型 */
  width: 200px; /* 设置固定宽度 */
  height: 30px; /* 设置固定高度 */
}

.table-row:nth-child(even) {
  background-color: #f2f2f2;
}
</style>