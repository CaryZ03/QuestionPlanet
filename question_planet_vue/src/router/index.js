import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
const Login = () => import('../views/LoginView.vue');
const CreateQuestionnaireView = () => import('../views/CreateView.vue');
const UserInfoView = () => import('../views/UserInfoView.vue')
const Analyze = () => import('../views/AnalyzeView.vue')
const Answer = () => import('@/views/AnswerView.vue')
const Preview = () => import('@/views/PreviewView.vue')
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
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/manage/:userID',
    name: 'Manager',
    component: () => import('../views/ManageView.vue'),
    children: [
      {
        path: 'questionnaire_create/:qn_id',
        name: 'questionnaire_create', //问卷管理

        component: CreateQuestionnaireView
      },
      {
        name: 'questionnaire_bin',//垃圾箱
        path: 'questionnaire_bin',
      },
      {
        name: 'questionnaire_model',
        path: 'questionnaire_model',
      },
      {
        name: 'questionnaire_check',
        path: 'questionnaire_check',
      },
      {
        path: '/Analyze/:qn_id',
        name: 'Analyze',
        component: Analyze
      }

    ]
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/userInfo/:userID',
    name: 'UserInfo',
    component: UserInfoView
  },
  {
    path: '/answer/:qn_id',
    name: 'Answer',
    component: Answer
  },
  {
    path: '/preview/:qn_id',
    name: 'Preview',
    component: Preview
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path === from.path) {  // 判断目标路径是否相同
    return next(false)  // 阻止路由跳转
  }
  next()  // 允许路由跳转
})
const routerRePush = VueRouter.prototype.push
VueRouter.prototype.push = function (location) {
  return routerRePush.call(this, location).catch(error => error)
}

export default router
