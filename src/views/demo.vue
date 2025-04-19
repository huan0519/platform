<template>
  <!-- 热力图容器 -->
  <div style="width: 80%;" v-show="activePage === 'after'">
    <span style="font-style: oblique; font-size: large">热力图</span>
    <div class="glass-container">
      <div ref="hot_chart" style="width: 90%; height: 560px; margin-top: 20px"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activePage: '', // 由父组件控制
      hotChartInstance: null,
      resizeObserver: null
    }
  },
  watch: {
    activePage(newVal) {
      if (newVal === 'after') {
        this.$nextTick(() => {
          if (!this.hotChartInstance) {
            this.initHotChart()
          } else {
            // 确保容器尺寸更新后重绘
            this.hotChartInstance.resize()
          }
        })
      }
    },

  },
  mounted() {
    // 如果初始状态需要显示
    if (this.activePage === 'after') {
      this.initHotChart()
    }
  },
  methods: {
    initHotChart() {
      const chartDom = this.$refs.hot_chart
      this.hotChartInstance = echarts.init(chartDom)

      // 初始化图表配置
      const option = {
        // 你的热力图配置项
        // ...
      }
      this.hotChartInstance.setOption(option)

      // 窗口缩放监听
      window.addEventListener('resize', this.handleHotChartResize)

      // 容器尺寸变化监听 (现代浏览器)
      if (typeof ResizeObserver !== 'undefined') {
        this.resizeObserver = new ResizeObserver(() => {
          this.hotChartInstance.resize()
        })
        this.resizeObserver.observe(chartDom)
      }
    },
    handleHotChartResize() {
      this.hotChartInstance && this.hotChartInstance.resize()
    }
  },
  beforeDestroy() {
    // 清理资源
    if (this.hotChartInstance) {
      this.hotChartInstance.dispose()
      window.removeEventListener('resize', this.handleHotChartResize)
    }
    if (this.resizeObserver) {
      this.resizeObserver.disconnect()
    }
  }
}
</script>

<style>
/* 确保容器链式继承 */
.glass-container {
  width: 100%; /* 继承父级80%宽度 */
  height: 600px; /* 总高度 = 560px + 20px margin-top */
}
</style>