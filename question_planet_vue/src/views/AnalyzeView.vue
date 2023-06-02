<template>
    <div class="row">
      
      <!-- 问题列表 -->
      <div class="question-card" id="question-list">
        <div>
        <h2 style="margin: 0 0 0 -70px; text-align: center;">{{ qn_title }}</h2>
        </div>

        <div v-for="(question, index) in questions" :key="index" class="card mb-2">
          <el-container style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
          <el-main>
            <span>第{{ index + 1 }}题：{{ question.q_title }}&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span v-if="question.q_type === 'single'" class="question-type">[单选题]</span>
            <span v-if="question.q_type === 'multiple'" class="question-type">[多选题]</span>
            <span v-if="question.q_type === 'text'" class="question-type">[填空题]</span>
            <span v-if="question.q_type === 'judge'" class="question-type">[判断题]</span>
            <div style="line-height: 30px;">&emsp;</div>
            
            <el-table
            :data="question.q_options"
            style="width: 100%"
            show-summary
            :default-sort = "{prop: 'label.label', order: 'ascending'}"
            v-if="question.q_type === 'single' || question.q_type === 'multiple'"
            >
              <el-table-column
                prop="label.label"
                label="选项"
                sortable
                width="500">
              </el-table-column>
              <el-table-column
                prop="num"
                label="小计"
                sortable
                width="140">
              </el-table-column>
              <el-table-column
                label="比例"
                width="100">
                <template slot-scope="scope">
                {{ calculatePercentage(scope.row.num, a_count) }}
                </template>
              </el-table-column>

            </el-table>
  
            <div v-if="question.q_type === 'text'">
              <div class="division"><span class="title">内容</span></div>
              <el-input type="textarea" autosize placeholder="请输入内容" v-model="question.a_content"></el-input>
            </div>
  
          </el-main>
          <el-footer>
              <el-button type="primary" round v-on:click="change_to_bar(index)">柱状图</el-button>          
              &emsp;&emsp;
              <el-button type="primary" round v-on:click="change_to_line(index)">折线图</el-button>
              &emsp;&emsp;
              <el-button type="primary" round v-on:click="change_to_pie(index)">饼状图</el-button>
              &emsp;&emsp;
              <el-button type="primary" round v-on:click="change_to_ring(index)">圆环图</el-button>
          </el-footer>
            <div class="echart" :id="'barChart-' + index" :style="myChartStyle"></div>
            <div class="echart" :id="'lineChart-' + index" :style="myChartStyle"></div>
            <div class="echart" :id="'pieChart-' + index" :style="myChartStyle"></div>
            <div class="echart" :id="'ringChart-' + index" :style="myChartStyle"></div>
          
          
          
          </el-container>
  
          <div style="line-height: 30px;">&emsp;</div>
          
  
        </div>
      </div>
    
  
    </div>
  </template>
  
  <script>
  import * as echarts from "echarts";
  import axios from 'axios';
  // const vm = new Vue({
  //   el: '#question-list',
  //   data:{
  //     seen:true
  //   }
  // }
  // )
  
  

  export default {
    data() {
      return {
        qn_title: "这是一个问卷名称",
        isBar: true,
        isLine: false,
        isPie: false,
        isRing: false,
        a_count: 0,
        questions: [
          {
          type: "single",
          isEdit: true,
          isMandatory: true,
          title: "问题名称1",
          options: [
            { label: "选项1", checked: false, num: 15 },
            { label: "选项2", checked: false, num: 20 },
            { label: "选项3", checked: false, num: 13 },
            { label: "选项4", checked: false, num: 12 },
            { label: "选项5", checked: false, num: 1 },
            { label: "选项6", checked: false, num: 24 },
          ],
          selectedOption: null,
          answer: "",
          answerNum: 85, // 回答本问题总人数
          },
          {
          type: "single",
          isEdit: true,
          isMandatory: true,
          title: "问题名称2",
          options: [
            { label: "选项1", checked: false, num: 15 },
            { label: "选项2", checked: false, num: 20 },
            { label: "选项3", checked: false, num: 13 },
            { label: "选项4", checked: false, num: 12 },
            { label: "选项5", checked: false, num: 1 },
            { label: "选项6", checked: false, num: 24 },
            { label: "选项7", checked: false, num: 10 },
            { label: "选项8", checked: false, num: 10 },
          ],
          selectedOption: null,
          answer: "",
          answerNum: 105, // 回答本问题总人数
          },
        ],
        myChartStyle: { float: "left", width: "100%", height: "400px"}
      };
    },
    created() {
        this.load_qn();
        this.drawBarCharts();
        this.drawLineCharts();
        this.drawPieCharts();
        this.drawRingCharts();
    },
    mounted() {
      this.drawBarCharts();
      this.drawLineCharts();
      this.drawPieCharts();
      this.drawRingCharts();
    },
    watch: {
    questions: {
      deep: true,
      handler() {
        this.drawBarCharts();
        this.drawLineCharts();
        this.drawPieCharts();
        this.drawRingCharts();
      },
      },
    },
    methods: {
      load_qn()
        {   
            var _this = this;
            // axios({
            //     method: 'get',
            //     url: 'http://127.0.0.1:4523/m2/2618081-0-default/83421811',
            //     params: {
            //         uid: 1
            //     },
            // })
            this.$api.data.getQuestionnaire_Analyze(this.$store.state.analyzingNumID)
            .then(function (response) {
            console.log(response);
            console.log(response.data.result);
            console.log(response.data.result.questionnaire_title);
            _this.qn_title = response.data.result.questionnaire_title;
            _this.a_count = response.data.result.answersheet_count;
            _this.questions = response.data.result.q_results;
            })
            .catch(function (error) {
            console.log(error);
            });
        },
      drawBarCharts() {
      this.questions.forEach((question, index) => {
        const chartId = 'barChart-' + index;
        const chartContainer = document.getElementById(chartId);

        // 使用 ECharts 初始化图表
        const myChart = echarts.init(chartContainer);

        // 绘制柱状图
        const option = {
          // 配置项
            xAxis: {
            data: question.q_options.map(option => option.label.label)
          },
          yAxis: {},
          series: [
            {
              type: "bar", //形状为柱状图
              data: question.q_options.map(option => option.num)
            }
          ]
          };
        myChart.setOption(option);
        //随着屏幕大小调节图表
        window.addEventListener("resize", () => {
        myChart.resize();
      });
      });
    },

    drawLineCharts() {
      this.questions.forEach((question, index) => {
        const chartId = 'lineChart-' + index;
        const chartContainer = document.getElementById(chartId);

        // 使用 ECharts 初始化图表
        const myChart = echarts.init(chartContainer);

        // 绘制柱状图
        const option = {
          // 配置项
            xAxis: {
            data: question.q_options.map(option => option.label.label)
          },
          yAxis: {},
          series: [
            {
              type: "line", //形状为折线图
              data: question.q_options.map(option => option.num)
            }
          ]
          };
        myChart.setOption(option);
        //随着屏幕大小调节图表
        window.addEventListener("resize", () => {
        myChart.resize();
      });
      });
    },
      
    drawPieCharts() {
      this.questions.forEach((question, index) => {
        const chartId = 'pieChart-' + index;
        const chartContainer = document.getElementById(chartId);

        // 使用 ECharts 初始化图表
        const myChart = echarts.init(chartContainer);

        // 绘制柱状图
        const option = {
          // 配置项
          series: [
            {
              type: "pie", //形状为饼状图
              data: question.q_options.map(option => ({
                name: option.label.label,
                value: option.num
              }))
            }
          ]
          };
        myChart.setOption(option);
        //随着屏幕大小调节图表
        window.addEventListener("resize", () => {
        myChart.resize();
      });
      });
    },

    drawRingCharts() {
      this.questions.forEach((question, index) => {
        const chartId = 'ringChart-' + index;
        const chartContainer = document.getElementById(chartId);

        // 使用 ECharts 初始化图表
        const myChart = echarts.init(chartContainer);

        // 绘制柱状图
        const option = {
          // 配置项
          series: [
            {
              type: "pie", //形状为饼状图
              radius: ['50%', '70%'],
              data: question.q_options.map(option => ({
                name: option.label.label,
                value: option.num
              }))
            }
          ]
          };
        myChart.setOption(option);
        //随着屏幕大小调节图表
        window.addEventListener("resize", () => {
        myChart.resize();
      });
      });
    },

    //绘制柱形图
      change_to_bar(index) {
        this.isLine = false;
        this.isPie = false;
        this.isRing = false;
        this.isBar = true;
      },

      change_to_line(index) {
        this.isPie = false;
        this.isRing = false;
        this.isBar = false;
        this.isLine = true;
      },
    
      change_to_pie(index) {
        this.isLine = false;
        this.isPie = true;
        this.isRing = false;
        this.isBar = false;
      },

      change_to_Ring(index) {
        this.isLine = false;
        this.isPie = false;
        this.isRing = true;
        this.isBar = false;
      },

      // 选择题添加选项
      addNode(index) {
        this.questions[index].options.push({label: "选项", checked: false});
      },
      //删除样本div
      deleteNode(index, i) {
        this.questions[index].options.splice(i, 1);  //删除index为i,位置的数组元素
      },
      // 题目上移
      upNode(i) {
        if(i <= 0) return
  
            [this.questions[i-1],this.questions[i]] = [this.questions[i],this.questions[i-1]]
  
            this.$forceUpdate()
      },
      //题目下移
      downNode(i) {
        if(i >= this.questions.length - 1) return
  
        [this.questions[i+1],this.questions[i]] = [this.questions[i],this.questions[i+1]]
  
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

      // 计算比例
      calculatePercentage(num, total) {
      return ((num / total) * 100).toFixed(2) + '%';
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
  
      
      scrollToQuestion(index) {
        // 获取锚点值
        const hash = '#question-' + (index + 1);
  
        // 查找对应的问题卡片元素
        const questionCard = document.querySelector(hash);
        if (!questionCard) {
          return;
        }
  
        // 滚动到可视区域
        questionCard.scrollIntoView({ behavior: "smooth" });
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
    width: 20%;
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
  
  .echart{
    background-color: rgba(240, 240, 240, .68);
  }
  .outline-area{
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
  
  .outline-list{
    
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
  
  .outline-title{
    border-radius: 4px ;
    background-color: white;
    left: 10%;
    width: 90%;
    
  }
  
  .outline-item{
    box-shadow: none !important;
    /* border: 1px solid #dee2e6 !important; */
    border-radius: 0.25rem !important;
    margin: 0rem;
  
  
    display: block;
    padding: 0.5rem;
    text-align: left!important;
    width:90%;
    /* background-color: #9b5d5d; */
  }
  
  .tool{
    box-shadow: none !important;
    border: 1px solid #dee2e6 !important;
    border-radius: 0.25rem !important;
    margin: 0.5rem;
    width:45%;
    background-color: #ffffff;
    /* height: 10rem; */
  }
  
  .tool-body{
    padding: 0.5rem !important;
    
  }
  
  .tool-title{
    font-size: 1rem !important;
    margin-bottom: 0.5rem !important;
  }
  
  .tool-text{
    font-size: .875rem !important;
    color: #6c757d !important;
    margin-bottom: 1rem !important;
  }
  .question-card{
    position: fixed;
    top: 4rem;
    left: 25%;
    bottom: 0;
    z-index: 100;
    padding: 1rem;
    width: 54%;
    overflow-y: scroll;
  }

  .question-card::-webkit-scrollbar {
    display: none;
}

  .question-type{
    color: #8d9aa5;
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
      position:absolute;
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
    
    .el-header, .el-footer {
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
      background-color: #E9EEF3;
      color: #333;
      text-align: left;
    }
    
    body > .el-container {
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