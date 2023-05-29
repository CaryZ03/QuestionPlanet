import request from "@/utils/request";

//用户注册
export function postUserInfo_Register(data) {
    return request({
        method: 'POST',
        url: '/user/user_register',
        data: data
    })
}
// 用户登录
export function postUserInfo_UserLogin(data) {
    return request({
        method: 'POST',
        url:  '/user/user_login',
        data: data
    })
}
//  管理员登录
export function postUserInfo_AdminLogin(data) {
    return request({
        method: 'POST',
        url:  '/user/admin_login',
        data: data
    })
}
//发验证码
export function postUserInfo_SendVeri(data) {
    return request({
        method: 'POST',
        url:  '/user/send_verification_code',
        data: data
    })
}
//重置密码
export function postUserInfo_ResetPassword(data) {
    return request({
        method: 'POST',
        url:  '/user/reset_password',
        data: data
    })
}
//登出
export function postUserInfo_Logout(data) {
    return request({
        method: 'POST',
        url:  '/user/logout',
        data: user
    })
}
//cancel_account
export function postUserInfo_CancelAccount(data) {
    return request({
        method: 'POST',
        url:  '/user/cancel_account',
        data: data
    })
}

// check_profile,获取用户信息
export function getUserInfo_GetUserInfo(data) {
    return request({
        method: 'GET',
        url:  '/user/check_profile',
        data: data
    })
}

//check_profile_admin
export function postUserInfo_GetAdminInfo(data) {
    return request({
        method: 'POST',
        url:  '/user/check_profile_admin',
        data: data
    })
}

// change_profile
export function postUserInfo_ChangeUserInfo(data) {
    return request({
        method: 'POST',
        url:  '/user/change_profile',
        data: data
    })
}

// change_profile admin
export function postUserInfo_ChangeAdminInfo(data) {
    return request({
        method: 'POST',
        url:  '/user/change_profile_admin',
        data: data
    })
}

// 获取用户问卷列表
export function postUserInfo_GetQList(data) {
    return request({
        method: 'POST',
        url:  '/user/check_questionnaire_list',
        data: data
    })
}

// 封禁用户
export function postUserInfo_ChangeUserStatus(user) {
    return request({
        method: 'POST',
        url:  '/user/change_user_status',
        data: user
    })
}









