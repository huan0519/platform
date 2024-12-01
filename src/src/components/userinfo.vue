<!--右上角个人头像和用户名显示组件-->
<template>
  <div class="user-info">
    <div v-if="isLoggedIn" class="af_login">
      <img :src="userAvatar" class="avatar" @click="Send_Page" />
      <span class="username" style="color: #E9EEF3">{{ userName }}</span>

    </div>
    <div v-else class="login-link">
      <router-link to="/login" style="color: #475669;font-weight: bolder">
        <i class="el-icon-user" style="color: #475669"></i> 登录
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
    userName() {
      return this.$store.state.userName;
    },
    userAvatar() {
      return this.$store.state.userAvatar || require('../assets/logo.png');
    },
  },
  methods: {

    Send_Page(){
      this.$router.push('/personal_center').catch(err=>err);
    }
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