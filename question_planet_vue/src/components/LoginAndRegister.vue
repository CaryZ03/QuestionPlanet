<template>
  <div class="wrapper">
    <span class="icon-close"><i class="el-icon-edit"></i></span>

    <div class="form-box login">
      <h2 style="color: aliceblue;">Login</h2>
      <form @click.prevent="">
        <div class="input-box">
          <span class="icon"><i class="el-icon-edit"></i></span>
          <input type="text" v-model="user.username" required>
          <label style="color: aliceblue;">Email</label>
        </div>

        <div class="input-box">
          <span class="icon"><i class="el-icon-edit"></i></span>
          <input type="password" v-model="user.password" required>
          <label style="color: aliceblue;">password</label>
        </div>

        <div class="remember-forgot">
          <label><input type="checkbox" v-model="isRemember">Remember Me</label>
          <a href="#" style="color: aliceblue;">Forgot Password</a>
        </div>

        <button class="btn" @click="login">Login</button>
        <button class="btn" @click="test">test</button>

        <div class="login-register">
          <p style="color: aliceblue;">Don't have an account?<a href="#" class="register-link"
              style="color: aliceblue;">Register</a></p>
        </div>
      </form>
    </div>

    <div class="form-box register">
      <h2 style="color: aliceblue;">Registeration </h2>
      <form>
        <div class="input-box">
          <span class="icon"><i class="el-icon-edit"></i></span>
          <input type="text" v-model="userR.username" required>
          <label style="color: aliceblue;">Username</label>
        </div>

        <div class="input-box">
          <span class="icon"><i class="el-icon-edit"></i></span>
          <input type="password" v-model="userR.password1" required>
          <label style="color: aliceblue;">password1</label>
        </div>

        <div class="input-box">
          <span class="icon"><i class="el-icon-edit"></i></span>
          <input type="password" v-model="userR.password2" required>
          <label style="color: aliceblue;">password2</label>
        </div>

        <div class="remember-forgot">
          <label style="color: aliceblue;"><input type="checkbox" v-model="isAgree">agree to the terms &
            conditions</label>
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


          alert("win")
          console.log(response.data)

          this.$store.state.token_key=response.data['token_key']
          console.log(response.data.token_key)

          console.log(response.data)
          
          console.log(response.data.uid)
          this.$store.state.curUserID = response.data['uid']
          this.$store.state.curUsername = this.user.username
          this.$store.state.isLogin = true

          console.log(`/manage/${this.$store.state.curUserID}`)
          // set cookie
          this.$router.push({
            path: `/manage/${this.$store.state.curUserID}`
          })
        }
        else {
          console.log(response.data)
          console.log("发生了奇怪的问题")
        }
      }).catch(error => {
        console.log(error)
        alert("wa")


      })
    },
    test(){
      this.$router.push({
            path: "/manage/" + this.$store.state.curUserID
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

        console.log(wrapper)

        const btnLogin = document.querySelector('.btnLogin-popup')
        const iconClose = document.querySelector('.icon-close')

        if(wrapper!=null)
        wrapper.classList.add('active-popup');

        this.$nextTick(()=>{
          if(wrapper!=null&&registerLink!=null){
            registerLink.addEventListener('click', () => {
            wrapper.classList.add('active');
          });
          }

          if(wrapper!=null&&loginLink!=null)
        loginLink.addEventListener('click', () => {
            wrapper.classList.remove('active');
        });

        if(wrapper!=null&&btnLogin!=null)
        btnLogin.addEventListener('click', () => {
            wrapper.classList.add('active-popup');
        });

        if(wrapper!=null&&iconClose!=null)
        iconClose.addEventListener('click', () => {
            wrapper.classList.remove('active-popup');
        })
        })

        // wrapper.classList.add('active-popup');
    }
}
</script>
<style scoped>
input[type="text"],
input[type="password"],
input[type="email"] {
  background: transparent;
}
</style>
<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

h2 {
  box-sizing: border-box;
  color: #ffffff;
  font-family: Poppins, sans-serif;
  font-size: 2em;
  margin: 0;
  padding: 0;
  text-align: center;
}

header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 20px 100px;
  /* background: red; */
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 99;
}

