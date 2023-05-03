import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const About = () => import('../views/AboutView.vue')
const Login = () => import('../views/LoginView.vue')
const Register = () => import('../views/RegisterView.vue')
const Menu = () => import('../views/MenuView.vue')
const routes = [
  
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/Menu',
    name: 'Menu',
    component: Menu
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    component: About
  },
  {
    path: '/login',
    name: 'Login' ,
    component: Login
  },
  {
    path: '/register',
    name: 'Register' ,
    component: Register
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
