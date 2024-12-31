<!--个人中心-->
<template>
  <div id="app" class="container">
    <el-card class="card" shadow="hover">
      <!-- 头像和用户名 -->
      <div class="profile-header">
        <img :src="cardimage" alt="用户头像" class="card-img" />
        <span class="name-style">{{ userName }}</span>
        <button class="Btn" @click="logout" style="margin-left: 50vw">

          <div class="sign"><svg viewBox="0 0 512 512"><path d="M377.9 105.9L500.7 228.7c7.2 7.2 11.3 17.1 11.3 27.3s-4.1 20.1-11.3 27.3L377.9 406.1c-6.4 6.4-15 9.9-24 9.9c-18.7 0-33.9-15.2-33.9-33.9l0-62.1-128 0c-17.7 0-32-14.3-32-32l0-64c0-17.7 14.3-32 32-32l128 0 0-62.1c0-18.7 15.2-33.9 33.9-33.9c9 0 17.6 3.6 24 9.9zM160 96L96 96c-17.7 0-32 14.3-32 32l0 256c0 17.7 14.3 32 32 32l64 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-64 0c-53 0-96-43-96-96L0 128C0 75 43 32 96 32l64 0c17.7 0 32 14.3 32 32s-14.3 32-32 32z"></path></svg></div>

          <div class="text">-         Logout</div>
        </button>

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
/* From Uiverse.io by vinodjangid07 */
.Btn {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  width: 45px;
  height: 45px;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition-duration: .3s;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.199);
  background-color: rgb(255, 65, 65);
}

/* plus sign */
.sign {
  width: 100%;
  transition-duration: .3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sign svg {
  width: 17px;
}

.sign svg path {
  fill: white;
}
/* text */
.text {
  position: absolute;
  right: 0%;
  width: 0%;
  opacity: 0;
  color: white;
  font-size: 1.2em;
  font-weight: 600;
  transition-duration: .3s;
}
/* hover effect on button width */
.Btn:hover {
  width: 125px;
  border-radius: 40px;
  transition-duration: .3s;
}

.Btn:hover .sign {
  width: 30%;
  transition-duration: .3s;
  padding-left: 20px;
}
/* hover effect button's text */
.Btn:hover .text {
  opacity: 1;
  width: 70%;
  transition-duration: .3s;
  padding-right: 10px;
}
/* button click effect*/
.Btn:active {
  transform: translate(2px ,2px);
}
</style>
