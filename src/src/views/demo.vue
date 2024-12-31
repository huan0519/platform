<template>
  <div class="container">
    <div class="heading">Sign In</div>
      <div class="form">
        <div style="margin: 10px 115px; font-size: 44px;letter-spacing: 15px;"><a>欢迎使用</a></div>
        <div style="margin: 20px 115px; font-size: 14px;letter-spacing: 3px;font-style: italic;"><a>welcome</a></div>
        <el-form ref="user" :model="user" :rules="rules" label-width="100px">
          <el-form-item label="账号" prop="username">
            <input type="text" class="button_back" v-model="user.username" placeholder="请输入账号"/>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <input class="button_back" type="password" v-model="user.password" placeholder="请输入密码"/>
          </el-form-item>
          <el-form-item class="button_group">
            <el-button type="primary" style="width: 100px;" @click="handleLogin" class="custom-button">登录</el-button>
            <el-button type="link" @click="goToRegister" class="custom-button">注册</el-button>
          </el-form-item>
        </el-form>
      </div>
  </div>


</template>

<script>
export default {

  data() {
    return {
      user: {
        username: '',
        password: '',
        avatar_url: '',
        token: '',
      },
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
          {min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
          {min: 8, max: 20, message: '长度在 8 到 20 个字符', trigger: 'blur'}
        ],
      },
    };
  },
}
</script>

<style scoped>
/* From Uiverse.io by mahbowal */
.container {
  max-width: 350px;
  background: #f8f9fd;
  background: linear-gradient(
      0deg,
      rgb(255, 255, 255) 0%,
      rgb(244, 247, 251) 100%
  );
  border-radius: 40px;
  padding: 25px 35px;
  border: 5px solid rgb(255, 255, 255);
  box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 30px 30px -20px;
  margin: 20px;
}

.heading {
  text-align: center;
  font-weight: 900;
  font-size: 30px;
  color: rgb(16, 137, 211);
}

.form {
  margin-top: 20px;
}

.form .input {
  width: 100%;
  background: white;
  border: none;
  padding: 15px 20px;
  border-radius: 20px;
  margin-top: 15px;
  box-shadow: #cff0ff 0px 10px 10px -5px;
  border-inline: 2px solid transparent;
}

.form .input::-moz-placeholder {
  color: rgb(170, 170, 170);
}

.form .input::placeholder {
  color: rgb(170, 170, 170);
}

.form .input:focus {
  outline: none;
  border-inline: 2px solid #12b1d1;
}

.form .forgot-password {
  display: block;
  margin-top: 10px;
  margin-left: 10px;
}

.form .forgot-password a {
  font-size: 11px;
  color: #0099ff;
  text-decoration: none;
}

.form .login-button {
  display: block;
  width: 100%;
  font-weight: bold;
  background: linear-gradient(
      45deg,
      rgb(16, 137, 211) 0%,
      rgb(18, 177, 209) 100%
  );
  color: white;
  padding-block: 15px;
  margin: 20px auto;
  border-radius: 20px;
  box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 20px 10px -15px;
  border: none;
  transition: all 0.2s ease-in-out;
}

.form .login-button:hover {
  transform: scale(1.03);
  box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 23px 10px -20px;
}

.form .login-button:active {
  transform: scale(0.95);
  box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 15px 10px -10px;
}

.social-account-container {
  margin-top: 25px;
}

.social-account-container .title {
  display: block;
  text-align: center;
  font-size: 10px;
  color: rgb(170, 170, 170);
}

.social-account-container .social-accounts {
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-top: 5px;
}

.social-account-container .social-accounts .social-button {
  background: linear-gradient(45deg, rgb(0, 0, 0) 0%, rgb(112, 112, 112) 100%);
  border: 5px solid white;
  padding: 5px;
  border-radius: 50%;
  width: 40px;
  aspect-ratio: 1;
  display: grid;
  place-content: center;
  box-shadow: rgba(133, 189, 215, 0.8784313725) 0px 12px 10px -8px;
  transition: all 0.2s ease-in-out;
}

.social-account-container .social-accounts .social-button .svg {
  fill: white;
  margin: auto;
}

.social-account-container .social-accounts .social-button:hover {
  transform: scale(1.2);
}

.social-account-container .social-accounts .social-button:active {
  transform: scale(0.9);
}

.agreement {
  display: block;
  text-align: center;
  margin-top: 15px;
}

.agreement a {
  text-decoration: none;
  color: #0099ff;
  font-size: 9px;
}
.el-container{
  display: flex;
  justify-content: center;
  align-items: center;
}
.back{
  height: 100vh;
  background-image: linear-gradient(to bottom right,#efeced,#3F5EFB);
  overflow: hidden;
}
.button_back {
  width: 160px;
  background: none;
  border: none;
  outline: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 9999px;
  box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
  color: #fff;
}
.custom-button{
  width: 70px;
  font-weight: bold;
  border-radius: 10px;
}
.button-group {
  display: flex; /* 启用 Flexbox */
  justify-content: space-between; /* 按钮之间的空间均匀分布 */
}
.splash {
  position: absolute;
  background-color: rgba(0, 150, 255, 0.6);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none; /* 防止水花干扰点击事件 */
}
</style>
