<template>
    <div class="row">

        <!-- 问题列表 -->
        <div class="question-card" id="question-list" style="margin: 0 0 0 -62px">
            <el-container class="card mb-2" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main>
                        <span style="color: #F3F2F2;">问卷标题：{{ this.qn_title }}</span>
                    </el-main>
                </el-container>

                <div style="line-height: 30px;">&emsp;</div>

            <div v-for="(question, index) in questions" :key="index" class="card mb-2" v-bind:id="question.id">
                <el-container style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main>
                        <span class="red_star" v-if="question.q_mandatory">*&nbsp;</span>
                        <span class="red_star" v-else></span>
                        <span v-if="question.q_type === 'single'" style="color: #F3F2F2;">{{ index + 1 }}.单选题</span>
                        <span v-if="question.q_type === 'multiple'" style="color: #F3F2F2;">{{ index + 1 }}.多选题</span>
                        <span v-if="question.q_type === 'text'" style="color: #F3F2F2;">{{ index + 1 }}.填空题</span>
                        <span v-if="question.q_type === 'judge'" style="color: #F3F2F2;">{{ index + 1 }}.判断题</span>
                        <span v-if="question.q_type === 'grade'" style="color: #F3F2F2;">{{ index + 1 }}.打分题</span>
                        <div style="line-height: 30px;">&emsp;</div>
                        <div style="color: #F3F2F2;">题目：{{ question.q_title }}</div>

                        <div style="line-height: 30px;">&emsp;</div>

                        <div v-if="question.q_type === 'single' || question.q_type === 'multiple'">
                            <div class="division"><span class="title" style="color: #F3F2F2;">选项</span></div>
                            <div v-if="question.q_type === 'single'">
                                <el-radio-group v-model="question.a_content">
                                    <el-radio v-for="(option, index_option) in question.q_options" :label="index_option"
                                        :key="index_option" style="color: #F3F2F2;">{{ option.label }}</el-radio>
                                    
                                </el-radio-group>
                            </div>

                            <div v-if="question.q_type === 'multiple'">
                                <div v-for="(option, index_option) in question.q_options" :key="index_option">
                                    <el-checkbox :label="index_option" v-model="option.checked" style="color: #F3F2F2;">{{ option.label
                                    }}</el-checkbox>
                                </div>
                            </div>
                        </div>

                        <div v-else-if="question.q_type === 'text'">
                            <div class="division"><span class="title" style="color: #F3F2F2;">内容</span></div>
                            <el-input type="textarea" autosize placeholder="请输入内容" v-model="question.a_content"></el-input>
                        </div>

                        <div v-else-if="question.q_type === 'judge'">
                            <div class="division"><span class="title" style="color: #F3F2F2;">选项</span></div>
                            <el-radio-group v-model="question.a_content">
                                <el-radio :label="0" style="color: #F3F2F2;">错误</el-radio>
                                <el-radio :label="1" style="color: #F3F2F2;">正确</el-radio>
                            </el-radio-group>
                        </div>

                        <div v-else-if="question.q_type === 'grade'">
                            <div class="division"><span class="title" style="color: #F3F2F2;">评分</span></div>
                            <el-rate
                                v-model="question.a_content"
                                :colors="grade_colors">
                            </el-rate>
                        </div>

                    </el-main>
                </el-container>

                <div style="line-height: 30px;">&emsp;</div>

            </div>
            <el-button type="success" style="margin: 0 0 0 214px" round v-on:click="submit_answer()">保存回答</el-button>
            <el-button type="primary" round >提交回答</el-button>
        </div>



        <router-view></router-view>
    </div>
</template>
  
<script>
import axios from 'axios';
// const vm = new Vue({
//   el: '#question-list',
//   data:{
//     seen:true
//   }
// }
// )

export default {
    name: 'createQuestionnaire',
    data() {
        return {
            uid: this.$store.state.curUserID,
            qn_id: "",
            as_id: "",
            qn_title: "这是问卷标题",
            qn_description: "",
            qn_end_time: "",
            qn_refillable: "",
            questions: [],
            answer_sheet: [],
            grade_colors: ['#99A9BF', '#F7BA2A', '#FF9900']
        };
    },
    created() {
        this.qn_id = this.$route.params.qn_id;
        this.load_qn();
        this.create_as();
    },
    methods: {
        create_as()
        {
            var _this = this;
            this.$api.questionnaire.postQuestionnaire_Fill(this.$route.params.qn_id)
            .then(function (response) {
            console.log(_this.qn_id);
            console.log(response);
            _this.as_id = response.data.as_id;
            console.log(_this.as_id);
            })
            .catch(function (error) {
            console.log(error);
            });
        },
        load_qn()
        {   
            var _this = this;
            this.$api.questionnaire.getQuestionnaire_Check(this.qn_id)
            .then(function (response) {
            //console.log(response);
            //console.log(response.data.qn_info);
            //console.log(response.data.question_list);
            const qn_info = JSON.parse(response.data.qn_info);
            const qn_list = response.data.question_list;
            console.log(qn_info);
            _this.qn_title = qn_info.qn_title;
            _this.qn_id = qn_info.qn_id;
            _this.qn_end_time = qn_info.qn_end_time;
            _this.qn_description = qn_info.qn_description;
            _this.qn_refillable = qn_info.qn_refillable;
            qn_list.forEach(question => {
                const item = JSON.parse(question);
                item.q_options = JSON.parse(item.q_options);
                _this.questions.push(item);
            })
            //_this.questions = qn_list;
            })
            .catch(function (error) {
            console.log(error);
            });
            console.log(this.qn_id);
        },

        submit_answer(){
            this.answer_sheet.splice(0, this.answer_sheet.length);
            this.questions.forEach((question, index_question) => {
                let a_content_array = [];
                if(question.q_type === "multiple")
                {
                    question.q_options.forEach((option, index_option) => {
                        if (option.checked) {
                            a_content_array.push(index_option.toString());
                        }
                        });
                    question.a_content = a_content_array.join(',');
                    //console.log(question.a_content);
                }
 
                this.answer_sheet.push({q_id: question.q_id, a_content: question.a_content});
                });
            console.log(this.answer_sheet);
            const dataObject = { 
                qn_id: this.qn_id,
                as_id: this.as_id,
                answer_data: JSON.stringify(this.answer_sheet)
            };
            const jsonString = JSON.stringify(dataObject);
            console.log(jsonString);
            //上传问卷，跳转。
            this.$api.questionnaire.postAnswer_Submit(jsonString)
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
        },  
        
        save_tips() {
        this.$alert('问卷保存成功！', '保存问卷', {
          confirmButtonText: '确定',
        });
      },

    },

    computed:{
        save_handler()
        {
            return () => {
            this.saveQuestionnaire();
            this.save_tips();
            }
        },
    },





};
</script>
  
