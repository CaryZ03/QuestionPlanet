<template>
    <div class="wrapper">
        <span class="icon-close"><i class="el-icon-edit"></i></span>

        <div class="form-box login">
            <h2>Login</h2>
            <form>
                <div class="input-box">
                    <span class="icon"><i class="el-icon-edit"></i></span>
                    <input type="text" v-model="user.username" required>
                    <label>Email</label>
                </div>

                <div class="input-box">
                    <span class="icon"><i class="el-icon-edit"></i></span>
                    <input type="password" v-model="user.password" required>
                    <label>password</label>
                </div>

                <div class="remember-forgot">
                    <label><input type="checkbox" v-model="isRemember">Remember Me</label>
                    <a href="#">Forgot Password</a>
                </div>

                <button class="btn" @click="login">Login</button>

                <div class="login-register">
                    <p>Don't have an account?<a href="#" class="register-link">Register</a></p>
                </div>
            </form>
        </div>

        <div class="form-box register">
            <h2>Registeration </h2>
            <form>
                <div class="input-box">
                    <span class="icon"><i class="el-icon-edit"></i></span>
                    <input type="text" v-model="userR.username" required>
                    <label>Username</label>
                </div>

                <div class="input-box">
                    <span class="icon"><i class="el-icon-edit"></i></span>
                    <input type="password" v-model="userR.password1" required>
                    <label>password1</label>
                </div>

                <div class="input-box">
                    <span class="icon"><i class="el-icon-edit"></i></span>
                    <input type="password" v-model="userR.password2" required>
                    <label>password2</label>
                </div>

                <div class="remember-forgot">
                    <label><input type="checkbox" v-model="isAgree">agree to the terms & conditions</label>
                </div>

                <button class="btn" @click="register">Register</button>

                <div class="login-register">
                    <p>Already have an account?<a href="#" class="login-link">Login</a></p>
                </div>
            </form>
        </div>
    </div>
</template>

<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<script>

import maxios from '../api'
export default {
    data() {
    return {
      user: {
        username: '',
        password: ''
      },
      userR: {
        username: '',
        password1: '',
        password2: ''
      },
      isAgree: false,
      isRemember: false
    }
  },
  methods: {
    login() {
      const data = JSON.stringify(this.user)
      console.log(data)



      this.$api.userInfo.postUserInfo_UserLogin(data).then((response) => {
        if (response.data['errno'] === 0) {

          this.$store.state.token_key=response.data['token_key']
          console.log(response.data.token_key)

          console.log(response.data)
          
          console.log(response.data.uid)
          this.$store.state.curUserID = response.data['uid']
          this.$store.state.curUsername = this.user.username
          this.$store.state.isLogin = true
          // set cookie
          document.cookie = `session_id=${response.data.session_id}`;
          this.$router.push({
            path: "/manage/" + this.$store.state.curUserID
          })
        }
        else {
          console.log(response.data)
          console.log("发生了奇怪的问题")
        }
      }).catch(error => {
        console.log(error)


      })
    },
    register() {
        if(this.isAgree==false){
            alert("请确认用户协议")
            return;
        }
      const data = JSON.stringify(this.userR)
      console.log(data)
      this.$api.userInfo.postUserInfo_Register(data).then((response) => {
        console.log(response.data)
        if (response.data.errno == 0) {
            alert("注册成功")
          const wrapper = document.querySelector('.wrapper')
        }
      }).catch(error => {
        alert("注册失败")
        console.log(error)
      })
    },
  },


    
    

    mounted() {
        const wrapper = document.querySelector('.wrapper')
        const loginLink = document.querySelector('.login-link')
        const registerLink = document.querySelector('.register-link')

        const btnLogin = document.querySelector('.btnLogin-popup')
        const iconClose = document.querySelector('.icon-close')

        registerLink.addEventListener('click', () => {
            wrapper.classList.add('active');
        });

        loginLink.addEventListener('click', () => {
            wrapper.classList.remove('active');
        });


        btnLogin.addEventListener('click', () => {
            wrapper.classList.add('active-popup');
        });


        iconClose.addEventListener('click', () => {
            wrapper.classList.remove('active-popup');
        })
    }
}
</script>
<style>
input[type="text"],
input[type="password"],
input[type="email"] {
    background: transparent;
}
</style>