.logo {
  font-size: 2em;
  color: #fff;
  user-select: none;

}

.navigation {
  position: relative;
  font-size: 1.1em;
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  margin-left: 40px;
}


.navigation .btnLogin-popup {
  width: 130px;
  height: 50px;
  background: transparent;
  border: 2px solid #fff;
  outline: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1.1em;
  color: #fff;
  font-weight: 500;
  margin-left: 40px;
  transition: .3s;
}

.navigation a {
  position: relative;
  font-size: 1.1em;
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  margin-left: 40px;
}

.navigation a::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 3px;
  bottom: -6px;
  left: 0;
  background: #fff;
  border-radius: 5px;
  transform-origin: right;
  transform: scaleX(0);
  transition: transform .4s;
}

.navigation a:hover::after {
  transform-origin: left;
  transform: scaleX(1);
}


.navigation .btnLogin-popup:hover {
  background: #fff;
  color: #162938;

}

.wrapper {
  position: relative;
  width: 400px;
  height: 440px;
  background: transparent;
  border: 2px solid rgba(255, 255, 255, .5);
  border-radius: 20px;
  backdrop-filter: blur(20px);
  box-shadow: 0 0 30px rgba(0, 0, 0, .5);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;

  transform: scale(0);
  transition: transform .5s ease, height .2s ease;
}

.wrapper.active-popup {
  transform: scale(1);
}

.wrapper.active {
  height: 520px;

}

.wrapper .form-box {
  width: 100%;
  padding: 40px;
}

.wrapper .form-box.login {
  transition: transform .18s ease;
  transform: translateX(0);
}

.wrapper.active .form-box.login {
  /* display: none; */
  transition: none;
  transform: translateX(-400px);
}

.wrapper .form-box.register {
  position: absolute;
  transform: translateX(400px);
}

.wrapper.active .form-box.register {
  /* display: none; */
  transition: transform .18s ease;
  transform: translateX(0);
}

.wrapper .icon-close {
  position: absolute;
  top: 0;
  right: 0;
  width: 45px;
  height: 45px;
  background: #162938;
  font-size: 2em;
  display: flex;
  color: #fff;
  justify-content: center;
  align-items: center;
  border-bottom-left-radius: 20px;
  cursor: pointer;
  z-index: 1;

}

.form-box h2 {
  font-size: 2em;
  color: #162938;
  text-align: center;
}

.input-box {
  position: relative;
  width: 100%;
  height: 50px;
  border-bottom: 2px solid #162938;
  margin: 30px 0;
}

/* .input-box input:not(:placeholder-shown)~label, */
.input-box input:focus~label,
.input-box input:valid~label {
  top: -5px;
}

.input-box label {
  position: absolute;
  top: 50%;
  left: 5px;
  transform: translateY(-50%);
  font-size: 1em;
  color: #162938;
  font-weight: 500;
  pointer-events: none;
  transition: all .3s ease;
}

.input-box input {
  width: 100%;
  height: 100%;
  background: transparent;
  border: none;
  outline: none;
  font-size: 1em;
  color: #ffffff;
  font-weight: 600;
  padding: 0 35px 0 5px;
}

.input-box .icon {
  position: absolute;
  right: 8px;
  font-size: 1.2em;
  color: #ffffff;
  line-height: 57px;
}

.remember-forgot {
  font-size: .9em;
  color: #ffffff;
  font-weight: 500;
  margin: -15px 0 15px;
  display: flex;
  justify-content: space-between;
}

.remember-forgot label input {
  accent-color: #ffffff;
  margin: 3px;
}

.remember-forgot a {
  color: #162938;
  text-decoration: none;
}

.remember-forgot a:hover {
  text-decoration: underline;
}

.btn {
  width: 100%;
  height: 45px;

  background: #162938;
  border: none;
  outline: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1em;
  color: #fff;
  font-weight: 500;

}

.login-register {
  font-size: .9em;
  color: #162938;
  text-align: center;
  font-weight: 500;
  margin: 25px 0 10px;
}

.login-register p a {
  color: #162938;
  text-decoration: none;
  font-weight: 600;
}

.login-register p a:hover {
  text-decoration: underline;
}
</style>