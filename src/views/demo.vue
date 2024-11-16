<template>
  <div>
    <!-- 上传组件 -->
    <el-upload
        class="upload-demo"
        action="#"
        :http-request="uploadFile"
        :on-change="handleChange"
        :file-list="fileList"
    >
      <el-button size="small" type="primary">点击上传</el-button>
      <div slot="tip" class="el-upload__tip">只能上传xlsx文件</div>
    </el-upload>

    <!-- 动态表格 -->
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="mass" label="Mass" width="180"></el-table-column>
      <el-table-column v-for="sample in samples" :key="sample" :prop="sample" :label="sample"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import XLSX from 'xlsx'; // 引入xlsx库

export default {
  data() {
    return {
      fileList: [],
      tableData: [],
      samples: [],
    };
  },
  methods: {
    // 上传文件
    uploadFile(file) {
      const formData = new FormData();
      formData.append('file', file.file);
      // 这里可以发送请求到后端，或者直接在前端处理
      this.readFile(file.file);
    },
    // 处理文件读取
    readFile(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const data = e.target.result;
        const workbook = XLSX.read(data, { type: 'array' });
        const sheetName = workbook.SheetNames[0];
        const sheet = workbook.Sheets[sheetName];
        this.processSheet(sheet);
      };
      reader.readAsArrayBuffer(file);
    },
    // 处理工作表
    processSheet(sheet) {
      const headers = this.getHeaders(sheet);
      const data = this.getData(sheet);
      this.samples = headers.slice(1);
      this.tableData = data.map((row, index) => {
        const obj = { mass: row[0] };
        this.samples.forEach((sample, i) => {
          obj[sample] = row[i * 2 + 1]; // 每两列代表一个sample的mass值和intensity值
        });
        return obj;
      });
    },
    // 获取表头
    getHeaders(sheet) {
      const headers = [];
      const range = XLSX.utils.decode_range(sheet['!ref']);
      for (let i = 0; i < range.e.c; i += 2) {
        headers.push(XLSX.utils.sheet_to_json(sheet, { header: [0, i], skipHeader: true })[0][i]);
      }
      return headers;
    },
    // 获取数据
    getData(sheet) {
      const range = XLSX.utils.decode_range(sheet['!ref']);
      const data = [];
      for (let i = 9; i <= range.e.r; i++) {
        const row = [];
        for (let j = 0; j <= range.e.c; j++) {
          row.push(sheet[i][j] ? sheet[i][j].v : '');
        }
        data.push(row);
      }
      return data;
    },
    // 文件选择变化时触发
    handleChange(file, fileList) {
      this.fileList = fileList;
    },
  },
};
</script>

<style>
/* 样式可以根据需要自行调整 */
</style>