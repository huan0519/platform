<!--帮助-->
<template>
  <div id="app" class="help">
    <div class="tutorial-page">
      <el-container>
        <!-- 侧边栏部分 -->
        <el-aside width="300px" class="aside">
          <div class="container" style="margin: 10px">
            <div class="search-container">
              <input v-model="searchQuery" placeholder="搜索词条" class="input" type="text">
              <svg viewBox="0 0 24 24" class="search__icon">
                <g>
                  <path d="M21.53 20.47l-3.66-3.66C19.195 15.24 20 13.214 20 11c0-4.97-4.03-9-9-9s-9 4.03-9 9 4.03 9 9 9c2.215 0 4.24-.804 5.808-2.13l3.66 3.66c.147.146.34.22.53.22s.385-.073.53-.22c.295-.293.295-.767.002-1.06zM3.5 11c0-4.135 3.365-7.5 7.5-7.5s7.5 3.365 7.5 7.5-3.365 7.5-7.5 7.5-7.5-3.365-7.5-7.5z">
                  </path>
                </g>
              </svg>
            </div>
          </div>
          <el-menu @select="handleSelect">
            <el-menu-item
                v-for="item in filteredTutorials"
                :key="item.id"
                :index="String(item.id)"
            >
              {{ item.title }}
            </el-menu-item>
          </el-menu>
        </el-aside>

        <!-- 主内容部分 -->
        <el-main class="main">
          <div v-if="selectedTutorial" class="content-wrapper">
            <h1 style="font-size: 40px">{{ selectedTutorial.title }}</h1>
            <p v-html="selectedTutorial.content" class="tutorial-content"></p>
          </div>
          <div v-else>
            <h1>请选择一个教程词条</h1>
          </div>
        </el-main>
      </el-container>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      selectedTutorial: null,
      tutorials: [
        { id: 1, title: '云平台介绍', content: '在生物医学研究与药物开发领域，质谱技术是测定分子质量的关键手段，凭借其精准测定分子质量的卓越能力，始终扮演着举足轻重的角色，源源不断地为前沿研究提供关键信息。随着蛋白质组学、代谢组学等前沿研究的推进，质谱数据量激增，这些数据维度高，既蕴含海量生物信息，又充斥冗余与噪声，如何从中提炼有价值的内容，成了科研与医疗诊断的难题。\n' +
              '<br>为应对这一挑战，我们团队全力打造创新的智能质谱数据分析平台。平台基于 Flask 框架，在数据存储方面，引入了 MySQL 数据库作为核心的数据存储解决方案。MySQL 以其高可靠性、高性能和广泛的适用性，为平台的数据持久化提供了坚实保障。平台选择采用先进的前后端分离架构。前端用 Vue 框架结合 ECharts，构建直观交互的可视化界面，方便用户洞悉数据细节；后端依托 Flask，集成 TensorFlow 和 Scikit-learn 环境，为机器学习模型的开发与推理提供有力支持。<br><img src="/image/help_cloud.png" alt="Vue介绍" style="width: 50vw;margin:40px;border: 1px solid">\n' +
              '<br>平台功能模块特色鲜明。数据采集模块可高效上传、精准解析各类数据文件，大幅提升数据录入效率。数据预处理模块功能齐全，涵盖缺失值填补、异常值检测、标准化和特征选择等，为后续分析夯实基础。数据可视化模块支持多种图表，能展示原始及处理后的数据，助力用户多维度洞察数据特征。疾病预测模块借助机器学习模型，精准预测患者疾病症型，并自动生成专业报告，为医疗诊断提供关键参考。AI 辅助分析模块是作品的一大创新点，利用自然语言处理技术实现智能交互，还能根据用户需求动态生成图表，降低使用门槛，零基础用户也能轻松操作。\n' +
              '<br>在医疗诊断场景中，平台优势明显。临床医护人员多不熟悉信息技术，而该平台凭借高度的用户友好性，能帮助他们快速从复杂质谱数据中提取关键生物信息，提前预判患者患病风险，以便精准实施救治措施，帮助有效遏制疾病蔓延。同时，平台提供客观的数据分析结果，避免医生主观意识干扰，为医疗诊断提供可靠的决策依据。经多次实验验证，平台在质谱数据分析各环节都展现出良好的效率与准确性，尤其在智能化和可视化方面实现了重大技术突破。\n' +
              '<br>本研究为质谱数据的分析与应用开拓了新思路，也为智能数据分析平台的设计与开发提供了有价值的参考。同时能够减少人工干预，为生命科学和医学领域的科研人员及医护工作者提供有效的数据分析支持。' },
        { id: 2, title: '常见问题', content: 'Element UI是一个基于Vue的组件库...<br><img style="margin-left: 25vw" src="/images/element-ui.png" alt="Element UI">' },
        { id: 3, title: '数据归一化', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 4, title: '补值', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 5, title: '玫瑰图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 6, title: '堆叠柱状图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 7, title: '堆叠折线图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 8, title: '散点图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 9, title: '箱线图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 10, title: '大数据折线图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 11, title: '大数据量箱线图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 12, title: '热力图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 13, title: '3D柱状图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 14, title: '虚线柱状图', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 15, title: '数据对齐', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 16, title: '数据降维', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
        { id: 17, title: 'AI数据分析助手', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
      ]
    };
  },
  computed: {
    filteredTutorials() {
      return this.tutorials.filter(tutorial =>
          tutorial.title.includes(this.searchQuery));
    }
  },
  methods: {
    handleSelect(index) {
      const tutorial = this.tutorials.find(t => t.id == index);
      this.selectedTutorial = tutorial;
    }
  },
  created() {
    this.selectedTutorial = this.tutorials[0];
  },
};
</script>

