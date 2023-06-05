import request from "@/utils/request";
//创建问卷
export function postQuestionnaire_Create(data) {
    return request({
        method: 'POST',
        url: '/questionnaire/create_questionnaire',
        data: data
    })
}
// 点击问卷链接时调用，创建新的答卷人或查找已存在答卷人，并创建新的答卷
export function postQuestionnaire_Fill(id) {
    return request({
        method: 'POST',
        url: `/questionnaire/fill_questionnaire/${id}`,
    })
}
//暂存回答
export function postAnswer_Save(data) {
    return request({
        method: 'POST',
        url: '/questionnaire/save_answers',
        data: data
    })
}

//提交回答
export function postAnswer_Submit(data) {
    return request({
        method: 'POST',
        url: '/questionnaire/submit_answers',
        data: data
    })
}

//保存问卷
export function postQuestionnaire_Save(data) {
    return request({
        method: 'POST',
        url: '/questionnaire/save_questionnaire',
        data: data
    })
}
//删除问卷
export function postQuestionnaire_Delete(data) {
    return request({
        method: 'POST',
        url: '/questionnaire/delete_questionnaire',
        data: data
    })
}
//改变问卷状态
export function postQuestionnaire_ChangeStatus(data) {
    return request({
        method: 'POST',
        url: '/questionnaire/change_questionnaire_status',
        data: data
    })
}

export function getQuestionnaire_Check(qn_id) {
    return request({
        method: 'GET',
        url: `/questionnaire/check_questionnaire/${qn_id}`
    })
}
