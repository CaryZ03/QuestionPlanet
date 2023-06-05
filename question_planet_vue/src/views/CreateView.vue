<template>
    <div class="row">
        <!-- 工具栏 -->
        <el-collapse v-model="activeNames" class="col-md-3 d-none d-lg-block bg-light sidebar">
            <el-collapse-item  name="1" class="tool " >
                <template slot="title">
                  <i class="el-icon-circle-check"></i>单选题
                </template> 
                <div class="tool-body">
                    <!-- <h5 class="tool-title"><i class="el-icon-circle-check"></i>单选题</h5>            -->
                    <!-- <p class="tool-text">问卷中用户只能选中一个选项作为答案。</p> -->
                    <el-tooltip class="item" effect="dark" content="问卷中用户只能选中一个选项作为答案。" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single')" round>添加单选题</el-button>
                    </el-tooltip>
                </div>
            </el-collapse-item>

            <!-- 多选题工具 -->
            <el-collapse-item  name="2" class="tool mb-2">
              <template slot="title">
                <i class="el-icon-circle-check"></i><i class="el-icon-circle-check"></i>多选题
                </template> 
                <div class="tool-body">
                    <!-- <h5 class="tool-title"><i class="el-icon-circle-check"></i><i class="el-icon-circle-check"></i>多选题</h5> -->
                    <!-- <p class="tool-text">问卷中用户可以选中多个选项作为答案。</p> -->
                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('multiple')" round>添加多选题</el-button>

                </div>
            </el-collapse-item>

            <!-- 填空题工具 -->
            <el-collapse-item  name="3" class="tool mb-2">
              <template slot="title">
                <i class="el-icon-edit-outline"></i>填空题
                </template>   
              <div class="tool-body">
                    <!-- <h5 class="tool-title"><i class="el-icon-edit-outline"></i>填空题</h5> -->
                    <!-- <p class="tool-text">问卷中用户需要输入文本信息作为答案。</p> -->
                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('text')" round>添加填空题</el-button>
                </div>
            </el-collapse-item>

            <!-- 评分题工具 -->
            <el-collapse-item  name="4" class="tool mb-2">
              <template slot="title">
                <i class="el-icon-star-off"></i>评分题
                </template>   
                <div class="tool-body">
                    <!-- <h5 class="tool-title"><i class="el-icon-star-off"></i>评分题</h5> -->
                    <!-- <p class="tool-text">问卷中用户需要对某个问题进行打分。</p> -->
                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('rating')" round>添加评分题</el-button>
                </div>
            </el-collapse-item>

            <!-- 排序题工具 -->
            <el-collapse-item  name="5" class="tool mb-2">
              <template slot="title">
                <i class="el-icon-s-data"></i>判断题
              </template>
                <div class="tool-body">
                    <!-- <h5 class="tool-title"><i class="el-icon-s-data"></i>排序题</h5> -->
                    <!-- <p class="tool-text">问卷中用户需要将一组选项按照自己的喜好进行排序。</p> -->
                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('judge')" round>添加判断题</el-button>
                </div>
            </el-collapse-item>

            <!-- 图片选择题工具 -->
            <el-collapse-item name="6" class="tool mb-2">
              <template slot="title">
                <i class="el-icon-picture-outline"></i>图片选择题
              </template>  
              <div class="tool-body">
                    <!-- <h5 class="tool-title"><i class="el-icon-picture-outline"></i>图片选择题</h5> -->
                    <!-- <p class="tool-text">问卷中用户需要从多个图片选项中选择一个。</p> -->
                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('image')" round>添加图片选择题</el-button>
                </div>
            </el-collapse-item>

            <!-- 进度条工具 -->
            <el-collapse-item name="7" class="tool mb-2">
              <template slot="title">
                <i class="el-icon-s-data"></i>进度条
              </template>  
              <div class="tool-body">
                    <!-- <h5 class="tool-title"><i class="el-icon-s-data"></i>进度条</h5> -->
                    <!-- <p class="tool-text">显示当前用户填写问卷的进度。</p> -->
                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        round>添加进度条</el-button>
                </div>
            </el-collapse-item>
    
    </el-collapse>

        <!-- 问题列表 -->
        <div class="question-card" id="question-list">
            <el-container class="card mb-2" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main>
                        <span class="red_star">*&nbsp;</span>
                        <span class="title">问卷标题</span>
                        <el-input placeholder="请输入问卷标题" v-model="qn_title" clearable></el-input>
                    </el-main>
                </el-container>
                <div style="line-height: 30px;">&emsp;</div>

            <el-container class="card mb-2" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main>
                        <span class="red_star">*&nbsp;</span>
                        <span class="title">问卷截止填写时间</span>
                        <br>
                        <el-date-picker
                            v-model="qn_end_time"
                            type="datetime"
                            placeholder="选择日期时间"
                            format="yyyy-MM-dd HH:mm:ss">
                            </el-date-picker>
                    </el-main>
                </el-container>

                <div style="line-height: 30px;">&emsp;</div>

            <div v-for="(question, index) in questions" :key="index" class="card mb-2" v-bind:id="question.id">
                <el-container style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main v-if="question.isEdit">
                        <span class="red_star" v-if="question.q_mandatory">*&nbsp;</span>
                        <span class="red_star" v-else></span>

                        <span v-if="question.q_type === 'single'" style="color: #F3F2F2;">{{ index + 1 }}.单选题</span>
                        <span v-if="question.q_type === 'multiple'" style="color: #F3F2F2;">{{ index + 1 }}.多选题</span>
                        <span v-if="question.q_type === 'text'" style="color: #F3F2F2;">{{ index + 1 }}.填空题</span>
                        <span v-if="question.q_type === 'judge'" style="color: #F3F2F2;">{{ index + 1 }}.判断题</span>
                        <div style="line-height: 30px;">&emsp;</div>

                        <div class="title">标题</div>
                        <el-input placeholder="请输入标题" v-model="question.q_title" clearable></el-input>
                        <div style="line-height: 30px;">&emsp;</div>

                        <div v-if="question.q_type === 'single' || question.q_type === 'multiple'">
                            <div class="division"><span class="title">选项</span></div>
                            <div class="single_choice_ques" v-for="(item, index_item) in question.q_options"
                                :key="index_item">
                                <el-row>
                                    <el-col :span="3">
                                        <div><el-button type="danger" icon="el-icon-minus" circle size="small"
                                                v-on:click="deleteNode(index, index_item)"></el-button></div>
                                    </el-col>
                                    <el-col :span="21">
                                        <div><el-input placeholder="请输入题目内容" v-model="item.label" clearable></el-input>
                                        </div>
                                    </el-col>
                                </el-row>
                            </div>

                            <el-row>
                                <el-col :span="3">
                                    <div><el-button type="primary" icon="el-icon-plus" circle size="small"
                                            v-on:click="addNode(index)"></el-button></div>
                                </el-col>
                                <el-col :span="21">
                                    <div style="line-height: 200%; color: #0099ff;">添加选项</div>
                                </el-col>
                            </el-row>
                        </div>

                        <div v-else-if="question.q_type === 'text'">
                            <div class="division"><span class="title">内容</span></div>
                            <el-input type="textarea" autosize placeholder="请输入内容" v-model="question.a_content"></el-input>
                        </div>

                        <div v-else-if="question.q_type === 'judge'">
                            <div class="division"><span class="title">选项</span></div>
                            <el-radio-group v-model="question.a_content">
                                <el-radio :label="0">错误</el-radio>
                                <el-radio :label="1">正确</el-radio>
                            </el-radio-group>
                        </div>

                        <div style="line-height: 30px;">&emsp;</div>
                        <div class="division"><span class="title">设置</span></div>

                        <el-row>
                            <el-col :span="21">
                                <div style="line-height: 200%; color: #F3F2F2;">此题目必须回答</div>
                            </el-col>
                            <el-col :span="3"><el-switch v-model="question.q_mandatory" active-color="#0099ff"
                                    inactive-color="#c2bdbd"></el-switch></el-col>
                        </el-row>
                    </el-main>

                    <el-main v-else>
                        <span class="red_star" v-if="question.q_mandatory">*&nbsp;</span>
                        <span class="red_star" v-else></span>
                        <span v-if="question.q_type === 'single'" style="color: #F3F2F2;">{{ index + 1 }}.单选题</span>
                        <span v-if="question.q_type === 'multiple'" style="color: #F3F2F2;">{{ index + 1 }}.多选题</span>
                        <span v-if="question.q_type === 'text'" style="color: #F3F2F2;">{{ index + 1 }}.填空题</span>
                        <span v-if="question.q_type === 'judge'" style="color: #F3F2F2;">{{ index + 1 }}.判断题</span>
                        <div style="line-height: 30px;">&emsp;</div>
                        <div style="color: #F3F2F2;">题目：{{ question.q_title }}</div>

                        <div style="line-height: 30px;">&emsp;</div>

                        <div v-if="question.q_type === 'single' || question.q_type === 'multiple'">
                            <div class="division"><span class="title">选项</span></div>
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
                            <div class="division"><span class="title">内容</span></div>
                            <el-input type="textarea" autosize placeholder="请输入内容" v-model="question.a_content"></el-input>
                        </div>

                        <div v-else-if="question.q_type === 'judge'">
                            <div class="division"><span class="title">选项</span></div>
                            <el-radio-group v-model="question.a_content">
                                <el-radio :label="0">错误</el-radio>
                                <el-radio :label="1">正确</el-radio>
                            </el-radio-group>
                        </div>

                    </el-main>
                    <el-footer>
                        <el-button icon="el-icon-folder-checked" circle v-on:click="change_to_save_mode(index)"
                            v-if="question.isEdit"></el-button>
                        <el-button icon="el-icon-edit" circle v-on:click="change_to_edit_mode(index)" v-else></el-button>
                        &emsp;&emsp;&emsp;&emsp;
                        <el-button icon="el-icon-delete" circle v-on:click="removeQuestion(index)"></el-button>
                        &emsp;&emsp;&emsp;&emsp;
                        <el-button icon="el-icon-top" circle v-on:click="upNode(index)"></el-button>
                        &emsp;&emsp;&emsp;&emsp;
                        <el-button icon="el-icon-bottom" circle v-on:click="downNode(index)"></el-button>
                    </el-footer>
                </el-container>

                <div style="line-height: 30px;">&emsp;</div>

            </div>
            <el-button type="success" style="margin: 0 0 0 214px" round v-on:click="save_handler()">保存问卷</el-button>
            <el-button type="primary" round v-on:click="commitQuestionnaire()">提交问卷</el-button>
            
        </div>


        <!-- 问卷大纲区域 -->
        <div class="outline-area">
            <div class="outline-title">问卷大纲</div>
            <div class="outline-list">
                <!-- <ol>
            <li size="medium" v-for="(question, index) in questions" :key="index">{{ question.title }}</li>
          </ol> -->
                <el-link class="outline-item" v-for="(question, index) in questions" :key="index"
                    @click.prevent="scrollToQuestion(question, index)">{{ index + 1 }}.{{ question.title }}</el-link>
            </div>

        </div>

        <router-view></router-view>
    </div>
