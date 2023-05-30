<template>
  <div>
    <div v-if="!this.$store.state.isAnalyzing && !this.$store.state.is_creating">
      <aside>
        <AsideMenu @childEvent="handleChildEvent"></AsideMenu>
      </aside>
      <main>
        <el-main style="background: transparent;">
          <el-row class="single_questionnaire_box hvr-grow-shadow">
            <div class="questionnaire_title">
              <div class="pull-left">
                <div class="questionnaire_title">hihi</div>
              </div>
              <div class="pull-right">
                <div class="pull-left item-id">id:NULL</div>
                <div class="pull-left item-running">status:NULL</div>
                <div class="pull-left item-data">receive:0</div>
                <div class="pull-left item-data">2020/02/02 00:22</div>
              </div>
            </div>
            <el-divider></el-divider>
            <div class="questionnaire_body">
              <el-button round style="background-color:rgba(227, 227, 227, 0.1);;">设计问卷</el-button>
              <el-button round style="background-color:rgba(227, 227, 227, 0.1);;">发送问卷</el-button>
              <el-button @click="getManagerQuestionnaireList_Create" round
                style="background-color:rgba(227, 227, 227, 0.1);;">分析问卷</el-button>
            </div>

          </el-row>
          <el-row v-for="questionnaire in questionnaireList" :key="questionnaire.qn_id"
            class="single_questionnaire_box hvr-grow-shadow">
            <div class="questionnaire_title">
              <div class="pull-left">
                <div class="questionnaire_title">{{ questionnaire.qn_title }}</div>
              </div>
              <div class="pull-right">
                <div class="pull-left item-id">ID:{{ questionnaire.qn_id }}</div>
                <div class="pull-left item-running">Status:{{ questionnaire.qn_status }}</div>
                <div class="pull-left item-data">receive:0</div>
                <div class="pull-left item-data">创建时间:{{ questionnaire.qn_createTime }}</div>
                <div class="pull-left item-data">结束时间:{{ questionnaire.qn_endTime }}</div>
              </div>
            </div>
            <el-divider></el-divider>
            <div class="questionnaire_body">
              <el-button @click="pushCreate(questionnaire)" round style="background-color:rgba(227, 227, 227, 0.1);;">设计问卷</el-button>
              <el-button round style="background-color:rgba(227, 227, 227, 0.1);;">发送问卷</el-button>
              <el-button @click="pushAnalyze(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);">分析问卷</el-button>
              <el-button v-show="stateType==0" @click="deleteQuestionnaire(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);">删除问卷</el-button>
              <el-button v-show="stateType==0" @click="deleteQuestionnaire(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);">移除问卷</el-button>
              <el-button v-show="stateType==2" @click="deleteQuestionnaire(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);">撤销删除</el-button>
            </div>

          </el-row>
        </el-main>
      </main>
    </div>

    <div v-else>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import AsideMenu from '@/components/AsideMenu.vue'
export default {
  data() {
    const item = {
      stDate: '2023-5-16',
      name: 'Loar',
      type: '考试卷',
      edDate: '2023-5-16'
    };
    return {
      searchText: '',
      tableData: Array(20).fill(item),
      userID: this.$store.state.curUserID,
      questionnaireList: null,
      stateType: 0 //0是管理，1是填写，2是回收站
    }
  },
  watch: {
    questions: {
      deep: true,
      handler() {
      },
    },
  },
  methods: {
    pushCreate(questionnaire) {
      var data=JSON.parse(questionnaire)
      var id=data.qn_id
      this.$store.state.is_creating = true,
        this.$router.push({
          name: 'questionnaire_create',
          params:{
            "qn_id": id
          }
        }),
        alert(this.$store.state.is_creating)
    },


    pushAnalyze(questionnaire) {
      var data=JSON.parse(questionnaire)
      var id=data.qn_id
      console.log("data!!!!!!"+data)
      this.$store.state.isAnalyzing = true
      this.$store.state.analyzingNumID =id
      this.$router.push({
          name: 'Analyze',
          params:{
            "qn_id": id
          }
        })
    },

    getManagerQuestionnaireList_Create() {
      const data = {
        "uid": this.$store.state.curUserID,
        "type": "created"
      }
      console.log(this.$store.state.token_key)
      console.log(this.$store.state.curUserID)
      this.$api.userInfo.getUserInfo_GetQList(data).then((res) => {

        this.questionnaireList = res.data['qn_info']
        console.log(typeof (res.data['qn_info'][0]))
      })
      this.stateType = 0
    },
    getManagerQuestionnaireList_Delete() {
      const data = {
        "uid": this.$store.state.curUserID,
        "type": "deleted"
      }
      console.log(this.$store.state.token_key)
      console.log(this.$store.state.curUserID)
      this.$api.userInfo.getUserInfo_GetQList(data).then((res) => {
        console.log(res.data['qn_info'])
        this.questionnaireList = res.data['qn_info']
      })
      this.stateType = 2
    },
    getManagerQuestionnaireList_Filled() {
      const data = {
        "uid": this.$store.state.curUserID,
        "type": "filled"
      }
      console.log(this.$store.state.token_key)
      console.log(this.$store.state.curUserID)
      this.$api.userInfo.getUserInfo_GetQList(data).then((res) => {
        console.log("!!!!!!!!!!!!!!!")
        console.log(res.data['qn_info'] + "!!!!!!!!!!!!!!!")
        this.questionnaireList = res.data['qn_info']
      })
      this.stateType = 1
    },
    deleteQuestionnaire(questionnaire) {
      console.dir(questionnaire)
      questionnaire = JSON.parse(questionnaire)
      console.log(questionnaire.qn_id)
      var qn_id
      qn_id = questionnaire.qn_id

      if (this.stateType == 0) {
        const data = {
          "uid": this.$store.state.curUserID,
          "qn_id": qn_id,
          "status": "deleted"
        }
        console.log("deleteQuestionnaire_data:" + data)

        this.$api.questionnaire.postQuestionnaire_ChangeStatus(data).then((res) => {
          console.log(res)
        })
        this.getManagerQuestionnaireList_Create()
      } else if (this.stateType == 1) {
        this.getManagerQuestionnaireList_Filled()
      } else if (this.stateType == 2) {
        const data = {
          "uid": this.$store.state.curUserID,
          "qn_id": qn_id
        }
        this.$api.questionnaire.postQuestionnaire_Delete(data).then((res) => {
          console.log(res)
        })
        this.getManagerQuestionnaireList_Delete()
      }

    },

    handleChildEvent(key) {
      console.log('Received child event:', key)
      switch (key) {
        case 0:
          this.getManagerQuestionnaireList_Create()
          break;
        case 1:
          this.getManagerQuestionnaireList_Filled()
          break;
        case 2:
          this.getManagerQuestionnaireList_Delete()
          break;
        default:
          break;
      }
    }
  },
  mounted() {
    this.getManagerQuestionnaireList_Create();
    this.$store.state.isAnalyzing=false
    this.$store.state.is_creating=false
  },
  components: {
    AsideMenu
  }
};
</script>


