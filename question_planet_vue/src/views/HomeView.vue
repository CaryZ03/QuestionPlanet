<template>
  <div>
    <div >

      <div class="box-btn" v-show="!this.$store.state.isLogin">
        <el-row>
          <router-link to="/login"><el-button round>登录</el-button></router-link>

          <router-link to="/register"><el-button round>注册</el-button></router-link><br>

          <router-link v-if="this.$store.state.isLogin" to="/new"><el-button round>创建问卷</el-button></router-link>
          <router-link v-else to="/login"><el-button round>创建问卷</el-button></router-link>
          <br>
          <div class="stepLine">
            <el-steps :active="active" finish-status="success">
            <el-step title="步骤 1"></el-step>
            <el-step title="步骤 2"></el-step>
            <el-step title="步骤 3"></el-step>
          </el-steps>

          <el-button style="margin-top: 12px;" @click="next">下一步</el-button>
          </div>
        </el-row>
      </div>



      <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
      <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    </div>
  </div>
</template>

<script>
import StepSlideVue from "../components/StepSlide.vue"


export default ({
  name: 'HomeViewVue',
  data: {

  }

})
</script>
<style scoped>
.stepLine{
  
}
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

  /* background-image: "../assets/BackGround.jpg"; */
}

.mbody {
  height: 100%;
  width: 100%;
  /* background-image: url('../assets/BackGround.jpg'); */
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100%;
  color: aqua;
  background-color: aqua;
  position: relative;
}

.box-btn {
  position: absolute;
  display: flex;
  height: 100%;
  width: 100%;
  margin: auto;
}

.el-row {
  position: relative;
  height: 100%;
  width: 100%;
  top: 35%;
}
</style>
