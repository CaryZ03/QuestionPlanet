<template>
    <div class="background">
        <div class="about" >
      <h1>关于我们</h1>
      <p>我们是一家专注于问卷管理的公司，致力于为用户提供高效、便捷、可靠的问卷管理服务。</p>
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
  },
  }
  </script>
  
  <style scoped>
.background{
    background-image: url("../assets/-311481de54f03b8f.png.png");
  width: 100%;
  height: 200%;
  overflow-y: hidden;
position:fixed;
background-size:100% 100%;

margin: -284px 0 0 -759px;
padding: 0px 0 0 9px;
}

  .about {
    max-width: 800px;
    margin: 0 auto;
    padding: 30px;
    text-align: center;
    font-size: 18px;
    color: #333;

  }
  .about h1 {
    font-size: 28px;
    margin-bottom: 20px;
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