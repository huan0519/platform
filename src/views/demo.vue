<template>
  <div class="tutorial-page">
    <el-container>
      <!-- 侧边栏部分 -->
      <el-aside width="300px" class="aside">
        <el-input
            v-model="searchQuery"
            placeholder="搜索词条"
            clearable
        />
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
        <div v-if="selectedTutorial">
          <h1>{{ selectedTutorial.title }}</h1>
          <p v-html="selectedTutorial.content"></p>
        </div>
        <div v-else>
          <h1>请选择一个教程词条</h1>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      selectedTutorial: null,
      tutorials: [
        { id: 1, title: 'Vue基础', content: 'Vue是一个渐进式JavaScript框架...<br><img src="/images/vue-intro.png" alt="Vue介绍">' },
        { id: 2, title: 'Element UI使用', content: 'Element UI是一个基于Vue的组件库...<br><img src="/images/element-ui.png" alt="Element UI">' },
        { id: 3, title: 'Vue路由', content: 'Vue Router用于处理页面导航...<br><img src="/images/vue-router.png" alt="Vue Router">' }
      ]
    };
  },
  computed: {
    filteredTutorials() {
      return this.tutorials
          .filter(tutorial => tutorial.title.includes(this.searchQuery))
          .sort((a, b) => a.title.localeCompare(b.title));
    }
  },
  methods: {
    handleSelect(index) {
      const tutorial = this.tutorials.find(t => t.id == index);
      this.selectedTutorial = tutorial;
    }
  }
};
</script>

<style scoped>
.tutorial-page {
  height: 100vh;
}

.aside {
  background-color: #f5f5f5;
  padding: 10px;
}

.main {
  padding: 20px;
}
</style>
