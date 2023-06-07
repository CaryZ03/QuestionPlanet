import axios from "axios";
import store from "@/store";
// import Cookies from 'js-cookie'

// const token = Cookies.get('token')
// axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
// axios.defaults.withCredentials = true;

// axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
axios.defaults.withCredentials = true;

const request = axios.create({
  baseURL: 'http://182.92.102.246:1145/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
})

request.interceptors.request.use(
  config => {
    var token_key = localStorage.getItem("token")

    // if (store.state.token_key !== '')
    //   token_key = store.state.token_key;
    // else{
    // if (localStorage.getItem("token") != null)
    //   token_key = localStorage.getItem("token")
    // }
    // console.log(token_key)
    if (token_key) {
      config.headers['Authorization'] = token_key;
    }
    return config;
  },
  error => {
    console.log(error)
    return Promise.reject(error);
  }
);


// 请求拦截器，自动注入 cookie
// request.interceptors.request.use((config) => {
//     const session_id = getCookie('session_id');
//     if (session_id) {
//         config.headers.Cookie = `session_id=${session_id}`;
//     }
//     return config;
// });


// function getCookie(key) {
//     const name = `${key}=`;
//     const cookies = document.cookie.split(';');
//     for (let i = 0; i < cookies.length; i++) {
//         let c = cookies[i].trim();
//         if (c.indexOf(name) == 0) {
//             return c.substring(name.length, c.length);
//         }
//     }
//     return '';
// }


export default request 