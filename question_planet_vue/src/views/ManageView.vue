<template>
  <div>
    <div v-if="!this.$store.state.isAnalyzing && !this.$store.state.is_creating">
      <aside>
        <AsideMenu @childEvent="handleChildEvent"></AsideMenu>
      </aside>
      <main>



        <el-main style="background: transparent;">



          <div class="q_nav">
            <button class="btnSort" @click="sortByCreateIDMax" style="float: right;">最大ID</button>
            <button class="btnSort" @click="sortByCreateIDMin" style="float: right;">最小ID</button>

            <div class="search-box" style="background: transparent;">
              <a class="search-btn" @click="filteredItems" style="background: transparent;">
                <i class="el-icon-search" aria-hidden="true"></i>
              </a>
              <input v-model="searchKeyword" class="search-txt" placeholder="搜索" />
              <!-- <div class="search-line"></div> -->
            </div>
          </div>






          <el-row v-for="questionnaire in questionnaireList" :key="questionnaire.qn_id"
            class="single_questionnaire_box hvr-grow-shadow">
            <div class="questionnaire_title">
              <div class="pull-left">
                <div class="questionnaire_title">{{ JSON.parse(questionnaire).qn_title }}</div>
              </div>
              <div class="pull-right">
                <div class="pull-left item-id">ID:{{ JSON.parse(questionnaire).qn_id }}</div>
                <div class="pull-left item-running">Status:{{ JSON.parse(questionnaire).qn_status }}</div>
                <div class="pull-left item-data">receive:0</div>
                <div class="pull-left item-data">创建时间:{{ JSON.parse(questionnaire).qn_createTime }}</div>
                <div class="pull-left item-data">结束时间:{{ JSON.parse(questionnaire).qn_endTime }}</div>
              </div>
            </div>
            <el-divider></el-divider>
            <div class="questionnaire_body">
              <el-button v-show="stateType == 0" @click="pushCreate(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);;">设计问卷</el-button>
              <el-button v-show="stateType == 0" @click="generateQuestionnaireLink(JSON.parse(questionnaire).qn_id)"
                class="copyLink" round style="background-color:rgba(227, 227, 227, 0.1);;">发送问卷</el-button>
              <el-button v-show="stateType == 0" @click="pushAnalyze(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);">分析问卷</el-button>
              <el-button v-show="stateType == 0" @click="deleteQuestionnaire(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);">删除问卷</el-button>
              <el-button v-show="stateType == 2" @click="deleteQuestionnaire(questionnaire)" round
                style="background-color:rgba(227, 227, 227, 0.1);">移除问卷</el-button>
              <el-button v-show="stateType == 2" @click="deDeleteQuestionnaire(questionnaire)" round
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
import Clipboard from 'clipboard';
import AsideMenu from '@/components/AsideMenu.vue'
export default {
  data() {
    const item = {
      stDate: '2023-5-16',
      name: 'Loar',
      type: '考试卷',
      edDate: '2023-5-16',
      
    };
    return {
      searchText: '',
      tableData: Array(20).fill(item),
      userID: this.$store.state.curUserID,
      questionnaireList: null,
      stateType: 0 ,//0是管理，1是填写，2是回收站
      searchKeyword: '' // 搜索关键字
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
      var data = JSON.parse(questionnaire)
      var id = data.qn_id
      this.$store.state.is_creating = true,
        this.$router.push({
          name: 'questionnaire_create',
          params: {
            "qn_id": id
          }
        }),
        alert(this.$store.state.is_creating)
    },
    // 生成问卷链接
    generateQuestionnaireLink(qn_id) {
      var text = `http://localhost:8080/answer/${qn_id}`

      alert(text)
      const clipboard = new Clipboard('.copyLink', {
        text: () => text
      });
      clipboard.on('success', () => {
        alert('文本已复制到剪贴板！');
        clipboard.destroy();
      });
      clipboard.on('error', () => {
        alert('Failed to copy text');
        clipboard.destroy();
      });
    },


    pushAnalyze(questionnaire) {
      var data = JSON.parse(questionnaire)
      var id = data.qn_id
      console.log("data!!!!!!" + data)
      this.$store.state.isAnalyzing = true
      this.$store.state.analyzingNumID = id
      this.$router.push({
        name: 'Analyze',
        params: {
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
        console.log(typeof (res.data['qn_info']))
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
    deDeleteQuestionnaire(questionnaire) {
      console.dir(questionnaire)
      questionnaire = JSON.parse(questionnaire)
      console.log(questionnaire.qn_id)
      var qn_id
      qn_id = questionnaire.qn_id
      const data = {
        "uid": this.$store.state.curUserID,
        "qn_id": qn_id,
        "status": "unpublished"
      }
      console.log("deleteQuestionnaire_data:" + data)

      this.$api.questionnaire.postQuestionnaire_ChangeStatus(data).then((res) => {
        console.log(res)
      })
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
    },
    // 按发布时间排序


    // 按ID排序
    sortByCreateIDMax() {
      console.log(this.questionnaireList)
      this.questionnaireList = this.questionnaireList.sort((a, b) => JSON.parse(b).qn_id - JSON.parse(a).qn_id);
      console.log(this.questionnaireList)
      return this.questionnaireList
    },

    sortByCreateIDMin() {
      console.log(this.questionnaireList)
      this.questionnaireList = this.questionnaireList.sort((b, a) => JSON.parse(b).qn_id - JSON.parse(a).qn_id);
      console.log(this.questionnaireList)
      return this.questionnaireList
    },
    // 创建时间排序
    sortByCreateTimeMAX() {
      console.log(this.questionnaireList)
      this.questionnaireList = this.questionnaireList.sort((a, b) => new Date(JSON.parse(b).qn_createTime) - new Date(JSON.parse(a).qn_createTime));
      console.log(this.questionnaireList)
      return this.questionnaireList
    },
    sortByCreateTimeMIN() {
      console.log(this.questionnaireList)
      this.questionnaireList = this.questionnaireList.sort((b, a) => new Date(JSON.parse(b).qn_createTime) - new Date(JSON.parse(a).qn_createTime));
      console.log(this.questionnaireList)
      return this.questionnaireList
    },
    // 按endTime排序


    // 按问卷回收量排序
    sortByQuestionnaireCount() {
      return this.questionnaireList.sort((a, b) => JSON.parse(a).questionnaireCount - JSON.parse(b).questionnaireCount);
    },

    // 根据当前排序方式显示数据列表
    sortedItems() {
      // TODO: 根据当前的排序方式返回排序后的数据
      return this.items;
    },
    filteredItems() {
      const keyword = this.searchKeyword.trim(); // 获取搜索关键字

      console.log(keyword)
      if (!keyword) {
        return this.questionnaireList; // 如果搜索关键字为空，则返回所有数据
      } else {
        return this.questionnaireList.filter(item => item.qn_id.indexOf(keyword)); // 过滤符合搜索条件的数据
      }
    }
  },
  mounted() {
    this.getManagerQuestionnaireList_Create();
    this.$store.state.isAnalyzing = false
    this.$store.state.is_creating = false
  },
  computed: {

  },
  components: {
    AsideMenu
  }
};
</script>
<!-- 下拉栏 -->
<style scoped>
.btnSort {
  width: 130px;
  height: 50px;
  background: transparent;
  border: 2px solid #fff;
  outline: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1.1em;
  color: #fff;
  font-weight: 500;
  margin-left: 40px;
  transition: .3s;
}


.q_nav {
  position: relative;
  height: 8vh;
  width: 100%;

  /* background: transparent; */
}

.btnSort:hover {
  background: #fff;
  color: #162938;
}

.search-line {
  position: absolute;
  left: 62px;
  bottom: 0px;
  width: 0px;
  height: 2px;
  background-color: rgb(251, 121, 0);
  transition: 0.3s;
}

.search-box {
  -webkit-tap-highlight-color: transparent;
  background: 0 0;
  background-color: linear-gradient(90deg, #5A85DC 0, rgba(108, 149, 218, .42) 50%, #3472DE 100%);
  background-image: linear-gradient(90deg, #5A85DC 0, rgba(108, 149, 218, .42) 50%, #3472DE 100%);
  background-position: 0 0;
  border: 3px none #F30000;
  border-radius: 40px;
  bottom: 30px;
  box-shadow: rgba(0, 0, 0, 0.1) 0 2px 25px 0;
  box-sizing: border-box;
  color: #333333;
  display: flex;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  font-size: 12px;
  height: 40px;
  left: 30px;
  margin: 0 0 -15px;
  padding: 0 10px 10px;
  position: absolute;
  text-align: left;
}

.search-txt {
  -webkit-tap-highlight-color: transparent;
  border-style: none;
  box-sizing: border-box;
  background: transparent;
  font-family: Helvetica;
  font-size: 16px;
  font-weight: inherit;
  line-height: 40px;
  margin: 0 0 -15px;
  outline: none;
  padding: 0 12px;
  text-align: left;
  transition: all .4s;
  width: 200px;
}

.search-btn {
  color: #888888;
  background: transparent;
  font-size: 24px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: 0.4s;
}

.search-box:hover .search-txt {
  width: 200px;
  padding: 0 12px;
}

.search-box:hover .search-btn {
  background-color: #fff;
  animation: rotate 0.4s linear;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
<style scoped>
.btnSort {
  width: 60px;
  height: 30px;
  background: transparent;
  border: 2px solid #fff;
  outline: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1.1em;
  color: #fff;
  font-weight: 500;
  margin-left: 40px;
  transition: .3s;
}

.inherited-styles-for-exported-element {
  color: #262626;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  font-size: 12px;
  text-align: left;
}

input,
li {
  margin: 0;
  padding: 0;
}

div,
h2,
input,
li,
ul {
  -webkit-tap-highlight-color: transparent;
}

ul {
  margin-bottom: 0;
  margin-left: 0;
  margin-right: 0;
}

div,
h2 {
  margin: 0;
  padding: 0;
}

.index_iconfont,
a {
  text-decoration: none;
}

li {
  list-style: none;
}

input {
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  outline: 0;
}

.index_iconfont {
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: .2px;
  font-size: 16px;
  margin-right: 5px;
}

.caret-inverted {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  height: 0;
  margin-left: 6px;
  vertical-align: middle;
  width: 0;
}

.fl {
  float: left;
}

.fr {
  float: right;
}

.vam {
  vertical-align: middle;
}

.clearfix {
  zoom: 1;
}

.surveyCont_search {
  margin-bottom: 30px;
  padding-top: 4px;
  position: relative;
  z-index: 200;
}

.status-box {
  cursor: pointer;
}

.mySurvey {
  color: #000;
  font-size: 20px;
  font-weight: 600;
  line-height: 44px;
}

.sort-status-cur,
.status-cur {
  color: #a6a6a6;
}

a:active {
  color: #0085ff;
  outline: 0;
}

body .spinner-list {
  cursor: default;
  position: relative;
}

input:-webkit-autofill {
  -webkit-text-fill-color: #666;
  box-shadow: #fff 0 0 0 1000px inset;
}

.clearfix::before {
  clear: both;
  content: "";
  display: block;
  height: 0;
  visibility: hidden;
}

input[type=text]::-ms-clear {
  display: none;
}

body .spinner-list ul {
  background-color: #fff;
  border: 1px solid #d9d9d9;
  border-radius: 3px;
  box-shadow: rgba(0, 0, 0, .1) 0 2px 10px 0;
  display: none;
  margin-top: -7px;
  padding: 6px 0;
  position: absolute;
  top: 100%;
  z-index: 3;
}

body .spinner-list ul li,
body .spinner-list ul li a {
  color: #262626;
  display: block;
  font-size: 13px;
  line-height: 33px;
  white-space: nowrap;
}

body .spinner-list ul li {
  text-align: left;
}

body .spinner-list ul li a {
  padding: 0 16px;
}

.surveyCont_search .create-search {
  position: relative;
}

.surveyCont_search .create-search input {
  background-color: #fff;
  border-radius: 999px;
  border-style: initial;
  border-width: 0;
  box-shadow: #bfbfbf 0 0 2px 0;
  color: #bfbfbf;
  font-size: 14px;
  height: 20px;
  padding: 11px 12px 11px 16px;
  width: 236px;
}

body .spinner-list ul .caret-inverted {
  color: #fff;
  left: 40px;
  line-height: 0;
  position: absolute;
  top: -5px;
}

body .spinner-list ul>:first-child+li {
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

body .spinner-list ul li:last-child {
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
}

body .spinner-list ul li a:hover {
  background-color: #f7f7f7;
}

.surveyCont_search .create-search .search-icon {
  cursor: pointer;
  font-size: 20px;
  position: absolute;
  right: 11px;
  top: 10px;
}

.surveyCont_search .create-search input:focus {
  outline: 0;
}

.surveyCont_search .create-search .search-icon:hover {
  color: #0085ff;
}

.index_iconfont {
  font-family: index_iconfont !important;
  font-weight: 400 !important;
}

.fs14 {
  font-size: 14px !important;
}

.mr0 {
  margin-right: 0 !important;
}

.status-box {
  left: -20px !important;
  width: 100px !important;
}

.caret-inverted {
  display: none !important;
}

.status-box li a {
  text-align: center !important;
}
</style>

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
  backdrop-filter: blur(20px);
  border-radius: 4px;
  border-style: initial;
  border-width: 10px;
  box-shadow: rgba(0, 0, 0, 0.3) 0 2px 12px 0;
  box-sizing: border-box;
  color: #333333;
  display: inline-block;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  font-size: 12px;
  height: 90px;
  left: 2.5%;
  letter-spacing: normal;
  line-height: normal;
  margin: 10px 0 20px;
  padding: 0 20px;
  position: relative;
  text-align: left;
  transform: perspective(1px) translateZ(0);
  transition-duration: .3s;
  transition-property: box-shadow, transform;
  vertical-align: middle;
  width: 95%;
  z-index: 100;
  background-color: #B38BFF;
  background-image: linear-gradient(45deg, #0D44E37A 0%, #2DC3EB78 52%, #2BFF882E 90.8%);
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
  overflow: auto;


}

::-webkit-scrollbar {
  width: 0;
  height: 0;
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