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

        <!-- 处理前模块 -->
        <el-container v-if="activePage === 'before'" class="table-container">
          <el-table :data="tableDataBefore" border>
            <el-table-column
                v-for="(value, key) in tableDataBefore[0] || {}"
                :key="key"
                :prop="key"
                :label="key"
            ></el-table-column>
          </el-table>
        </el-container>

        <!-- 处理后模块 -->
        <el-container v-if="activePage === 'after'" class="table-container">
          <el-table :data="tableDataAfter" border>
            <el-table-column
                v-for="(value, key) in tableDataAfter[0] || {}"
                :key="key"
                :prop="key"
                :label="key"
            ></el-table-column>
          </el-table>
        </el-container>
      </el-main>

      <!-- 控制台 -->
      <el-aside width="400px" class="aside">
        <p style="margin: 20px;line-height: 40px;font-weight: bolder">控制台</p>
        <el-button class="chart-button" @click="submitUpload">提交</el-button>
        <el-upload
            class="upload-demo"
            ref="upload"
            :auto-upload="false"
            :on-change="handleFileUpload"
            accept=".txt,.csv,.xls,.xlsx"
        >
          <div>
            <el-button class="sel_button">选择文件</el-button>
          </div>
        </el-upload>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import * as XLSX from "xlsx";
import axios from "axios";

export default {
  data() {
    return {
      activePage: "before",
      tableDataBefore: [], // 处理前数据
      tableDataAfter: [],  // 处理后数据
      selectedFile: null,  // 当前选中文件
    };
  },
  methods: {
    handleFileUpload(file) {
      // 处理上传文件，显示在“处理前”模块
      const reader = new FileReader();
      reader.onload = (e) => {
        const fileData = new Uint8Array(e.target.result);
        const workbook = XLSX.read(fileData, { type: "array" });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

        // 构建表格数据
        const headers = jsonData[0].map((col, index) => {
          return index === 0 ? col : `Sample_${index + 0}`;
        });
        const tableData = jsonData.slice(1).map((row) =>
            headers.reduce((acc, key, i) => ({ ...acc, [key]: row[i] || null }), {})
        );
        this.tableDataBefore = tableData;
        this.selectedFile = file; // 保存文件以供后续上传
      };
      reader.readAsArrayBuffer(file.raw);
    },
    async submitUpload() {
      if (!this.selectedFile) {
        this.$message.error("请先选择文件！");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.selectedFile);

      try {
        const response = await axios.post("http://localhost:8000/get_data", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });

        // 假设后端返回处理后的表格数据
        this.tableDataAfter = response.data.tableData || [];
        this.activePage = "after"; // 切换到“处理后”模块
        this.$message.success("文件处理成功！");
      } catch (error) {
        console.error("上传失败:", error);
        this.$message.error("文件处理失败，请重试！");
      }
    },
  },
};
</script>

<style scoped>
.table-container {
  padding: 20px;
}
.aside {
  background-color: #f5f7fa;
  padding: 20px;
}
.chart-button {
  width: 100%;
  margin-top: 20px;
}
.sel_button {
  margin-top: 20px;
  display: block;
  background-color: #409eff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
}
.sel_button:hover {
  cursor: pointer;
  background-color: #66b1ff;
}
</style>
