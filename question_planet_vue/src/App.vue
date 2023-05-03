<template>
  <div id="app">
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link> </li>
        <!-- <li><router-link to="/Menu">MenuView</router-link></li> -->
        <li><router-link to="/login">login</router-link></li>
        <li><router-link to="/register">register</router-link></li>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
<style>
#app nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: cadetblue ;
}

#app nav ul li {
    float: left;
}

#app nav ul router-link {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

#app nav ul router-link:hover {
    background-color: cornflowerblue;
}
</style>