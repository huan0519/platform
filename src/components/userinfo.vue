<!--右上角个人头像和用户名显示组件-->
<template>
    <div class="user-info">
      <div v-if="isLoggedIn" class="af_login">
        <img :src="userAvatar" class="avatar" @click="Send_Page" />
        <span class="username">{{ userName }}</span>
      </div>
      <div v-else class="login-link">
        <i class="el-icon-user"></i>
        <router-link to="/login">登录</router-link>
      </div>
  </div>
</template>

<script>
import avetar from '../assets/logo.png';
import vue_header from "@/components/vue_header.vue";

export default {
  components:{
    vue_header
  },

  name: 'UserInfo',
  data() {
    return {
      isLoggedIn: false, // 这里需要根据实际情况来设置
      userName: 'maxia', // 实际用户名
      userAvatar: avetar, // 实际用户头像路径
    };
  },
  methods: {
    Send_Page() {
      this.$emit('ChangePage');
    },
  },
};
</script>

<style scoped>
.user-info {
  display: flex;
  align-items: center;

}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  cursor: pointer;
}

.login-link {
  display: flex;
  align-items: center;
}

.username{
  align-self: center;
  margin-left: 20px;
}

a {
  text-decoration: none;
  color: #000;
}

.af_login{
  display: flex;
  align-items: center;
  font-size: 14px;
}
</style>