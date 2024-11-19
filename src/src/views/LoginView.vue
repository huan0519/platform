<template>
  <div id="app" class="back" @click="createSplash($event)">
    <el-container style="max-height: 100vh">
        <div class="form">
          <div style="margin: 10px 115px; font-size: 44px;letter-spacing: 15px;"><a>欢迎使用</a></div>
          <div style="margin: 20px 115px; font-size: 14px;letter-spacing: 3px;font-style: italic;"><a>welcome</a></div>
            <el-form ref="user" :model="user" :rules="rules" label-width="100px">
              <el-form-item label="账号" prop="username">
                <el-input class="button_back" v-model="user.username" placeholder="请输入账号" prefix-icon="el-icon-user" clearable ></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input class="button_back" type="password" v-model="user.password" prefix-icon="el-icon-lock" placeholder="请输入密码" clearable show-password ></el-input>
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


  import anime from "animejs";

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
    methods: {
      createSplash(event) {
        const { clientX, clientY } = event;

        // 创建一个新的水花 DOM 元素
        const splash = document.createElement("div");
        splash.classList.add("splash");

        // 设置初始位置并考虑宽高居中
        const size = 70; // 水花大小
        splash.style.width = `${size}px`;
        splash.style.height = `${size}px`;
        splash.style.left = `${clientX - size / 2}px`;
        splash.style.top = `${clientY - size / 2}px`;

        document.body.appendChild(splash);

        // 动画效果
        anime({
          targets: splash,
          scale: [0, 1],
          opacity: [1, 0],
          easing: "easeOutQuad",
          duration: 800,
          complete: () => {
            // 动画完成后移除 DOM 元素
            splash.remove();
          },
        });
      },
      handleLogin() {
        console.log('Logging in with:', this.user);
        this.$refs['user'].validate((valid) => {
          if (valid) {
            axios.post("http://localhost:8085/user/login", this.user).then(res => {
              if (res.data.code === '200') {
                localStorage.setItem("user", JSON.stringify(res.data.data))
                this.$router.push("/")
                this.$message.success("登录成功")
              } else {
                this.$message.error(res.data.msg)
              }
            })
          } else {
            return false;
          }
        });
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
    created() {
      axios.get('http://localhost:8080').then(function (res){
        let that=this;
        that.user = res.data;
      }).catch(err => err)
    }
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
  .back{
    height: 100vh;
    background-image: linear-gradient(to bottom right,#efeced,#3F5EFB);
    overflow: hidden;
  }
  .custom-button{
    width: 100px;
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