<template>
<div style="display: flex;height: 100vh;align-items: center;justify-content: center;background: #00BBFF">
  <div class="bubble">这是一个气泡对话框</div>
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

 .bubble {
   position: relative;
   padding: 10px;
   background: #f0f0f0;
   border-radius: 5px;
   width: 200px;
 }

.bubble::before {
  content: "";
  position: absolute;
  left: -10px;
  top: 50%;
  transform: translateY(-50%);
  border: 10px solid transparent;
  border-right-color: #ff007f;
}
</style>

