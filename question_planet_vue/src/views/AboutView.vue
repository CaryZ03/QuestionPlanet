<template>
    <div class="background">
        <div class="about" >
      <h1>关于我们</h1>
      <p>我们是一家专注于问卷管理的公司，致力于为用户提供高效、便捷、可靠的问卷管理服务。</p>
      <!-- <img src="../assets/-311481de54f03b8f.png.png" alt="图片"> -->
      <el-link :underline="false"  style="font-size: 28px;
    margin-bottom: 20px;
    color:#d3d8db;margin: 0 auto;
    padding: 30px;
    text-align: center;"  @click="payment">支持我们</el-link>
      <img src="../assets/planet1.png">
      <!-- <img src="../assets/-311481de54f03b8f.png.png" alt="图片" style="max-width: 100%;"> -->
        </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'About',

    methods: {
    goBack() {
      this.$router.push('/');
    },

    payment(){
      this.$alert(' <img src="' + require('@/assets/付款码.jpg') + '" alt="图片" style="max-width: 100%;">', '这是付款码捏~', {
        customClass: 'my-message-box',
        dangerouslyUseHTMLString: true,
        showClose: false,
        confirmButtonText: '确定',
        center: true,
        callback: action => {
          console.log(action);
        },
        beforeClose: (action, instance, done) => {
          if (action === 'confirm') {
            done();
          }
        }
      });
    }
  },
  }
  </script>
  
  <style scoped>

.my-message-box .el-message-box__message img {
  max-width: 100%;
}

.background{
    background-image: url("../assets/-311481de54f03b8f.png.png");
  width: 100%;
  height: 200%;
  overflow-y: hidden;
position:fixed;
background-size:100% 100%;
background: transparent;

margin: -284px 0 0 -761px;
padding: 0px 0 0 9px;
}

  .about {
    max-width: 800px;
    margin: 0 auto;
    padding: 30px;
    text-align: center;
    font-size: 18px;
    color: #e9e9e9;

    margin: -36px auto 0;

  }
  .about h1 {
    font-size: 28px;
    margin-bottom: 20px;
    color:#d3d8db;
  }

  .about el-link{
    font-size: 28px;
    margin-bottom: 20px;
    color:#d3d8db;
  }

  
  /* header */
  
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
  color: #040404;
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