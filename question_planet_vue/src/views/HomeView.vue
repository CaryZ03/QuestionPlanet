<template>
  <div class="box">

    <div class="box-btn">
      <el-row>
        <router-link to="/login"><el-button round >登录</el-button></router-link>

        <router-link to="/register"><el-button round>注册</el-button></router-link><br>

        <router-link v-if="this.$store.state.isLogin" to="/new"><el-button round>创建问卷</el-button></router-link>
        <router-link v-else to="/login"><el-button round>创建问卷</el-button></router-link>
        <br>
        
      </el-row>
    </div>

    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
</script>
<style >
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
.mbody {
  height:100%;
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
  height:100%;
  width: 100%;
  margin: auto; 
}
.el-row{
  position: relative;
  height:100%;
  width: 100%;
  top: 35%;
}
  
</style>