<style scoped>
/* 样式代码 */
.sidebar {
    position: fixed;
    top: 4rem;
    left: 0;
    bottom: 0;
    z-index: 100;
    padding: 1rem;
    width: 30%;
    overflow-y: scroll;
    background-color: #ccd2d8;
    /* color: #409EFF; */

    /* display: flex;
    justify-content: flex-start; 
    align-content: start;
    align-items: flex-start;
    flex-direction: row;
    flex-wrap: wrap; */

    display: flex;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap;

}

.outline-area {
    position: fixed;
    top: 4rem;
    left: 82%;
    bottom: 0;
    z-index: 100;
    padding: 1rem;
    width: 20%;
    background-color: #d8e5f3;
    /* overflow-y: scroll;
    background-color: #ccd2d8;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap; */
}

.outline-list {

    top: 6rem;
    left: 10%;
    right: 10%;
    /* height: 90%; */
    height: calc(100% - 6rem);
    z-index: 100;
    padding: 1rem;
    width: 77%;
    overflow-y: scroll;
    background-color: #ffffff;
    /* background-color: #aebac5; */


    /* display: flex;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap; */
}

.outline-title {
    border-radius: 4px;
    background-color: white;
    left: 10%;
    width: 90%;

}

.outline-item {
    box-shadow: none !important;
    /* border: 1px solid #dee2e6 !important; */
    border-radius: 0.25rem !important;
    margin: 0rem;


    display: block;
    padding: 0.5rem;
    text-align: left !important;
    width: 90%;
    /* background-color: #9b5d5d; */
}

.tool {
    box-shadow: none !important;
    border: 1px solid #dee2e6 !important;
    border-radius: 0.25rem !important;
    margin: 0.5rem;
    width: 45%;
    background-color: #ffffff;
    /* height: 10rem; */
}

.tool-body {
    padding: 0.5rem !important;

}

.tool-title {
    font-size: 1rem !important;
    margin-bottom: 0.5rem !important;
}

.tool-text {
    font-size: .875rem !important;
    color: #6c757d !important;
    margin-bottom: 1rem !important;
}

.question-card {
    position: fixed;
    top: 4rem;
    left: 35%;
    bottom: 0;
    z-index: 100;
    padding: 1rem;
    width: 44%;
    overflow-y: scroll;
}

.question-card::-webkit-scrollbar {
    display: none;
}

.card {
    box-shadow: none !important;

    border-radius: 0.25rem !important;


    width: 90%;


    /* margin: 1rem;
    width: 18rem; */

}

.card-body {
    padding: 0.75rem !important;
}

.card-title {
    font-size: 1rem !important;
    margin-bottom: 0.5rem !important;
}

.card-text {
    font-size: .875rem !important;
    color: #6c757d !important;
    margin-bottom: 1rem !important;
}

.btn-primary {
    background-color: #007bff !important;
    border-color: #007bff !important;
}

.btn-primary:hover {
    background-color: #0069d9 !important;
    border-color: #0062cc !important;
}

.btn-danger {
    color: #fff !important;
    background-color: #dc3545 !important;
    border-color: #dc3545 !important;
}

.dragging {
    background-color: #e9ecef;
}

.sorting {
    display: flex;
    flex-direction: column;
}

.option {
    display: flex;
    align-items: center;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 0.25rem;
    cursor: move;
}

.handle {
    margin-left: auto;
    cursor: move;
}

.image-question {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.image-question img {
    border: 2px solid transparent;
}

.image-question img.selected {
    border: 2px solid #007bff;
}

@media (max-width: 991.98px) {
    .sidebar {
        position: static;
        height: auto;
        padding-top: 1rem;
        padding-bottom: 1rem;
        overflow-y: visible;
    }
}

.login {
    width: 600px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
}

.title {
    color: #857e7e;
    font-size: 13px;
}

.red_star {
    color: #ff0000;
    font-size: 13px;
}

.division {
    line-height: 30px;
}

.el-header,
.el-footer {
    background-color: #dbe1e9;
    color: #333;
    text-align: center;
    line-height: 60px;
}

.el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
}

.el-main {
    background-color: rgba(233, 238, 243, .27) !important;
    color: #333;
    text-align: left;
}

body>.el-container {
    margin-bottom: 40px;
    border-radius: 60%;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 320px;
}</style>