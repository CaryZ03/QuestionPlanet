import axios from "axios";
import Cookies from 'js-cookie'

const token = Cookies.get('token')
axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
axios.defaults.withCredentials = true;



const request = axios.create({
    baseURL: 'http://182.92.102.246:1145/api',
    timeout: 10000,
    headers:{
        'Content-Type': 'application/json'
    }
})

export default request 