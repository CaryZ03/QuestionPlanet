<template>
    <div class="bg">
      <newhome></newhome>
    </div>

</template>

<script>


import Newhome from '@/components/Newhome.vue';
export default ({
  name: 'HomeViewVue',
  data() {
    return {
      isShow: true
    }
  },

  components: {
    newhome: Newhome,
  },

})
</script>



<style scoped>
.bg {
  /* background-image:  url('../assets/homebackground.jpg'); */
  /* background-image: url("../assets/-311481de54f03b8f.png.png"); */
  width: 100%;
  overflow-y: hidden;
  position: fixed;
  left: 0;
  top: 0;
  /* background-size: 100% 100%; */

  /* margin: -377px 0px 0 -762px;
  padding: 0 0 0px 0px; */

  background: transparent;
}


img{
    background: transparent;
}

</style>
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
