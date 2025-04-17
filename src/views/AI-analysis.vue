<template>
  <div id="app" class="container">
  <div class="chatbox">
    <!-- 标题栏 -->
    <div class="header">
      <h3>医疗数据分析AI小助手</h3>
    </div>

    <!-- 聊天记录窗口 -->
    <div class="chat-window">
      <div v-for="message in messages" :key="message.id" :class="['message', message.role]">
        <div class="message-bubble" v-html="message.content"></div>
      </div>
      <!-- 图表渲染区域 -->
      <div v-if="chartConfig" class="chart-container">
        <div id="chart" style="width: 100%; height: 400px;"></div>
      </div>
    </div>

    <!-- 输入框和按钮 -->
    <div class="input-box">
      <!-- 普通聊天模式 -->
      <div v-if="!isFileUploading" class="chat-input">
        <input
            class="input"
            type="text"
            v-model="userMessage"
            @keyup.enter="sendMessage"
            placeholder="输入您的消息"
        />
        <button  @click="sendMessage">
          <div class="svg-wrapper-1">
            <div class="svg-wrapper">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                <path fill="none" d="M0 0h24v24H0z"></path>
                <path fill="currentColor" d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"></path>
              </svg>
            </div>
          </div>
          <span>发送</span>
        </button>
        <button @click="startFileUpload">上传文件</button>
      </div>

      <!-- 文件上传模式 -->
      <div v-if="isFileUploading" class="file-upload">
            <input class="ul-input" type="file" @change="handleFileUpload"/>
        <button @click="uploadFile">上传文件</button>
        <button @click="cancelFileUpload">取消</button>
      </div>

      <!-- 图表参数选择 -->
      <div v-if="availableColumns.length > 0" class="parameters">
        <label for="chartType">选择图表类型：</label>
        <select v-model="selectedChartType">
          <option value="bar">柱状图</option>
          <option value="line">折线图</option>
          <option value="pie">饼图</option>
          <option value="scatter">散点图</option>
          <option value="radar">雷达图</option>
          <option value="stackedBar">堆叠柱状图</option>
          <option value="bubble">气泡图</option>
          <option value="waterfall">瀑布图</option>
        </select>

        <label for="xAxis">选择横轴：</label>
        <select v-model="selectedXAxis">
          <option v-for="col in availableColumns" :key="col" :value="col">{{ col }}</option>
        </select>

        <label for="yAxis">选择纵轴：</label>
        <select v-model="selectedYAxis">
          <option v-for="col in availableColumns" :key="col" :value="col">{{ col }}</option>
        </select>

        <button @click="analyzeData">开始分析</button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import * as echarts from "echarts";

export default {
  data() {
    return {
      userMessage: "",
      messages: [],
      isFileUploading: false,
      file: null,
      availableColumns: [],
      selectedChartType: "bar",
      selectedXAxis: "",
      selectedYAxis: "",
      chartConfig: null,
      analyzedData: null, // 用于存储文件解析后的数据
    };
  },
  methods: {
    // 逻辑部分保持不变
    async sendMessage() {
      if (!this.userMessage.trim()) return;

      this.messages.push({
        id: Date.now(),
        role: "user", // 或 "system"
        content: this.userMessage, // 发送的内容
      });


      const userMessage = this.userMessage;
      this.userMessage = "";

      try {
        const requestData = {
          model: "4.0Ultra",
          messages: [{ role: "user", content: userMessage }],
        };

        const response = await axios.post(
            "http://127.0.0.1:8000/api/chat",
            requestData,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
        );

        if (response.data && response.data.chatResponse) {
          this.messages.push({
            id: Date.now(),
            role: "system",
            content: response.data.chatResponse,
          });
        } else {
          this.messages.push({
            id: Date.now(),
            role: "system",
            content: "未能获得有效响应，请稍后再试。",
          });
        }
      } catch (error) {
        console.error("Request failed:", error);
        this.messages.push({
          id: Date.now(),
          role: "system",
          content: "聊天处理失败，请稍后再试。",
        });
      }
    },
    startFileUpload() {
      this.isFileUploading = true;
    },
    cancelFileUpload() {
      this.isFileUploading = false;
      this.file = null;
      this.availableColumns = [];
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.file = file;
      }
    },
    async uploadFile() {
      if (!this.file) {
        this.messages.push({
          id: Date.now(),
          role: "system",
          content: "请先选择文件再上传。",
        });
        return;
      }

      const formData = new FormData();
      formData.append("file", this.file);

      try {
        const response = await axios.post(
            "http://127.0.0.1:8000/api/analyze",
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
        );

        if (response.data.recommendations) {
          const recommendations = response.data.recommendations;
          this.messages.push({
            id: Date.now(),
            role: "system",
            content: `推荐图表：${recommendations.chartType}，横轴：${recommendations.xAxis}，纵轴：${recommendations.yAxis}`,
          });

          this.availableColumns = response.data.columns;
          this.selectedChartType = recommendations.chartType;
          this.selectedXAxis = recommendations.xAxis;
          this.selectedYAxis = recommendations.yAxis;

          this.analyzedData = response.data.data;
        } else {
          this.messages.push({
            id: Date.now(),
            role: "system",
            content: "文件上传成功，但未能生成推荐参数。",
          });
        }
      } catch (error) {
        console.error("File upload failed:", error.response?.data || error);
        this.messages.push({
          id: Date.now(),
          role: "system",
          content: "文件上传失败，请稍后再试。",
        });
      }
    },
    async analyzeData() {
      if (!this.selectedXAxis || !this.selectedYAxis) {
        this.messages.push({
          id: Date.now(),
          role: "system",
          content: "请先选择横轴和纵轴。",
        });
        return;
      }

      const requestData = {
        chartType: this.selectedChartType,
        xAxis: this.selectedXAxis,
        yAxis: this.selectedYAxis,
        data: this.analyzedData,
      };

      this.messages.push({
        id: Date.now(),
        role: "user",
        content: `开始分析数据，图表类型：${requestData.chartType}，横轴：${requestData.xAxis}，纵轴：${requestData.yAxis}`,
      });

      try {
        const response = await axios.post(
            "http://127.0.0.1:8000/api/analyze",
            requestData,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
        );

        if (response.data.chartConfig) {
          this.chartConfig = response.data.chartConfig;
          this.renderChart();
          this.messages.push({
            id: Date.now(),
            role: "system",
            content: "数据分析成功，图表已生成。",
          });

          if (response.data.analysisConclusion) {
            this.messages.push({
              id: Date.now(),
              role: "system",
              content: response.data.analysisConclusion,
            });
          }
        } else {
          this.messages.push({
            id: Date.now(),
            role: "system",
            content: "数据分析失败，请稍后再试。",
          });
        }
      } catch (error) {
        console.error("Data analysis failed:", error.response?.data || error);
        this.messages.push({
          id: Date.now(),
          role: "system",
          content: `数据分析失败：${error.response?.data?.error || "请稍后再试"}`,
        });
      }
    },
    renderChart() {
      this.$nextTick(() => {
        const chartDom = document.getElementById("chart");
        if (!chartDom) {
          console.error("Chart DOM element not found.");
          return;
        }

        const myChart = echarts.init(chartDom);
        if (!this.chartConfig) {
          console.error("Chart config is empty.");
          return;
        }

        try {
          myChart.setOption(this.chartConfig);
          window.addEventListener("resize", myChart.resize);
        } catch (error) {
          console.error("Error rendering chart:", error);
          this.messages.push({
            id: Date.now(),
            role: "system",
            content: "图表渲染失败，请检查图表配置。",
          });
        }
      });
    },
  },
};
</script>