<style scoped>
.help{
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: auto;
}
.tutorial-page {
  height: 100vh;
}
.aside {
  background-color: #f5f5f5;
  padding: 10px;
  height: auto;
  overflow: hidden;
  position: sticky;
}
.main {
  overflow: auto;
  padding: 80px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  text-align: start;
}
.content-wrapper {
  max-width: 100vw;
}
.search :hover{
  cursor: pointer;
}
.container {
  position: relative;
  background: linear-gradient(135deg, rgb(179, 208, 253) 0%, rgb(164, 202, 248) 100%);
  border-radius: 1000px;
  padding: 10px;
  display: grid;
  place-content: center;
  z-index: 0;
  max-width: 300px;
  margin: 0 10px;
}

.search-container {
  position: relative;
  width: 95%;
  border-radius: 50px;
  background: linear-gradient(135deg, rgb(218, 232, 247) 0%, rgb(214, 229, 247) 100%);
  padding: 5px;
  display: flex;
  align-items: center;
}

.search-container::after, .search-container::before {
  content: "";
  width: 100%;
  height: 100%;
  border-radius: inherit;
  position: absolute;
}

.search-container::before {
  top: -1px;
  left: -1px;
  background: linear-gradient(0deg, rgb(218, 232, 247) 0%, rgb(255, 255, 255) 100%);
  z-index: -1;
}

.search-container::after {
  bottom: -1px;
  right: -1px;
  background: linear-gradient(0deg, rgb(163, 206, 255) 0%, rgb(211, 232, 255) 100%);
  box-shadow: rgba(79, 156, 232, 0.7019607843) 3px 3px 5px 0px, rgba(79, 156, 232, 0.7019607843) 5px 5px 20px 0px;
  z-index: -2;
}

.input {
  padding: 10px;
  width: 100%;
  background: linear-gradient(135deg, rgb(218, 232, 247) 0%, rgb(214, 229, 247) 100%);
  border: none;
  color: #9EBCD9;
  font-size: 14px;
  border-radius: 50px;
}

.input:focus {
  outline: none;
  background: linear-gradient(135deg, rgb(239, 247, 255) 0%, rgb(214, 229, 247) 100%);
}

.search__icon {
  width: 30px;
  aspect-ratio: 1;
  border-left: 2px solid white;
  border-top: 3px solid transparent;
  border-bottom: 3px solid transparent;
  border-radius: 50%;
  padding-left: 12px;
  margin-right: 10px;
}

.search__icon:hover {
  border-left: 3px solid white;
}

.search__icon path {
  fill: white;
}
.tutorial-content img {
  display: block;
  max-width: 100%;
}
</style>
