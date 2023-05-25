import axios from "axios";

const request = axios.create({
    baseURL: 'http://182.92.102.246:1145/api',
    timeout: 10000,
    headers:{
        'Content-Type': 'application/json'
    }
})

export default request 