<style scoped>
.container{
  width: 100%;
  height: 100%;
  overflow: hidden;
  box-sizing: border-box;
  /* Add your background pattern here */
  background: lightblue;
  background-image: radial-gradient(
      rgba(255, 255, 255, 0.9) 3px,
      transparent 0
  );
  background-size: 30px 30px;
  background-position: -5px -5px;
}
.chatbox {
  width: 1100px;
  height: 100vh;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header {
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.8em;
  font-weight: bold;
  color: #333;
}

.chat-window {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 20px;
  padding: 10px;
  background-color: #fff;
  border-radius: 10px;
  min-height: 300px;
  max-height: 600px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1);
}

.message {
  margin-bottom: 15px;
  display: flex;
}

.message.system .message-bubble {
  background-color: #e9ecef !important; /* 确保系统消息的灰色背景生效 */
  color: #333;
}

.message.user .message-bubble {
  background-color: #007bff !important; /* 确保用户消息的蓝色背景生效 */
  color: white;
}


.message-bubble {
  display: inline-block;
  max-width: 70%;
  padding: 10px 15px;
  border-radius: 15px;
  word-break: break-word;
}


.input-box {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 20px;
}

.input-box .chat-input,
.input-box .file-upload,
.input-box .parameters {
  display: flex;
  align-items: center;
  gap: 10px;
}

button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #0056b3;
}

input[type="text"],
select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  flex: 1;
}

.chart-container {
  margin-top: 20px;
  width: 100%;
  height: 400px;
  min-height: 300px;
}
.input {
  width: 100%;
  max-width: 920px;
  height: 40px;
  padding: 12px;
  border-radius: 12px;
  border: 1.5px solid lightgrey;
  outline: none;
  transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1);
  box-shadow: 0px 0px 20px -18px;
}

.input:hover {
  border: 2px solid lightgrey;
  box-shadow: 0px 0px 20px -17px;
}

.input:active {
  transform: scale(0.95);
}

.input:focus {
  border: 2px solid grey;
}
/* From Uiverse.io by eirikvold */
button {
  font-family: inherit;
  font-size: 18px;
  background: linear-gradient(to bottom, #4dc7d9 0%,#66a6ff 100%);
  color: white;
  padding: 0.8em 1.2em;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 25px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.3s;
}

button:hover {
  transform: translateY(-3px);
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.3);
}

button:active {
  transform: scale(0.95);
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}

button span {
  display: block;
  margin-left: 0.4em;
  transition: all 0.3s;
}

button svg {
  width: 18px;
  height: 18px;
  fill: white;
  transition: all 0.3s;
}

button .svg-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.2);
  margin-right: 0.5em;
  transition: all 0.3s;
}

button:hover .svg-wrapper {
  background-color: rgba(255, 255, 255, 0.5);
}

button:hover svg {
  transform: rotate(45deg);
}
.drop-container:hover .drop-title {
  color: #222;
}
.ul-input {
  width: 350px;
  max-width: 100%;
  color: #444;
  padding: 2px;
  background: #fff;
  border-radius: 10px;
  border: 1px solid rgba(8, 8, 8, 0.288);
}

.ul-input::file-selector-button {
  margin-right: 20px;
  border: none;
  background: #084cdf;
  padding: 10px 20px;
  border-radius: 10px;
  color: #fff;
  cursor: pointer;
  transition: background .2s ease-in-out;
}

.ul-input::file-selector-button:hover {
  background: #0d45a5;
}
</style>
