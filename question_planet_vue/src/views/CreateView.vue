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
                            @click="addQuestion('single',0)" round>添加单选题</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="您的性别" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',1)" round>性别</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="你玩原神吗" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',2)" round>原神</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="婚姻情况" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',3)" round>婚姻情况</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="工作状态" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',4)" round>工作状态</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="交通工具" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',5)" round>交通工具</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="电影" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',6)" round>电影</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="运动" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',7)" round>运动</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="使用手机时长" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('single',8)" round>使用手机时长</el-button>
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
                    <el-tooltip class="item" effect="dark" content="问卷中用户可以选中多个选项作为答案" placement="bottom">
                         <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('multiple',0)" round>添加多选题</el-button>
                    </el-tooltip>
                   
                    

                    <el-tooltip class="item" effect="dark" content="喜欢的原神角色" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('multiple',1)" round>原神角色</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="运动" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('multiple',2)" round>运动</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="网站" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('multiple',3)" round>网站</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="音乐" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('multiple',4)" round>音乐</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="交通工具" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('multiple',5)" round>交通工具</el-button>
                    </el-tooltip>

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
                    <el-tooltip class="item" effect="dark" content="问卷中用户需要输入文本信息作为答案" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('text',0)" round>添加填空题</el-button>
                    </el-tooltip>
                    

                    <el-tooltip class="item" effect="dark" content="姓名" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('text',1)" round>姓名</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="学号" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('text',2)" round>学号</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="原神UID" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('text',3)" round>原神UID</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="家庭住址" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('text',4)" round>家庭住址</el-button>
                    </el-tooltip>

                    <el-tooltip class="item" effect="dark" content="手机号" placement="bottom">
                        <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                            @click="addQuestion('text',5)" round>手机号</el-button>
                    </el-tooltip>
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
                        @click="addQuestion('grade',0)" round>添加评分题</el-button>

                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('grade',1)" round>模板1</el-button>

                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('grade',2)" round>模板2</el-button>
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
                        @click="addQuestion('judge',0)" round>添加判断题</el-button>

                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('judge',1)" round>模板1</el-button>
                    
                    <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" size="small"
                        @click="addQuestion('judge',2)" round>模板2</el-button>
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
                        <span class="title">问卷描述</span>
                        <el-input placeholder="请输入问卷描述" v-model="qn_description" clearable></el-input>
                    </el-main>
                </el-container>
                <div style="line-height: 30px;">&emsp;</div>
            
                <el-container class="card mb-2" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main>
                        <span class="red_star">*&nbsp;</span>
                        <span class="title">问卷类型</span>
                        <br>
                        <el-select v-model="qn_type" placeholder="请选择" @change="updateQnType">
                        <el-option
                        v-for="item in qn_type_options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
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
                            default-time="12:00:00"
                            format="yyyy-MM-dd HH:mm:ss">
                            </el-date-picker>
                    </el-main>
                </el-container>

                <div style="line-height: 30px;">&emsp;</div>

            <div v-for="(question, index) in questions" :key="index" class="card mb-2" :id="index">
                <el-container style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main v-if="question.isEdit">
                        <div v-if="qn_is_normal || qn_is_test">
                            <span class="red_star" v-if="question.q_mandatory">*&nbsp;</span>
                            <span class="red_star" v-else></span>
                            <span v-if="question.q_type === 'single'" style="color: #F3F2F2;">{{ index + 1 }}.单选题</span>
                            <span v-if="question.q_type === 'multiple'" style="color: #F3F2F2;">{{ index + 1 }}.多选题</span>
                            <span v-if="question.q_type === 'text'" style="color: #F3F2F2;">{{ index + 1 }}.填空题</span>
                            <span v-if="question.q_type === 'judge'" style="color: #F3F2F2;">{{ index + 1 }}.判断题</span>
                            <span v-if="question.q_type === 'grade'" style="color: #F3F2F2;">{{ index + 1 }}.打分题</span>
                        </div>
                        <div v-else-if="qn_is_vote">
                            <span style="color: #F3F2F2;">投票</span>
                        </div>
                        <div v-else-if="qn_is_application">
                            <span style="color: #F3F2F2;">报名</span>
                        </div>

                        <div style="line-height: 30px;">&emsp;</div>

                        <div class="title">标题</div>
                        <el-input placeholder="请输入标题" v-model="question.q_title" clearable></el-input>
                        <div style="line-height: 30px;">&emsp;</div>

                        <div class="title">问题描述</div>
                        <el-input placeholder="请输入问题描述" v-model="question.q_description" clearable></el-input>
                        <div style="line-height: 30px;">&emsp;</div>

                        <div v-if="question.q_type === 'single' || question.q_type === 'multiple'">
                            <div v-if="qn_is_application">
                                <div class="division"><span class="title">选项&报名个数</span></div>
                                <div class="single_choice_ques" v-for="(item, index_item) in question.q_options"
                                    :key="index_item">
                                    <el-row>
                                        <el-col :span="3">
                                            <div><el-button type="danger" icon="el-icon-minus" circle size="small"
                                                    v-on:click="deleteNode(index, index_item)"></el-button></div>
                                        </el-col>
                                        <el-col :span="14">
                                            <div><el-input placeholder="请输入题目内容" v-model="item.label" clearable></el-input>
                                            </div>
                                        </el-col>
                                        <el-col :span="1">
                                            &nbsp;
                                        </el-col>
                                        <el-col :span="6">
                                            <div><el-input placeholder="请输入报名个数" v-model.number="item.num" clearable type="number"></el-input>
                                            </div>
                                        </el-col>
                                    </el-row>
                                </div>
                            </div>    
                            <div v-else>
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
                                <el-radio :label="0" style="color: #F3F2F2;">错误</el-radio>
                                <el-radio :label="1" style="color: #F3F2F2;">正确</el-radio>
                            </el-radio-group>
                        </div>

                        <div v-else-if="question.q_type === 'grade'">
                            <div class="division"><span class="title">评分</span></div>
                            <el-rate
                                v-model="question.a_content"
                                :colors="grade_colors">
                            </el-rate>
                        </div>

                        <div style="line-height: 30px;">&emsp;</div>

                        <div v-if="qn_is_test && (question.q_type === 'single' || question.q_type === 'multiple')">
                            <span class="red_star">*&nbsp;</span>
                            <span class="title">正确答案</span>
                        <el-input placeholder="请输入正确答案" v-model="question.q_correct_answer" clearable></el-input>
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
                        <div v-if="qn_is_normal || qn_is_test">
                            <span class="red_star" v-if="question.q_mandatory">*&nbsp;</span>
                            <span class="red_star" v-else></span>
                            <span v-if="question.q_type === 'single'" style="color: #F3F2F2;">{{ index + 1 }}.单选题</span>
                            <span v-if="question.q_type === 'multiple'" style="color: #F3F2F2;">{{ index + 1 }}.多选题</span>
                            <span v-if="question.q_type === 'text'" style="color: #F3F2F2;">{{ index + 1 }}.填空题</span>
                            <span v-if="question.q_type === 'judge'" style="color: #F3F2F2;">{{ index + 1 }}.判断题</span>
                            <span v-if="question.q_type === 'grade'" style="color: #F3F2F2;">{{ index + 1 }}.打分题</span>
                        </div>
                        <div v-else-if="qn_is_vote">
                            <span style="color: #F3F2F2;">投票</span>
                        </div>
                        <div v-else-if="qn_is_application">
                            <span style="color: #F3F2F2;">报名</span>
                        </div>
                        <div style="line-height: 30px;">&emsp;</div>
                        <div style="color: #F3F2F2;">题目：{{ question.q_title }}</div>
                        <div style="line-height: 30px;">&emsp;</div>
                        <div style="color: #F3F2F2;">问题描述：{{ question.q_description }}</div>

                        <div style="line-height: 30px;">&emsp;</div>

                        <div v-if="qn_is_application">
                            <div v-if="question.q_type === 'single' || question.q_type === 'multiple'">
                                <div class="division"><span class="title">选项</span></div>
                                <div v-if="question.q_type === 'single'">
                                    <el-radio-group v-model="question.a_content">
                                        <el-radio v-for="(option, index_option) in question.q_options" :label="index_option"
                                            :key="index_option" :disabled="option.disabled"
                                            style="color: #F3F2F2;">{{ option.label }} &nbsp;&nbsp; 剩余人数：{{ option.num }}</el-radio>
                                        
                                    </el-radio-group>
                                </div>

                                <div v-if="question.q_type === 'multiple'">
                                    <div v-for="(option, index_option) in question.q_options" :key="index_option">
                                        <el-checkbox :label="index_option" v-model="option.checked" style="color: #F3F2F2;">{{ option.label
                                        }}&nbsp;&nbsp; 剩余人数：{{ option.num }}</el-checkbox>
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
                        </div>
                        <div v-else>
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
                        </div>

                    </el-main>
                    <el-footer>
                        <el-button icon="el-icon-folder-checked" circle v-on:click="change_to_save_mode(index)"
                            v-if="question.isEdit"></el-button>
                        <el-button icon="el-icon-edit" circle v-on:click="change_to_edit_mode(index)" v-else></el-button>
                        &emsp;&emsp;&emsp;&emsp;
                        <el-button icon="el-icon-document-copy" circle v-on:click="dup_question(index)"></el-button>
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
            <el-button type="success" style="margin: 0 0 0 214px" round v-on:click="save_questionnaire()">保存问卷</el-button>
            <el-button type="primary" round v-on:click="submit_questionnaire()">提交问卷</el-button>
            
        </div>


        <!-- 问卷大纲区域 -->
        <div class="outline-area">
            <div class="outline-title">问卷大纲</div>
            <div class="outline-list">
                <!-- <ol>
            <li size="medium" v-for="(question, index) in questions" :key="index">{{ question.title }}</li>
          </ol> -->
                <el-link class="outline-item" v-for="(question, index) in questions" :key="index"
                    @click.prevent="scrollToQuestion(question, index)">{{ index + 1 }}.{{ question.q_title }}</el-link>
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
            qn_type: "normal",
            qn_type_options: [
                {value: 'normal', label: '普通问卷'},
                {value: 'test', label: '考试问卷'},
                {value: 'vote', label: '投票问卷'},
                {value: 'application', label: '报名问卷'},
            ],
            qn_description: "",
            qn_end_time: '',
            qn_refillable: true,
            questions: [],
            activeNames: ['1','2','3','4','5','6','7'],
            grade_colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
            qn_is_normal: false,
            qn_is_test: false,
            qn_is_vote: false,
            qn_is_application: true,
        };
    },
    created() {
        this.qn_id = this.$route.params.qn_id;
        this.load_qn();
    },
    methods: {
        change_to_qn_normal(){
            this.qn_is_normal = true;
            this.qn_is_test = false;
            this.qn_is_vote = false;
            this.qn_is_application = false;
        },
        
        change_to_qn_test(){
            this.qn_is_normal = false;
            this.qn_is_test = true;
            this.qn_is_vote = false;
            this.qn_is_application = false;
        },

        change_to_qn_vote(){
            this.qn_is_normal = false;
            this.qn_is_test = false;
            this.qn_is_vote = true;
            this.qn_is_application = false;
        },

        change_to_qn_application(){
            this.qn_is_normal = false;
            this.qn_is_test = false;
            this.qn_is_vote = false;
            this.qn_is_application = true;
        },

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
            _this.qn_type = qn_info.qn_type;
            if(_this.qn_type === "normal")
            {
                _this.change_to_qn_normal();
            }
            else if(_this.qn_type === "test")
            {
                _this.change_to_qn_test();
            }
            if(_this.qn_type === "vote")
            {
                _this.change_to_qn_vote();
            }
            if(_this.qn_type === "application")
            {
                _this.change_to_qn_application();
            }
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
        addQuestion(q_type, option) {
            if (this.qn_type === "vote")
            {
                this.$message({
                message: '警告哦，在投票问卷下无法自由添加题目',
                type: 'warning'
                });
                return;
            }
            else if (this.qn_type === "application")
            {
                this.$message({
                message: '警告哦，在报名问卷下无法自由添加题目',
                type: 'warning'
                });
                return;
            };
            let question = {
                q_type: q_type,
                isEdit: true,
                q_mandatory: true,
                q_title: "标题",
                q_options: [],
                q_description: "",
                a_content: "",
                q_correct_answer: "",
                q_score: 0.0,
            };
            if (q_type === "single" ) {
                if(option == 0){
                    question.q_options = [
                    { label: "选项1", checked: false ,num: 0},
                    { label: "选项2", checked: false ,num: 0},
                ];
                }
                else if( option ==1){
                    question.q_title = "您的性别"
                    question.q_options = [
                    { label: "男", checked: false ,num: 0},
                    { label: "女", checked: false ,num: 0},
                ];
                }
                else if( option ==2){
                    question.q_title = "你玩原神吗"
                    question.q_options = [
                    { label: "原神，启动！", checked: false ,num: 0},
                    { label: "不玩", checked: false ,num: 0},
                ];
                }
                else if( option ==3){
                    question.q_title = "婚姻状况"
                    question.q_options = [
                    { label: "未婚", checked: false ,num: 0},
                    { label: "已婚", checked: false ,num: 0},
                    { label: "离异", checked: false ,num: 0},
                ];
                }
                else if(option ==4){
                    question.q_title = "您的工作状态"
                    question.q_options = [
                        { label: "在职", checked: false ,num: 0},
                        { label: "待业", checked: false ,num: 0},
                        { label: "自由职业", checked: false ,num: 0},
                        { label: "退休", checked: false ,num: 0},
                    ];
                }
                else if(option == 5){
                    question.q_title = "你平时使用的交通工具"
                    question.q_options = [
                        { label: "公共交通", checked: false ,num: 0},
                        { label: "私家车", checked: false ,num: 0},
                        { label: "共享单车", checked: false ,num: 0},
                        { label: "步行/自行车", checked: false ,num: 0},
                    ];
                }
                else if(option == 6){
                    question.q_title = "你平时喜欢看什么类型的电影"
                    question.q_options = [
                        { label: "动作片", checked: false ,num: 0},
                        { label: "喜剧片", checked: false ,num: 0},
                        { label: "科幻片", checked: false ,num: 0},
                        { label: "爱情片", checked: false ,num: 0},
                        { label: "恐怖片", checked: false ,num: 0},
                        { label: "纪录片", checked: false ,num: 0},
                        { label: "其他", checked: false ,num: 0},
                    ];
                }
                else if(option == 7){
                    question.q_title = "你最喜欢的运动类型是"
                    question.q_options = [
                        { label: "足球", checked: false ,num: 0},
                        { label: "篮球", checked: false ,num: 0},
                        { label: "羽毛球", checked: false ,num: 0},
                        { label: "跑步", checked: false ,num: 0},
                        { label: "游泳", checked: false ,num: 0},
                        { label: "健身", checked: false ,num: 0},
                        { label: "其他", checked: false ,num: 0},
                    ];
                }
                else if(option == 8){
                    question.q_title = "你每天会花多长时间看手机"
                    question.q_options = [
                        { label: "不到1小时", checked: false ,num: 0},
                        { label: "1-2小时", checked: false ,num: 0},
                        { label: "2-3小时", checked: false ,num: 0},
                        { label: "3小时以上", checked: false ,num: 0},
                    ];
                }
            }
            else if(q_type === "multiple"){
                if(option == 0){
                    question.q_options = [
                    { label: "选项1", checked: false ,num: 0},
                    { label: "选项2", checked: false ,num: 0},
                ];
                }
                else if(option ==1){
                    question.q_title = "你喜欢的原神角色"
                    question.q_options = [
                        { label: "神里绫华", checked: false ,num: 0},
                        { label: "胡桃", checked: false ,num: 0},
                        { label: "琴", checked: false ,num: 0},
                        { label: "七七", checked: false ,num: 0},
                        { label: "迪卢克", checked: false ,num: 0},
                        { label: "可莉", checked: false ,num: 0},
                        { label: "宵宫", checked: false ,num: 0},
                        { label: "其他", checked: false ,num: 0}
                    ];
                }
                else if(option == 2){
                    question.q_title = "你平时喜欢做哪些运动"
                    question.q_options = [
                        { label: "跑步", checked: false ,num: 0},
                        { label: "游泳", checked: false ,num: 0},
                        { label: "打羽毛球", checked: false ,num: 0},
                        { label: "健身", checked: false ,num: 0},
                        { label: "骑自行车", checked: false ,num: 0},
                        { label: "其他", checked: false ,num: 0}
                    ];
                }
                else if(option==3){
                    question.q_title = "请选择你经常去的网站"
                    question.q_options = [
                        { label: "新闻", checked: false ,num: 0},
                        { label: "社交媒体", checked: false ,num: 0},
                        { label: "购物", checked: false ,num: 0},
                        { label: "视频流媒体", checked: false ,num: 0},
                        { label: "游戏", checked: false ,num: 0},
                        { label: "其他", checked: false ,num: 0}
                    ];
                }
                else if(option ==4){
                    question.q_title = "你喜欢的音乐类型"
                    question.q_options = [
                        { label: "流行", checked: false ,num: 0},
                        { label: "摇滚", checked: false ,num: 0},
                        { label: "电子", checked: false ,num: 0},
                        { label: "古典", checked: false ,num: 0},
                        { label: "嘻哈", checked: false ,num: 0},
                        { label: "其他", checked: false ,num: 0}
                    ];
                }
                else if(option == 5){
                    question.q_title = "你平时使用的交通工具"
                    question.q_options = [
                        { label: "公共交通", checked: false ,num: 0},
                        { label: "私家车", checked: false ,num: 0},
                        { label: "共享单车", checked: false ,num: 0},
                        { label: "步行/自行车", checked: false ,num: 0},
                    ];
                }
            }
            else if(q_type === 'text'){
                if(option == 1){
                    question.q_title = "你的姓名是？"
                }
                else if(option == 2){
                    question.q_title = "你的学号是？"
                }
                else if(option == 3){
                    question.q_title = "你的原神UID是？"
                }
                else if(option == 4){
                    question.q_title = "你的家庭地址是？"
                }
                else if(option == 5){
                    question.q_title = "你的手机号是？"
                }
            }
            else if(q_type === 'grade'){
                if(option == 1){
                    question.q_title = "你对原神的喜爱程度"
                }
                else if(option == 2){
                    question.q_title = "你对xxx老师的评价"
                }
            }
            else if(q_type === 'judge'){
                if( option == 1){
                    question.q_title = "原神是世界第一吗"
                }
                else if( option == 2){
                    question.q_title = "你是否会向你的朋友推荐本产品"
                }
            }

            // 为题目卡片动态生成唯一 ID
            question.id = 'question-' + (this.questions.length + 1);
            this.questions.push(question);
        },

        //保存试卷
        save_handler(){
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

            // 调整日期格式
            const [YYYY, MM, DD] = dateString.split('-');
            const formattedDate = `${DD}-${MM}-${YYYY} ${timeString}`;
            console.log(formattedDate);   // 输出： 19-04-2023 20:06:11


            const dataObject = { 
                uid: this.$store.curUserID,
                qn_id: this.qn_id,
                qn_title: this.qn_title,
                qn_description: this.qn_description,
                qn_type: this.qn_type,
                qn_end_time: formattedDate,
                qn_refillable: this.qn_refillable,
                question_list: selectedQuestions,
            };
            const jsonString = JSON.stringify(dataObject);
            console.log(jsonString);
            this.$api.questionnaire.postQuestionnaire_Save(jsonString)
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });            
        },

        save_questionnaire() {
            this.save_handler();
            this.$alert('问卷保存成功！', '保存问卷', {
            confirmButtonText: '确定',
            });
        },

        submit_questionnaire() {
            this.$confirm('是否提交问卷?', '提交问卷', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {

                this.$message({
                    type: 'success',
                    message: '提交成功!'
                });
                this.save_handler();
                this.$router.push({
                path: "/manage/" + this.$store.state.curUserID
                });
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消提交'
                });          
            });
        },

        // 选择题添加选项
        addNode(index) {
            if(this.qn_is_application)
            {
                this.questions[index].q_options.push({ label: "选项", checked: false , num: 0, disabled: false});
            }
            else
            {
                this.questions[index].q_options.push({ label: "选项", checked: false , num: 0});
            }
        },
        //删除样本div
        deleteNode(index, i) {
            this.questions[index].q_options.splice(i, 1);  //删除index为i,位置的数组元素
        },
        //复制问题
        dup_question(index) {
            if (this.qn_type === "vote")
            {
                this.$message({
                message: '警告哦，在投票问卷下无法自由复制题目',
                type: 'warning'
                });
                return;
            }
            else if (this.qn_type === "application")
            {
                this.$message({
                message: '警告哦，在报名问卷下无法自由复制题目',
                type: 'warning'
                });
                return;
            };
            let question = {
                q_type: this.questions[index].q_type,
                isEdit: true,
                q_mandatory: this.questions[index].q_mandatory,
                q_title: this.questions[index].q_title,
                q_options: this.questions[index].q_options,
                q_description: this.questions[index].q_description,
                a_content: this.questions[index].a_content,
                q_correct_answer: this.questions[index].q_correct_answer,
                q_score: this.questions[index].q_score,
            };
            console.log(question);
            this.questions.splice(index, 0, question);
        },
        // 题目上移
        upNode(i) {
            if (this.qn_type === "vote")
            {
                this.$message({
                message: '警告哦，在投票问卷下无法上移题目',
                type: 'warning'
                });
                return;
            }
            else if (this.qn_type === "application")
            {
                this.$message({
                message: '警告哦，在报名问卷下无法上移题目',
                type: 'warning'
                });
                return;
            };
            if (i <= 0) return

            [this.questions[i - 1], this.questions[i]] = [this.questions[i], this.questions[i - 1]]

            this.$forceUpdate()
        },
        //题目下移
        downNode(i) {
            if (this.qn_type === "vote")
            {
                this.$message({
                message: '警告哦，在投票问卷下无法下移题目',
                type: 'warning'
                });
                return;
            }
            else if (this.qn_type === "application")
            {
                this.$message({
                message: '警告哦，在报名问卷下无法下移题目',
                type: 'warning'
                });
                return;
            };
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
            if (this.qn_type === "vote")
            {
                this.$message({
                message: '警告哦，在投票问卷下无法自由删除题目',
                type: 'warning'
                });
                return;
            }
            else if (this.qn_type === "application")
            {
                this.$message({
                message: '警告哦，在报名问卷下无法自由删除题目',
                type: 'warning'
                });
                return;
            };
            this.questions.splice(index, 1);
        },

        updateQnType() {
            console.log("当前选择的题目类型是： ",this.qn_type);
            if(this.qn_type === "vote")
            {
                this.change_to_qn_vote();
                this.questions.splice(0, this.questions.length);
                let question = {
                    q_type: "single",
                    isEdit: true,
                    q_mandatory: true,
                    q_title: "",
                    q_options: [],
                    q_description: "",
                    a_content: "",
                    q_correct_answer: "",
                    q_score: 0.0,
                };
                question.q_options = [
                    { label: "选项1", checked: false ,num: 0},
                    { label: "选项2", checked: false ,num: 0},
                ];
                // 为题目卡片动态生成唯一 ID
                question.id = 'question-' + (this.questions.length + 1);
                this.questions.push(question);
            }
            else if(this.qn_type === "application")
            {
                this.change_to_qn_application();
                this.questions.splice(0, this.questions.length);
                let question_name = {
                    q_type: "text",
                    isEdit: true,
                    q_mandatory: true,
                    q_title: "个人信息",
                    q_options: [],
                    q_description: "",
                    a_content: "",
                    q_correct_answer: "",
                    q_score: 0.0,
                };
                // 为题目卡片动态生成唯一 ID
                question_name.id = 'question-' + (this.questions.length + 1);
                this.questions.push(question_name);
                let question = {
                    q_type: "single",
                    isEdit: true,
                    q_mandatory: true,
                    q_title: "",
                    q_options: [],
                    q_description: "",
                    a_content: "",
                    q_correct_answer: "",
                    q_score: 0.0,
                };
                question.q_options = [
                    { label: "选项1", checked: false ,num: 0, disabled: false},
                    { label: "选项2", checked: false ,num: 0, disabled: false},
                ];
                // 为题目卡片动态生成唯一 ID
                question.id = 'question-' + (this.questions.length + 1);
                this.questions.push(question);
            }
            else if(this.qn_type === "normal")
            {
                this.change_to_qn_normal();
            }
            else if(this.qn_type === "test")
            {
                this.change_to_qn_test();
            }
        },

        scrollToQuestion(question, index) {

            this.$nextTick(() => {

                //获取锚点值
                const hash = '.outline-item #question-' + (index + 1);


                // 查找对应的问题卡片元素
                //const questionCard = document.querySelector(hash);
                // console.log(question)
                // console.log(question.q_id)
                console.log(index)
                const questionCard = document.getElementById(index);
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