</template>
  
<script>
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
            qn_title: "",
            qn_description: "",
            qn_end_time: '',
            qn_refillable: true,
            questions: [],
            activeNames: ['1','2','3','4','5','6','7']
        };
    },
    created() {
        this.qn_id = this.$route.params.qn_id;
        this.load_qn();
    },
    methods: {
        load_qn()
        {   
            var _this = this;
            this.$api.questionnaire.getQuestionnaire_Check(this.$route.params.qn_id)
            .then(function (response) {
            console.log(response);
            console.log(response.data.qn_info);
            console.log(response.data.question_list);
            const qn_info = JSON.parse(response.data.qn_info);
            const qn_list = response.data.question_list;
            console.log(qn_info);
            _this.qn_title = qn_info.qn_title;
            _this.qn_end_time = qn_info.qn_end_time;
            _this.qn_description = qn_info.qn_description;
            _this.qn_refillable = qn_info.qn_refillable;
            qn_list.forEach(question => {
                const item = JSON.parse(question);
                item.q_options = JSON.parse(item.q_options);
                item.isEdit = true;
                _this.questions.push(item);
            })
            //_this.questions = qn_list;
            })
            .catch(function (error) {
            console.log(error);
            });
            console.log(this.qn_id);
        },
        // 添加问题
        addQuestion(q_type) {
            let question = {
                q_type: q_type,
                isEdit: true,
                q_mandatory: true,
                q_title: "",
                q_options: [],
                q_description: "",
                a_content: "",
                q_correct_answer: "",
                score: 0.0,
                stars: [false, false, false, false, false],
            };
            if (q_type === "single" || q_type === "multiple") {
                question.q_options = [
                    { label: "选项1", checked: false ,num: 0},
                    { label: "选项2", checked: false ,num: 0},
                ];
            } else if (q_type === "rating") {
                question.stars = [false, false, false, false, false];
            }
            // 为题目卡片动态生成唯一 ID
            question.id = 'question-' + (this.questions.length + 1);
            this.questions.push(question);
        },
        
        commitQuestionnaire(){
            this.saveQuestionnaire();
            this.$router.push({
                path: "/new/" + this.$store.state.curUserID
            })
        },
        //保存试卷
        saveQuestionnaire(){
            const selectedQuestions = this.questions.map(question => {
            // 选择要包含在 JSON 数据中的属性
            return {
                q_type: question.q_type,
                q_mandatory: question.q_mandatory,
                q_title: question.q_title,
                q_description: question.q_description,
                q_option_count: question.q_options.length,
                q_options: question.q_options,
                q_correct_answer: question.q_correct_answer,
                q_score: question.q_score,
            };
            });
            const isoString = this.qn_end_time;
            const date = new Date(isoString);

            const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
            const dateString = date.toLocaleDateString('en-US', options).replace(/\//g, '-');
            const timeString = date.toLocaleTimeString('en-US', {hour12:false});

            const formattedDate = `${dateString.split('-').reverse().join('-')} ${timeString}`;

            const dataObject = { 
                uid: this.$store.curUserID,
                qn_id: this.qn_id,
                qn_title: this.qn_title,
                qn_description: this.qn_description,
                qn_end_time: formattedDate,
                qn_refillable: this.qn_refillable,
                question_list: selectedQuestions,
            };
            const jsonString = JSON.stringify(dataObject);
            console.log(jsonString);
            // axios({
            //     method: 'post',
            //     url: 'http://182.92.102.246:1145/api/questionnaire//save_questionnaire',
            //     headers: {
            //         'Content-Type': 'application/json'
            //     },
            //     data: jsonString
            // })
            this.$api.questionnaire.postQuestionnaire_Save(jsonString)
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
            /*
            const filename = 'data.json';

            const blob = new Blob([jsonString], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            
            const link = document.createElement('a');
            link.href = url;
            link.download = filename;
            link.click();
            URL.revokeObjectURL(url);*/

        },

        save_tips() {
        this.$alert('问卷保存成功！', '保存问卷', {
          confirmButtonText: '确定',
        });
      },
        // 选择题添加选项
        addNode(index) {
            this.questions[index].q_options.push({ label: "选项", checked: false });
        },
        //删除样本div
        deleteNode(index, i) {
            this.questions[index].q_options.splice(i, 1);  //删除index为i,位置的数组元素
        },
        // 题目上移
        upNode(i) {
            if (i <= 0) return

            [this.questions[i - 1], this.questions[i]] = [this.questions[i], this.questions[i - 1]]

            this.$forceUpdate()
        },
        //题目下移
        downNode(i) {
            if (i >= this.questions.length - 1) return

            [this.questions[i + 1], this.questions[i]] = [this.questions[i], this.questions[i + 1]]

            this.$forceUpdate()
        },

        //退出编辑模式
        change_to_save_mode(index) {
            this.questions[index].isEdit = false;
        },

        //退出编辑模式
        change_to_edit_mode(index) {
            this.questions[index].isEdit = true;
        },

        // 删除问题
        removeQuestion(index) {
            this.questions.splice(index, 1);
        },

        // 评分题选择星星
        selectStar(question, starIndex) {
            for (let i = 0; i < question.stars.length; i++) {
                if (i <= starIndex) {
                    question.stars.splice(i, 1, true);
                } else {
                    question.stars.splice(i, 1, false);
                }
            }
        },

        // 排序题拖动事件
        dragStart(event, question, option) {
            event.preventDefault();
            event.stopPropagation();
            event.dataTransfer.setData("text/plain", "");
            event.target.parentElement.classList.add("dragging");
            this.dragOption = option;
            this.dragQuestion = question;
        },
        dragEnd(event, question, option) {
            event.preventDefault();
            event.stopPropagation();
            event.target.parentElement.classList.remove("dragging");
            let newIndex = question.options.indexOf(option);
            let oldIndex = question.options.indexOf(this.dragOption);
            if (newIndex > oldIndex) {
                question.options.splice(newIndex + 1, 0, this.dragOption);
            } else {
                question.options.splice(newIndex, 0, this.dragOption);
            }
            question.options.splice(oldIndex, 1);
            this.dragOption = null;
            this.dragQuestion = null;
        },

        // 图片选择题选择图片
        selectImage(question, index) {
            question.images.forEach((image, imageIndex) => {
                if (index === imageIndex) {
                    image.selected = true;
                } else {
                    image.selected = false;
                }
            });
        },






        scrollToQuestion(question, index) {

            this.$nextTick(() => {

                //获取锚点值
                const hash = '.outline-item #question-' + (index + 1);


                // 查找对应的问题卡片元素
                //const questionCard = document.querySelector(hash);
                const questionCard = document.getElementById(question.id);
                console.log(questionCard);
                // const questionCard = document.querySelector(hash);
                if (!questionCard) {
                    return;
                }
                // // 滚动到可视区域
                // questionCard.scrollIntoView({ behavior: "smooth" });
                questionCard.scrollIntoView({ behavior: "smooth" });
            })

        }




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
    background-color: rgba(212, 219, 224, .18) !important;

    /* color: #409EFF; */

    /* display: flex;
    justify-content: flex-start; 
    align-content: start;
    align-items: flex-start;
    flex-direction: row;
    flex-wrap: wrap; */

    /* display: flex;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap; */

}

.el-collapse-item__header.is-active{
    background-color: #0069d9;
}

.sidebar::-webkit-scrollbar {
    display: none;
}
.outline-area {
    position: fixed;
    top: 4rem;
    left: 82%;
    bottom: 0;
    z-index: 100;
    padding: 1rem;
    width: 20%;
    background-color: #d8e5f327;
    /* overflow-y: scroll;
    background-color: #ccd2d8;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap; */
    box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0, rgba(27, 31, 35, 0.15) 0 0 0 1px;
}

.outline-list::-webkit-scrollbar {
    display: none;
}
.outline-list {

    top: 6rem;
    left: 10%;
    right: 10%;
    /* height: 90%; */
    height: calc(100% - 6rem);
    z-index: 100;
    padding: 1rem;
    width: 90%;
    overflow-y: scroll;
    background-color: #ffffff48;
    /* background-color: #aebac5; */

    color: #e9ecef;
    /* display: flex;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap; */
    box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0, rgba(27, 31, 35, 0.15) 0 0 0 1px;
}

.outline-title {
    border-radius: 4px;
    background-color: rgba(255, 255, 255, 0.274);
    left: 10%;
    width: 90%;
    box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0, rgba(27, 31, 35, 0.15) 0 0 0 1px;
    font-size: 16px;
    text-align: center;
    color: #fff;
}

.outline-item {
    box-shadow: none !important;
    /* border: 1px solid #dee2e6 !important; */
    border-radius: 0.25rem !important;
    margin: 0rem;

    color: #fff;
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
    width: 95%;
    background-color: rgba(0, 0, 0, 0.55);
    /* height: 10rem; */
}

.tool-body {
    padding: 0.5rem !important;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap;
    background-color: rgba(255, 255, 255, 0.103);
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
    width: 30%;
    margin: 1%;
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
    color: #F3F2F2;
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
    background-color: rgba(219, 225, 233, .73) !important;
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
}

</style>

