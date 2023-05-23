import request from "@/utils/request";

export function getUserInfo(uname) {
    return request({
        method: 'GET',
        url: '/user',
        params:{username:uname}
    })
}
//uname是主键，data是我们要更新的东西捏捏捏
export function updateUserInfo(uname, data) {
    return request({
        method: 'PUT',
        url: `/user/${uname}`,
        data,
        // params:{username:uname}
    })
}
export function postUserInfo(user) {
    return request({
        method: 'POST',
        url: '/user',
        data: user,
    })
}