<style scoped>
.wrapper {
  display: flex;
  position: relative;
}

header {
  flex: 1;
  /* background: transparent; */
  /* background-color: #4CAF50; */

  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 20px 100px;
  /* background: red; */
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 99;
  /* 设置一个背景色便于观察 */
}

aside {
  bottom: 40px;
  color: #262626;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  font-size: 12px;
  left: 5px;
  margin: 0;
  padding: 0 0px 0 0;
  position: fixed;
  text-align: left;
  top: 100px;
  width: 35%;
  z-index: 200;
  /* background-color: #fff; */
}

main {
  bottom: 40px;
  color: #262626;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  font-size: 12px;
  left: 25%;
  margin: 0;
  padding: 0 0px 0 0;
  position: fixed;
  text-align: left;
  top: 100px;
  /* position: absolute; */
  width: 70%;
  z-index: 200;
  /* background-color: #4CAF50; */
}

/* Curl Bottom Right */
.hvr-curl-bottom-right {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  position: relative;
}

.hvr-curl-bottom-right:before {
  pointer-events: none;
  position: absolute;
  content: '';
  height: 0;
  width: 0;
  bottom: 0;
  right: 0;
  background: white;
  /* IE9 */
  background: linear-gradient(315deg, white 45%, #aaa 50%, #ccc 56%, white 80%);
  box-shadow: -1px -1px 1px rgba(0, 0, 0, 0.4);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: width, height;
  transition-property: width, height;
}

.hvr-curl-bottom-right:hover:before,
.hvr-curl-bottom-right:focus:before,
.hvr-curl-bottom-right:active:before {
  width: 25px;
  height: 25px;
}

/* Grow-Shadow */
.hvr-grow-shadow {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: box-shadow, transform;
  transition-property: box-shadow, transform;
}

.hvr-grow-shadow:hover,
.hvr-grow-shadow:focus,
.hvr-grow-shadow:active {
  box-shadow: 0 10px 10px -10px rgba(0, 0, 0, 0.5);
  -webkit-transform: scale(1.03, 1.10);
  transform: scale(1.03, 1.10);
}



div {
  display: block;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-wrapper .survey-wrapper .survey-list .item-top {
  padding: 13px 24px 0;
  font-size: 16px;
  height: 22px;
  line-height: 22px;
  color: #262626;
}

.survey-items {
  background: #fff;
  border-radius: 2px;
  margin-bottom: 20px;
  box-shadow: 0 0 4px 0 #f0f0f0;
  border: 1px solid #e6e6e6;
}

.questionnaire_box {
  height: 500px;
  margin: 0;
  padding: 10;
  border: 10;

  max-height: 600px;
}

.single_questionnaire_box {
  left: 2.5%;
  width: 95%;

  height: 90px;
  border: 10px;
  padding-left: 20px;
  padding-right: 20px;
  /* padding: 0px;0 */
  margin-top: 10px;
  box-shadow: rgb(240, 240, 240) 0px 0px 4px 0px;
  border-radius: 10px;

  backdrop-filter: blur(20px);
  background: transparent;
  /* background-color: aqua; */
  /* border-bottom: 3px solid #000; */
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  z-index: 100;
  position: relative;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.3);

  font-size: 12px;
  line-height: normal;
  text-align: left;
  letter-spacing: normal;
}

.questionnaire_title {
  height: 32px;
  padding-top: 3px;
  font-size: 16px;
  line-height: 22px;
  text-align: left;
  letter-spacing: normal;
  font-family: "Helvetica Neue", Helvetica, Arial,
    "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
}

.questionnaire_body {
  padding-top: 5px;
  height: 80px;
}



.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

.pull-left {
  float: left;
  padding-left: 2px;
  padding-right: 4px;
}

.pull-right {
  float: right;
  /* float: right !important;
   */
  /* 
  line-height: 22px; */
  font-size: 16px;
  /* text-align: right;
  letter-spacing: normal; */
}

.item-id {
  text-decoration-color: black;
}

.item-data {
  text-decoration-color: black;

}

.item-running {
  text-decoration-color: #0095ff;
}
</style>


<style scoped>
.el-row {
  margin-bottom: 20px;
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>

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
  left: 25%;
  bottom: 0;
  z-index: 100;
  padding: 1rem;
  width: 54%;
  overflow-y: scroll;
}

.question-type {
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
  background-color: #E9EEF3;
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