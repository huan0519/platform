<!--个人中心-->
<template>
  <div id="app" class="container">
    <el-card class="card" shadow="hover">
      <!-- 头像和用户名 -->
      <div class="profile-header">
        <img :src="cardimage" alt="用户头像" class="card-img" />
        <span class="name-style">{{ userName }}</span>
        <el-button type="danger" size="mini" class="logout-button" @click="logout">
          退出登录
        </el-button>
      </div>

      <el-divider></el-divider>

      <!-- 描述列表 -->
      <el-descriptions column="2" border class="descriptions">
        <el-descriptions-item label="用户名">{{ userName}}</el-descriptions-item>
        <el-descriptions-item label="手机号">10086</el-descriptions-item>
        <el-descriptions-item label="居住地">加利福尼亚州</el-descriptions-item>
        <el-descriptions-item label="备注">
          <el-tag size="small" type="info">学校</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="联系地址" span="2">
          江苏省苏州市吴中区吴中大道 1188 号
        </el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>


<script>
import Vue_header from "@/components/vue_header.vue";
import card_img from "../assets/logo.png";

export default {
  components: {
    Vue_header,
  },
  data() {
    return {
      cardimage: card_img,
    };
  },
  computed: {
    userName() {
      return this.$store.state.userName;
    },
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/login");
    },
  },
};
</script>


<style scoped>
/* 外部容器 */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

/* 卡片样式 */
.card {
  width: 75vw;
  padding: 20px;
  border-radius: 12px;
  height: 80vh;
}

/* 头像和用户名区域 */
.profile-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

/* 头像样式 */
.card-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 2px solid #dcdfe6;
}

/* 用户名样式 */
.name-style {
  font-size: 18px;
  font-weight: bold;
  margin-left: 20px;
  color: #333;
}

/* 退出按钮 */
.logout-button {
  margin-left: auto;
  background-color: #f56c6c;
  color: white;
}

/* 描述列表样式 */
.descriptions {
  margin-top: 20px;
}

.el-descriptions__label {
  font-weight: 600;
  color: #606266;
}

.el-descriptions__content {
  color: #333;
}
</style>
