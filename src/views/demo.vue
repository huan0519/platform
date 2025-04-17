<template>
  <div>
    <div
        class="aside-container"
        :class="{ 'collapsed': !isDrawerOpen }">
      <nav>
        <h3>导航菜单</h3>
        <ul>
          <li>菜单项1</li>
          <li>菜单项2</li>
        </ul>
      </nav>
    </div>
    <button :label="false" @click="toggleDrawer" class="button">
      <i :class="iconClass" style="font-size: 25px"></i>
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isDrawerOpen: true
    };
  },
  methods: {
    toggleDrawer() {
      this.isDrawerOpen = !this.isDrawerOpen;
    }
  }
};
</script>

<style>
.aside-container {
  width: 200px;
  height: 100vh;
  background: #fff;
  box-shadow: 2px 0 8px rgba(0,0,0,0.1);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.aside-container.collapsed {
  transform: translateX(-100%);
}

/* 美化内容 */
nav {
  padding: 20px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 10px;
  cursor: pointer;
}
li:hover {
  background: #f5f5f5;
}
.button {
  height: 50px;
  padding: 0;
  position: fixed;
  width: 40px;
  border: none;
  border-bottom-right-radius: 30%;
}
.button :hover{
  cursor: pointer;
}
</style>