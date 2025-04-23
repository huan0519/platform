<template>
  <!-- From Uiverse.io by Dennyhml -->
  <div id="app" class="back" @click="createSplash($event)">
    <el-container style="max-height: 100vh;margin-top: 15%">
      <div class="container1">
        <div class="heading" style="margin: 20px">Sign In</div>
        <div class="form">
          <el-form ref="user" :model="user" :rules="rules" label-width="100px">
            <el-form-item label="账号" prop="username">
              <el-input type="text" class="custom-input" v-model="user.username" prefix-icon="el-icon-user" clearable placeholder="请输入账号"/>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input class="custom-input" type="password" v-model="user.password" prefix-icon="el-icon-lock" clearable show-password placeholder="请输入密码"/>
            </el-form-item>
            <el-form-item class="button_group">
              <el-button type="primary" style="width: 120px;" @click="handleLogin" class="custom-button">登录</el-button>
              <el-button type="link" @click="goToRegister" class="custom-button">注册</el-button>
            </el-form-item>
          </el-form>
        </div>
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
import anime from "animejs";
import Vue from "vue";
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI);

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
              const { username, avatar_url } = res.data.data;

              // 使用 Vuex 更新全局状态
              this.$store.dispatch('login', { username, avatar_url });
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
.container1 {
  max-width: 420px;
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
.custom-input ::v-deep .el-input__inner {
  width: 250px;
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