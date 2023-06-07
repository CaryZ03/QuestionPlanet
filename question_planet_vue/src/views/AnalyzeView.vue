<template>
    <div class="row">
      
      <!-- 问题列表 -->
      <div class="question-card" id="question-list">
        <el-container class="card mb-2" style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
                    <el-main>
                        <span>问卷标题：{{ this.qn_title }}</span>
                    </el-main>
        </el-container>

        

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

            <el-table
            :data="question.q_options"
            style="width: 100%"
            show-summary
            :default-sort = "{prop: 'label.label', order: 'ascending'}"
            v-if="question.q_type === 'judge' || question.q_type === 'grade'"
            >
              <el-table-column
                prop="label "
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
            <div class="echart" :id="'barChart-' + index" :style="myChartStyle" v-if="isBar"></div>
            <div class="echart" :id="'lineChart-' + index" :style="myChartStyle" v-else-if="isLine"></div>
            <div class="echart" :id="'pieChart-' + index" :style="myChartStyle" v-else-if="isPie"></div>
            <div class="echart" :id="'ringChart-' + index" :style="myChartStyle" v-else-if="isRing"></div>
          
          </el-container>
  
          <div style="line-height: 30px;">&emsp;</div>
          
  
        </div>
      </div>
    
  
    </div>
  </template>
  
  <script>
  import * as echarts from "echarts";
  export default {
    data() {
      return {
        qn_title: "这是一个问卷名称",
        isBar: true,
        isLine: false,
        isPie: false,
        isRing: false,
        a_count: 0,
        questions: [],
        myChartStyle: { float: "left", width: "100%", height: "400px"}
      };
    },
    created() {
        this.load_qn();
    },
    mounted() {
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
        if (question.q_type === "single" || question.q_type === "multiple")
        {
          const chartId = 'barChart-' + index;
          const chartContainer = document.getElementById(chartId);

          console.log(chartContainer);
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
      }
      else if (question.q_type === "judge" || question.q_type === "grade")
        {
          const chartId = 'barChart-' + index;
          const chartContainer = document.getElementById(chartId);

          console.log(chartContainer);
          // 使用 ECharts 初始化图表
          const myChart = echarts.init(chartContainer);

          // 绘制柱状图
          const option = {
            // 配置项
              xAxis: {
              data: question.q_options.map(option => option.label)
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
      }
      });
    },

    drawLineCharts() {
      this.questions.forEach((question, index) => {
        if (question.q_type === "single" || question.q_type === "multiple")
        {
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
    }
    else if (question.q_type === "judge" || question.q_type === "grade")
        {
        const chartId = 'lineChart-' + index;
        const chartContainer = document.getElementById(chartId);

        // 使用 ECharts 初始化图表
        const myChart = echarts.init(chartContainer);

        // 绘制柱状图
        const option = {
          // 配置项
            xAxis: {
            data: question.q_options.map(option => option.label)
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
    }
      });
    },
      
    drawPieCharts() {
      this.questions.forEach((question, index) => {
        if (question.q_type === "single" || question.q_type === "multiple")
        {
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
        }
        else if (question.q_type === "judge" || question.q_type === "grade")
        {
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
                name: option.label,
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
        }
      });
    },

    drawRingCharts() {
      this.questions.forEach((question, index) => {
        if (question.q_type === "single" || question.q_type === "multiple")
        {
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
        }
        else if (question.q_type === "judge" || question.q_type === "grade")
        {
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
                name: option.label,
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
        }
      });
    },

    destroyBarCharts() {
    this.questions.forEach((question, index) => {
      if (question.q_type === "single" || question.q_type === "multiple")
      {
      const chartId = 'barChart-' + index;
      const chartContainer = document.getElementById(chartId);

      // 根据容器元素获取图表实例
      const myChart = echarts.getInstanceByDom(chartContainer);

      // 销毁图表实例
      myChart.dispose();

      // 移除 resize 事件监听器
      window.removeEventListener('resize', () => {
        myChart.resize();
      });
    }
    });
  },

    destroyLineCharts() {
    this.questions.forEach((question, index) => {
      if (question.q_type === "single" || question.q_type === "multiple")
      {
      const chartId = 'lineChart-' + index;
      const chartContainer = document.getElementById(chartId);

      // 根据容器元素获取图表实例
      const myChart = echarts.getInstanceByDom(chartContainer);

      // 销毁图表实例
      myChart.dispose();

      // 移除 resize 事件监听器
      window.removeEventListener('resize', () => {
        myChart.resize();
      });
    }
    });
  },

    destroyPieCharts() {
    this.questions.forEach((question, index) => {
      if (question.q_type === "single" || question.q_type === "multiple")
      {

      const chartId = 'pieChart-' + index;
      const chartContainer = document.getElementById(chartId);

      // 根据容器元素获取图表实例
      const myChart = echarts.getInstanceByDom(chartContainer);

      // 销毁图表实例
      myChart.dispose();

      // 移除 resize 事件监听器
      window.removeEventListener('resize', () => {
        myChart.resize();
      });
    }
    });
  },

    destroyRingCharts() {
    this.questions.forEach((question, index) => {
      if (question.q_type === "single" || question.q_type === "multiple")
      {
      const chartId = 'ringChart-' + index;
      const chartContainer = document.getElementById(chartId);

      // 根据容器元素获取图表实例
      const myChart = echarts.getInstanceByDom(chartContainer);

      // 销毁图表实例
      myChart.dispose();

      // 移除 resize 事件监听器
      window.removeEventListener('resize', () => {
        myChart.resize();
      });
    }
    });
  },


    //绘制柱形图
      change_to_bar(index) {
        this.isLine = false;
        this.isPie = false;
        this.isRing = false;
        this.isBar = true;
        setTimeout(() => {
          this.drawBarCharts();
        }, 100);
      },

      change_to_line(index) {
        this.isPie = false;
        this.isRing = false;
        this.isBar = false;
        this.isLine = true;
        setTimeout(() => {
          this.drawLineCharts();
        }, 100);
      },
    
      change_to_pie(index) {
        this.isLine = false;
        this.isPie = true;
        this.isRing = false;
        this.isBar = false;
        setTimeout(() => {
          this.drawPieCharts();
        }, 100);
      },

      change_to_ring(index) {
        this.isLine = false;
        this.isPie = false;
        this.isRing = true;
        this.isBar = false;
        setTimeout(() => {
          this.drawRingCharts();
        }, 100);
      },

      // 计算比例
      calculatePercentage(num, total) {
      return ((num / total) * 100).toFixed(2) + '%';
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