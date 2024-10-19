<template>
  <div id="app" class="back">
    <el-header>
    </el-header>
    <el-container class="el-container">
        <div class="form">
          <div style="margin: 10px 115px; font-size: 44px;letter-spacing: 15px;"><a>欢迎使用</a></div>
          <div style="margin: 20px 115px; font-size: 14px;letter-spacing: 3px;font-style: italic;"><a>welcome</a></div>
            <el-form ref="user" :model="userform" :rules="rules" label-width="100px">
              <el-form-item label="账号" prop="username">
                <el-input class="button_back" v-model="userform.username" placeholder="请输入账号" prefix-icon="el-icon-user" clearable ></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input class="button_back" type="password" v-model="userform.password" prefix-icon="el-icon-lock" placeholder="请输入密码" clearable show-password ></el-input>
              </el-form-item>
              <el-form-item class="button_group">
                <el-button type="primary" style="width: 200px;" @click="handleLogin" class="custom-button">登录</el-button>
                <el-button type="link" @click="goToRegister" class="custom-button">注册</el-button>
              </el-form-item>
            </el-form>
          </div>
    </el-container>
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {

    data() {
      return {
        userform: {
          username: '',
          password: '',
          img_path: '',
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
        mockUsers: [
          { username: 'admin', password: '123456' ,img_path: '../../public/image/HT.jpg'}
        ]
      };
    },
    methods: {
      handleLogin() {
        // 登录逻辑
        const user = this.mockUsers.find(u => u.username === this.userform.username);
        if (user && user.password === this.userform.password) {
          this.$message.success("登录成功");
          // 这里可以跳转到主页或其他页面
          this.$router.push('/');
        } else {
          this.$message.error("登陆失败");
          // 这里可以显示登录失败的提示信息
        }
        console.log('Logging in with:', this.user);
        // this.$refs['user'].validate((valid) => {
        //   if (valid) {
        //     axios.post("http://localhost:8085/user/login", this.user).then(res => {
        //       if (res.data.code === '200') {
        //         localStorage.setItem("user", JSON.stringify(res.data.data))
        //         this.$router.push("/")
        //         this.$message.success("登录成功")
        //       } else {
        //         this.$message.error(res.data.msg)
        //       }
        //     })
        //   } else {
        //     return false;
        //   }
        // });
      },
      goToRegister() {
      // 跳转到注册页面
      this.$router.push('/Register');
    },
      handleClick(){
        //回主页
        this.$router.push('/');
      }
    },
  };
  </script>

  <style scoped>
  .el-container{
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .button_back{
    width: 320px;
  }
  .el-header{
    background-color: #B3C0D1;
    opacity: 0.33;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .back{
    height: 100vh;
    background-image: linear-gradient(to bottom right,#efeced,#3F5EFB);
    overflow: hidden;
    cursor: url('../../public/image/kl.png'), auto !important;
    display: flex;
    justify-content: center;
  }
  .custom-button{
  width: 100px;
  }
  .button-group {
    display: flex; /* 启用 Flexbox */
    justify-content: space-between; /* 按钮之间的空间均匀分布 */
  }
  .form{
    justify-content: center;
    align-items: center;
  }
  </style>