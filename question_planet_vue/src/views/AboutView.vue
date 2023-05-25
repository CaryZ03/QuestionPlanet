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
  overflow-y: scroll;
position:fixed;
background-size:100% 100%;
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


  
  </style>