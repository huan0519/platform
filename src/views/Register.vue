<template>
    <div id="app" class="back">
      <el-container>
        <el-header>
            <el-button @click="handleClick" class="el-icon-arrow-left" style="font-size: 40px;float: left">
            </el-button>
        </el-header>
      <div class="form">
        <div style="margin: 10px 115px; font-size: 44px;letter-spacing: 15px;"><a>注册</a></div>
        <div style="margin: 20px 115px; font-size: 14px;letter-spacing: 3px;font-style: italic;"><a>Sign Up</a></div>
        <el-form ref="user" :model="user" :rules="rules" label-width="100px">
          <el-form-item label="用户名" prop="username">
            <el-input style="width: 320px;" v-model="user.username" placeholder="请输入用户名" prefix-icon="el-icon-user" clearable></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input style="width: 320px;" type="password" v-model="user.password" prefix-icon="el-icon-lock" placeholder="请输入密码" clearable show-password></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="confirmPassword">
            <el-input style="width: 320px;" type="password" v-model="user.confirmPassword" prefix-icon="el-icon-lock" placeholder="请再次输入密码" clearable show-password></el-input>
          </el-form-item>
          <el-form-item class="button_group">
            <el-button type="primary" style="width: 200px;" @click="handleRegister" class="custom-button">注册</el-button>
            <router-link style="" to="/login" class="link">
              已有账号？登录
            </router-link>
          </el-form-item>
        </el-form>
      </div>
      </el-container>
    </div>
  </template>
  
  <script>
  import { Container } from 'element-ui';
  
  export default {
  
    data() {
      return {
        user: {},
        rules: {
          username: [
            { required: true, message: '请输入用户名', trigger: 'blur' },
            { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'blur' },
            { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
          ],
          confirmPassword: [
            { required: true, message: '请再次输入密码', trigger: 'blur' },
            { validator: (rule, value, callback) => {
              if (value !== this.user.password) {
                callback(new Error('两次输入的密码不一致!'));
              } else {
                callback();
              }
            }, trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      handleRegister() {
        // 注册逻辑
        console.log('Registering with:', this.user);
      },
      goToLogin() {
        // 跳转到登录页面的逻辑
        this.$router.push('/Login');
      },
      handleClick(){
        this.$router.push('/');
      }
    },
  };
  </script>
  
  <style scoped>

  .el-header {
    background-color: #B3C0D1;
    opacity: 0.2;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .back {
    height: 100vh;
    background-image: linear-gradient(to bottom right, #efeced, #3F5EFB);
    overflow: hidden;
    cursor: url('../../public/image/kl1.png'), auto !important;
  }
  .custom-button {
    width: 100px;
  }
  .button-group {
    display: flex; /* 启用 Flexbox */
    justify-content: space-between; /* 按钮之间的空间均匀分布 */
  }
  .form {
    margin-top: 17%;
    margin-left: 34%;
  }
  .link{
    color: #3F5EFB;
    padding: 4px;
    text-decoration: none;
  }
  .link:hover{
    color: #E9EEF3;
  }
  </style>