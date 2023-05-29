import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

const Login = () => import('../views/LoginView.vue');
const Register = () => import('../views/RegisterView.vue');
const CreateQuestionnaireView = () => import('../views/CreateView.vue');
const UserInfoView = () => import('../views/UserInfoView.vue')
const Analyze = () => import('../views/AnalyzeView.vue')
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/manage/:userID',
    name: 'Manager',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/ManageView.vue'),
    children:[
      {
        name:'questionnaire_create', //问卷管理
        path:'questionnaire_create',
        component: CreateQuestionnaireView
      },
      {
        name:'questionnaire_bin',//垃圾箱
        path:'questionnaire_bin',
      },
      {
        name:'questionnaire_model',
        path:'questionnaire_model',
      },
      {
        name:'questionnaire_check',
        path:'questionnaire_check',
      },

    ]
  },
  {
    path: '/login/',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:Login
  },
  {
    path: '/register',
    name: 'Register',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:Register
  },
  {
    path: '/userInfo/:userID',
    name: 'UserInfo',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:UserInfoView
  },
  {
    path: '/Analyze/:qn_id',
    name: 'Analyze',
    component: Analyze
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
