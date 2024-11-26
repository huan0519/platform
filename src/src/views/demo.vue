<template>
  <div>
    <nav>
      <a
          :class="{ active: activeMenu === 'home' }"
          @click="setActiveMenu('home', '/')"
      >
        Home
      </a>
      <a
          :class="{ active: activeMenu === 'about' }"
          @click="setActiveMenu('about', '/about')"
      >
        About
      </a>
      <a
          :class="{ active: activeMenu === 'contact' }"
          @click="setActiveMenu('contact', '/contact')"
      >
        Contact
      </a>
    </nav>
    <router-view />
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  computed: {
    ...mapState(['activeMenu']), // 从 Vuex 中获取状态
  },
  methods: {
    ...mapMutations(['setActiveMenu']),
    navigate(menu, path) {
      this.setActiveMenu(menu);
      this.$router.push(path);
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

a.active {
  color: red; /* 高亮样式 */
  font-weight: bold;
}
</style>
