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
        { id: 1, title: '云平台介绍', content: 'Vue是一个渐进式JavaScript框架...<br><img src="/image/3D.png" alt="Vue介绍">' },
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
        { id: 16, title: '数据增强（PCA）', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' },
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
  overflow: hidden;
}
.tutorial-page {
  height: 100vh;
}
.aside {
  background-color: #f5f5f5;
  padding: 10px;
  height: 100vh;
}
.main {
  width: 100vw;
  padding: 20px;
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