<!--注册-->
<template>
    <div id="app" class="back">
      <el-container style="max-height: 100vh;margin-top: 15%">
      <div class="form">
        <div class="heading"><a>Sign Up</a></div>
        <el-form ref="user" :model="user" :rules="rules" label-width="100px">
          <el-form-item label="用户名" prop="username">
            <el-input class="custom-input" style="width: 210px;" v-model="user.username" placeholder="请输入用户名" prefix-icon="el-icon-user" clearable/>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input class="custom-input" style="width: 250px;" type="password" v-model="user.password" prefix-icon="el-icon-lock" placeholder="请输入密码" clearable show-password/>
          </el-form-item>
          <el-form-item label="确认密码" prop="confirmPassword">
            <el-input class="custom-input" style="width: 250px;" type="password" v-model="user.confirmPassword" prefix-icon="el-icon-lock" placeholder="请再次输入密码" clearable show-password/>
          </el-form-item>
          <el-form-item class="button_group">
            <el-button type="primary" style="width: 150px;" @click="handleRegister" class="custom-button">注册</el-button>
            <router-link style="" to="/login" class="link">
              已有账号？登录
            </router-link>
          </el-form-item>
        </el-form>
      </div>
      </el-container>
      <div style="width: 10rem;position: relative;bottom: 68%">
        <div class="bubble">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div class="bubble">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div class="bubble">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div class="bubble">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div class="bubble">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
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
            { min: 8, max: 20, message: '长度在 8 到 20 个字符', trigger: 'blur' }
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
        //回主页
        this.$router.push('/');
      }
    },
  };
  </script>

  <style scoped>
  .bubble {
    position: absolute;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    box-shadow: inset 0 0 25px rgba(255, 255, 255, 0.25);
    animation: animate_4010 8s ease-in-out infinite;
  }

  .bubble:nth-child(2) {
    position: relative;
    zoom: 0.45;
    left: -10px;
    top: -100px;
    animation-delay: -4s;
  }

  .bubble:nth-child(3) {
    position: relative;
    zoom: 0.45;
    right: -80px;
    top: -300px;
    animation-delay: -6s;
  }

  .bubble:nth-child(4) {
    position: relative;
    zoom: 0.35;
    left: -120px;
    bottom: -200px;
    animation-delay: -3s;
  }

  .bubble:nth-child(5) {
    position: relative;
    zoom: 0.5;
    left: 0px;
    top: 200px;
    animation-delay: -5s;
  }

  @keyframes animate_4010 {
    0%,100% {
      transform: translateY(-20px);
    }

    50% {
      transform: translateY(20px);
    }
  }

  .bubble::before {
    content: '';
    position: absolute;
    top: 50px;
    left: 45px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: #fff;
    z-index: 10;
    filter: blur(2px);
  }

  .bubble::after {
    content: '';
    position: absolute;
    top: 80px;
    left: 80px;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #fff;
    z-index: 10;
    filter: blur(2px);
  }

  .bubble span {
    position: absolute;
    border-radius: 50%;
  }

  .bubble span:nth-child(1) {
    inset: 10px;
    border-left: 15px solid #0fb4ff;
    filter: blur(8px);
  }

  .bubble span:nth-child(2) {
    inset: 10px;
    border-right: 15px solid #ff4484;
    filter: blur(8px);
  }

  .bubble span:nth-child(3) {
    inset: 10px;
    border-top: 15px solid #ffeb3b;
    filter: blur(8px);
  }

  .bubble span:nth-child(4) {
    inset: 30px;
    border-left: 15px solid #ff4484;
    filter: blur(12px);
  }

  .bubble span:nth-child(5) {
    inset: 10px;
    border-bottom: 10px solid #fff;
    filter: blur(8px);
    transform: rotate(330deg);
  }
  .form {
    width: 470px;
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
  .back {
    max-height: 100vh;
    background-image: linear-gradient(to bottom right, #efeced, #3F5EFB);
    overflow: hidden;
    display: flex;
  }
  .el-container{
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .custom-button {
    width: 100px;
    font-weight: bold;
    border-radius: 10px;
  }
  .button-group {
    display: flex; /* 启用 Flexbox */
    justify-content: space-between; /* 按钮之间的空间均匀分布 */
  }
  .button-back{
    width: 200px;
    background: none;
    border: none;
    outline: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 9999px;
    box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
    color: #000000;
  }
  .link{
    margin-left: 20px;
    color: #3F5EFB;
    padding: 4px;
    text-decoration: none;
  }
  .link:hover{
    color: #E9EEF3;
  }
  .heading {
    text-align: center;
    font-weight: 900;
    font-size: 30px;
    color: rgb(16, 137, 211);
    margin-bottom: 20px;
    margin-right: 20px
  }
  .custom-input ::v-deep .el-input__inner {
    width: 260px;
    background: none;
    border: none !important; /* 需要强制覆盖 */
    outline: none;
    padding: 10px 30px;
    font-size: 16px;
    border-radius: 9999px !important;
    box-shadow: inset 2px 5px 10px rgb(5 5 5 / 20%);
    color: #000;
    transition: all 0.3s;
  }
  /* 处理聚焦状态 */
  .custom-input ::v-deep .el-input.is-focus .el-input__inner {
    box-shadow: inset 2px 5px 10px rgb(5 5 5 / 30%);
  }

  /* 处理悬停状态 */
  .custom-input ::v-deep .el-input:hover .el-input__inner {
    box-shadow: inset 2px 5px 10px rgb(5 5 5 / 25%);
  }

  /* 处理禁用状态 */
  .custom-input ::v-deep .el-input.is-disabled .el-input__inner {
    box-shadow: inset 2px 5px 10px rgb(5 5 5 / 10%);
    background-color: #f5f5f5;
  }
  </style>
