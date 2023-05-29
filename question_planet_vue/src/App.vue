<template>
  <body>
    <el-header>
      <header>

        <h2 class="logo">logo</h2>
        <nav class="navigation">
          <a href=""  @click.prevent="pushHome">主页</a>
          <a href="" @click.prevent="pushAbout">关于 </a>

          <a href="" v-if="this.$store.state.isLogin" @click.prevent="pushManage">问卷管理</a>
          <a href="" v-else @click.prevent="pushLogin">问卷管理</a>

          <!-- <a href="" @click.prevent="">Contact</a> -->
          <a href="" v-if="this.$store.state.isLogin" @click.prevent="pushUserInfo">用户信息</a>
          <a href="" v-else @click.prevent="pushLogin">用户信息</a>

          <button v-if="!this.$store.state.isLogin" class="btnLogin-popup">登录/注册</button>
          <a href="" v-else @click.prevent="logout">退出登录</a>
        </nav>
      </header>
    </el-header>
    <div class="app-wrapper">
      <router-view></router-view>
    </div>
    
  </body>
</template>

<script>
import Newhome from '@/components/Newhome.vue';
export default {

  name: 'app',
  data() {
    return {
    }
  },


  methods: {
    pushHome() {

      this.$router.push({
        name: 'home',
      })
    },
    pushUserInfo() {
      if (this.$store.state.isLogin == false) {
        this.$router.push({
          name: 'Login',
        })
        return;
      }
      this.$router.push({
        name: 'UserInfo',
        params: {
          userID: this.$store.state.curUserID,
        }
      }),
        alert("my new ")
    },
    pushManage() {
      this.$store.state.isAnalyzing = false
      this.$store.state.is_creating = false
      if (this.$store.state.isLogin == false) {
        this.$router.push({
          name: 'Login',
        })
        return;
      }
      this.$router.push({
        name: 'Manager',
        params: {
          userID: this.$store.state.curUserID,
        }
      }),
        alert("my new ")
    },
    pushLogin() {
      const wrapper = document.querySelector('.wrapper')
      const btnLogin = document.querySelector('.btnLogin-popup')
      wrapper.classList.add('active-popup');
      
      this.$router.push({
        name: 'Login',
      }),
        alert("my new ")
    },
    pushAbout() {

      this.$router.push({
        name: 'About',
      }),
        alert("my new ")
    },
    logout() {
      this.$store.isLogin = false
      this.$store.curUserID = -1
      this.$store.curUserName = ''
      this.$store.token_key = ''
      this.$router.push({
        name: 'Login',
      })

    },

    show() {
      const udata = {
        "uid": 21373219
      }
    },
  },
  components:{
      newhome: Newhome,
  },
}
</script>



<style scoped>
.app-wrapper {
  display: flex;
  position: relative;
}

header {
  flex: 1;
  /* background: transparent; */
  /* background-color: #4CAF50; */

  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 20px 100px;
  /* background: red; */
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 200;
  /* 设置一个背景色便于观察 */
  /* box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px; */
}

aside {
  bottom: 40px;
  color: #262626;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  font-size: 12px;
  left: 5px;
  margin: 0;
  padding: 0 0px 0 0;
  position: fixed;
  text-align: left;
  top: 100px;
  width: 20%;
  z-index: 200;
  /* background-color: #fff; */
}

main {
  bottom: 40px;
  color: #262626;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  font-size: 12px;
  left: 25%;
  margin: 0;
  padding: 0 0px 0 0;
  position: fixed;
  text-align: left;
  top: 100px;
  /* position: absolute; */
  width: 70%;
  z-index: 200;
  background: transparent;
  backdrop-filter: blur(20px);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}



body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  /* background: url('./assets/background2.jpg'); */
  background:  url('./assets/homebackground.jpg');

  background-size: cover;
  background-position: center;
  z-index: 100;
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
</style>


<style >
#login {
  float: right !important;
  margin: 5px 10px 0;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  border: 1px solid #e7e7e7;
  background-color: #f3f3f3;
}

li {
  float: left;
}

li a {
  display: block;
  color: #666;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #ddd;
}

li a.active {
  color: white;
  background-color: #4CAF50;
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#app ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  border: 1px solid #e7e7e7;
  background-color: #f3f3f3;
}

#app li {
  float: left;
}

#app li a:hover:not(.active) {
  background-color: #ddd;
}

#app li a.active {
  color: white;
  background-color: #4CAF50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>