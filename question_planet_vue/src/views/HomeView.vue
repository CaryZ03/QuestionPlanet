<template>
  <body>
    <div>
    <div>

      <div class="box-btn" v-show="!this.$store.state.isLogin">
        <el-row>
          <router-link to="/login"><el-button round>登录</el-button></router-link>
          <router-link to="/register"><el-button round>注册</el-button></router-link><br>
          <router-link v-if="this.$store.state.isLogin" to="/new"><el-button round>创建问卷</el-button></router-link>
          <router-link v-else to="/login"><el-button round>创建问卷</el-button></router-link>
          <br>
        </el-row>
      </div>

    </div>
  </div>
  </body>
</template>


<script>


export default ({
  name: 'HomeViewVue',
  data: {

  }

})
</script>
<!-- <style scoped>
.BackGround{
  background-image: url(../assets/BackGround_2.jpg);
  width: 100%;
  height: 100%;
position:fixed;
background-size:100% 100%;
}
.stepLine {}

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
<style scoped>

body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: url('../assets/background2.jpg');

  background-size: cover;
  background-position: center;
}

.el-header,
.el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body>.el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style> -->
