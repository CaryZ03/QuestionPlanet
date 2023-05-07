<template>
  <div id="app">
    <ul class="header">
      <li><router-link to="/">主页</router-link> </li>
      <li><router-link to="/about">关于</router-link></li>
      <li><router-link to="/new">新页面</router-link></li>
      <li v-show="!isLogin"><router-link to="/login">Login</router-link></li>
      <li><router-link to="/register">Register</router-link></li>

    </ul>
    <router-view/>
  </div>
</template>

<script>
export default {
  name:'app',
  data() {
    return {
      isLogin:false
    }
  },
  methods: {
    login(){
      isLogin=true
    }
  },
}
</script>



<style>

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
#app li{
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
