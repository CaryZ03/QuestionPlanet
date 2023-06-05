<template>
  <div>
    <LoginAndRegister></LoginAndRegister>
  </div>
</template>

<script>
import LoginAndRegister from '@/components/LoginAndRegister.vue'
export default {
  data() {
    return {
      // user: {
      //   username: '',
      //   password: ''
      // },
      // userR: {
      //   username: '',
      //   password1: '',
      //   password2: ''
      // },
    }
  },
  methods: {
    // login() {
    //   const data = JSON.stringify(this.user)
    //   console.log(data)



    //   this.$api.userInfo.postUserInfo_UserLogin(data).then((response) => {
    //     if (response.data['errno'] === 0) {
    //       console.log(response.data)
    //       console.log(response.data)
    //       console.log(response.data.uid)
    //       this.$store.state.curUserID = response.data['uid']
    //       this.$store.state.curUsername = this.user.username
    //       this.$store.state.isLogin = true
    //       // set cookie
    //       document.cookie = `session_id=${response.data.session_id}`;
    //       this.$router.push({
    //         path: "/manage/" + this.$store.state.curUserID
    //       })
    //     }
    //     else {
    //       console.log("发生了奇怪的问题")
    //     }
    //   }).catch(error => {
    //     console.log(error)


    //   })
    // },
    // register() {
    //   const data = JSON.stringify(this.userR)
    //   this.$api.userInfo.postUserInfo_Register(data).then((response) => {
    //     console.log(response.data)
    //     if (response.data[0].error == 0) {
    //       console.log("注册成功")
    //       this.$router.push({
    //       path: "/login" 
    //       })
    //     }
    //   }).catch(error => {
    //     alert("注册失败")
    //     console.log(error)
    //   })
    // },
  },


  components: {
    LoginAndRegister
  }
}
</script>
<style scoped>
.bigBox {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: url('../assets/background2.jpg');

    background-size: cover;
    background-position: center;
  
  
}




/* 最外层的大盒子 */
.box {
  width: 1050px;
  height: 600px;
  display: flex;
  /* 相对定位 */
  position: relative;
  z-index: 2;
  margin: auto;
  /* 设置圆角 */
  border-radius: 8px;
  /* 设置边框 */
  border: 1px solid rgba(255, 255, 255, .6);
  /* 设置盒子阴影 */
  box-shadow: 2px 1px 19px rgba(0, 0, 0, .1);
}

/* 滑动的盒子 */

</style>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
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
  color: #162938;
  font-weight: 600;
  padding: 0 35px 0 5px;
}

.input-box .icon {
  position: absolute;
  right: 8px;
  font-size: 1.2em;
  color: #162938;
  line-height: 57px;
}

.remember-forgot {
  font-size: .9em;
  color: #162938;
  font-weight: 500;
  margin: -15px 0 15px;
  display: flex;
  justify-content: space-between;
}

.remember-forgot label input {
  accent-color: #162938;
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