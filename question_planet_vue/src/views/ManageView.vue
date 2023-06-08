<template>
  <div>
    <div v-if="!this.$store.state.isAnalyzing && !this.$store.state.is_creating">
      <aside>
        <AsideMenu @childEvent="handleChildEvent" @file-selected="onFileSelected"></AsideMenu>
      </aside>
      <main>
        <el-main style="background: transparent;">
          <div class="q_nav">
            <button class="btnSort" @click="sortByCreateIDMax" style="float: right;">最大ID</button>
            <button class="btnSort" @click="sortByCreateIDMin" style="float: right;">最小ID</button>
            <button class="btnSort" @click="sortByCreateTimeMAX" style="float: right;">最早发布</button>
            <button class="btnSort" @click="sortByCreateTimeMIN" style="float: right;">最晚发布</button>
            <button class="btnSort" @click="sortByQuestionnaireCountMAX" style="float: right;">最多收集</button>
            <button class="btnSort" @click="sortByQuestionnaireCountMIN" style="float: right;">最少收集</button>

            <div class="search-box" style="">
              <a class="search-btn" @click.prevent="filteredItems" style="">
                <i class="el-icon-search" aria-hidden="true"></i>
              </a>
              <input type="text" v-model="searchKeyword" style="color: aliceblue;" class="search-txt" placeholder="搜索" />
              <!-- <div class="search-line"></div> -->
            </div>
          </div>

          <TransitionGroup tag="ul" name="moveR" style="background: transparent ;margin: 0;padding: 0;border: 0;">
            <div v-for="questionnaire in questionnaireListShow" :key="questionnaire"
              class="single_questionnaire_box hvr-grow-shadow">
              <div class="questionnaire_title">
                <div class="pull-right">
                  <div class="pull-left item-id">{{ JSON.parse(questionnaire).qn_title }}</div>
                  <div class="pull-left item-id">ID:{{ JSON.parse(questionnaire).qn_id }}</div>
                  <div class="pull-left item-running" v-if="(JSON.parse(questionnaire).qn_status == 'unpublished')">状态:未发布
                  </div>
                  <div class="pull-left item-running" v-else>状态:已发布</div>
                  <div class="pull-left item-data">回收数量:{{ JSON.parse(questionnaire).qn_answersheet_count }}</div>
                  <div class="pull-left item-data">{{ JSON.parse(questionnaire).qn_create_time.substring(0, 19) }}
                  </div>
                  <!-- <div class="pull-left item-data">结束时间:{{ JSON.parse(questionnaire).qn_end_time.substring(0, 19) }}
                  </div> -->
                </div>
              </div>
              <el-divider></el-divider>
              <div class="questionnaire_body">
                <el-button v-show="stateType == 0" @click="pushCreate(questionnaire)" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">设计问卷</el-button>
                <el-button v-show="stateType == 0" @click="publicQuestionnaire(JSON.parse(questionnaire).qn_id)"
                  class="copyLink" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">发送问卷</el-button>
                <el-button v-show="stateType == 0" @click="pushAnalyze(questionnaire)" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">分析问卷</el-button>
                <el-button v-show="stateType == 0" @click="deleteQuestionnaire(questionnaire)" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">删除问卷</el-button>
                <el-button v-show="stateType == 2" @click="deleteQuestionnaire(questionnaire)" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">移除问卷</el-button>
                <el-button v-show="stateType == 2" @click="deDeleteQuestionnaire(questionnaire)" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">撤销删除</el-button>
                <el-button v-show="stateType == 0" @click="preViewQuestionnaire(questionnaire)" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">预览问卷</el-button>
                <el-button v-show="stateType == 0" @click="exportQuestionnaire(questionnaire)" round
                  style="background-color:rgba(227, 227, 227, 0.1);color:#ffffff !important;">导出问卷</el-button>
                </div>

            </div>
          </TransitionGroup>

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
// import router from '../router'
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
      questionnaireListShow: null,
      stateType: 0,//0是管理，1是填写，2是回收站
      searchKeyword: '', // 搜索关键字
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
    publicQuestionnaire(qn_id) {
      var text = `http://182.92.102.246:1145/answer/${qn_id}`

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

      const data = {
        "uid": this.$store.state.curUserID,
        "qn_id": qn_id,
        "status": "published"
      }
      console.log("publishQuestionnaire_data:" + data)

      this.$api.questionnaire.postQuestionnaire_ChangeStatus(data).then((res) => {
        console.log(res)
      })
    },
    preViewQuestionnaire(questionnaire){

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

    async getManagerQuestionnaireList_Create() {
      const data = {
        "uid": this.$store.state.curUserID,
        "type": "created"
      }
      console.log(this.$store.state.token_key)
      console.log(this.$store.state.curUserID)
      this.$api.userInfo.getUserInfo_GetQList(data).then((res) => {

        this.questionnaireList = res.data['qn_info']
        this.questionnaireListShow = res.data['qn_info']
        console.log(typeof (res.data['qn_info']))
      })
      this.stateType = 0
    },

    onFileSelected(file) {
      // 处理接收到的文件数据
      alert("getFile")
      console.log(file)

      const formData = new FormData()
      formData.append('file', file)

      this.$api.data.postQuestionnaire_Import(formData).then((res) => {
        console.log(res)
      })

    },

    importQuestionnaire() {
      // 获取文件输入框元素
      const fileInput = document.getElementById('questionnaireFile');
      // 监听文件选择事件
      fileInput.addEventListener('change', (event) => {
        // 获取选择的文件
        const file = event.target.files[0];
        // 创建FormData对象，用于传输文件
        const formData = new FormData();
        formData.append('file', file);
        // 发送POST请求
        fetch('/import-questionnaire', {
          method: 'POST',
          body: formData
        })
          .then(response => response.json())
          .then(data => {
            console.log(data); // 处理响应数据
          })
          .catch(error => {
            console.error('Error:', error);
          });
      });
    },


    async getManagerQuestionnaireList_Delete() {
      const data = {
        "uid": this.$store.state.curUserID,
        "type": "deleted"
      }
      console.log(this.$store.state.token_key)
      console.log(this.$store.state.curUserID)
      this.$api.userInfo.getUserInfo_GetQList(data).then((res) => {
        console.log(res.data['qn_info'])
        this.questionnaireList = res.data['qn_info']
        this.questionnaireListShow = res.data['qn_info']
      })
      this.stateType = 2
    },
    async getManagerQuestionnaireList_Filled() {
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
        this.questionnaireListShow = res.data['qn_info']
      })
      this.stateType = 1
    },
    copyQuestionnaire(questionnaire) {
      var qn_id = JSON.parse(questionnaire).qn_id
      this.$api.questionnaire.getQuestionnaire_copy(qn_id).then((res) => {
        console.log(res)
      })
      this.getManagerQuestionnaireList_Create()
    },
    async deleteQuestionnaire(questionnaire) {
      console.dir(questionnaire)
      questionnaire = JSON.parse(questionnaire)
      console.log(questionnaire.qn_id)
      var qn_id
      qn_id = questionnaire.qn_id

      if (this.stateType == 0) {
        //已创建文件
        await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          });

          const data = {
          "uid": this.$store.state.curUserID,
          "qn_id": qn_id,
          "status": "deleted"
        }
        console.log("deleteQuestionnaire_data:" + data)
        this.$api.questionnaire.postQuestionnaire_ChangeStatus(data).then((res)=>{
          //console.log(res.data);
          //console.log(res.data.errno);
          if(res.data.errno==0) return this.getManagerQuestionnaireList_Create()
        })

        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });

        
        
      } else if (this.stateType == 1) {
        //已填写问卷
        this.getManagerQuestionnaireList_Filled()
      } else if (this.stateType == 2) {
        //从垃圾箱里删除
        await this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {

          const data = {
          "uid": this.$store.state.curUserID,
          "qn_id": qn_id
        }
         this.$api.questionnaire.postQuestionnaire_Delete(data).then((res) => {
          console.log(res);
          if(res.data.errno == 0) this.getManagerQuestionnaireList_Delete()
        })
        this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });


        
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

    exportQuestionnaire(questionnaire) {
      var qn_id = JSON.parse(questionnaire).qn_id
      console.log("typeof" + typeof (qn_id))
      this.$api.data.getQuestionnaire_ExportFile(qn_id).then((res) => {

        console.log(res)
        const url = window.URL.createObjectURL(new Blob([res.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'questionnaire_export.csv')
        document.body.appendChild(link)
        link.click()
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
    async sortByCreateIDMax() {
      console.log(this.questionnaireListShow)
      this.questionnaireList = this.questionnaireListShow.sort((a, b) => JSON.parse(b).qn_id - JSON.parse(a).qn_id);
      console.log(this.questionnaireListShow)
      return this.questionnaireListShow
    },

    async sortByCreateIDMin() {
      console.log(this.questionnaireListShow)
      this.questionnaireList = this.questionnaireListShow.sort((b, a) => JSON.parse(b).qn_id - JSON.parse(a).qn_id);
      console.log(this.questionnaireListShow)
      return this.questionnaireListShow
    },
    // 创建时间排序
    async sortByCreateTimeMIN() {
      console.log(JSON.parse(this.questionnaireListShow[0]).qn_create_time)
      console.log(JSON.parse(this.questionnaireListShow[0]).qn_create_time.substring(0, 19))

      this.questionnaireList = this.questionnaireListShow.sort((a, b) =>
        new Date(JSON.parse(b).qn_create_time.substring()) - new Date(JSON.parse(a).qn_create_time.substring()));
      return this.questionnaireListShow
    },
    async sortByCreateTimeMAX() {
      console.log(JSON.parse(this.questionnaireListShow[0]).qn_create_time)
      console.log(JSON.parse(this.questionnaireListShow[0]).qn_create_time.substring(0, 19))

      this.questionnaireListShow = this.questionnaireListShow.sort((b, a) =>
        new Date(JSON.parse(b).qn_create_time.substring()) - new Date(JSON.parse(a).qn_create_time.substring()));
      return this.questionnaireListShow
    },
    // 按endTime排序


    // 按问卷回收量排序
    async sortByQuestionnaireCountMIN() {
      return this.questionnaireListShow.sort((a, b) => JSON.parse(a).qn_answersheet_count - JSON.parse(b).qn_answersheet_count);
    },
    async sortByQuestionnaireCountMAX() {
      return this.questionnaireListShow.sort((b, a) => JSON.parse(a).qn_answersheet_count - JSON.parse(b).qn_answersheet_count);
    },

    // 根据当前排序方式显示数据列表

    filteredItems() {
      this.$set(this.$data, 'questionnaireListShow', this.questionnaireList);

      const keyword = this.searchKeyword.trim(); // 获取搜索关键字

      console.log("KeyWord!!!!!!!!:" + keyword)
      if (!keyword) {
        console.log(this.questionnaireListShow)
        return this.questionnaireListShow; // 如果搜索关键字为空，则返回所有数据

      } else {
        console.log("filter!" + this.questionnaireListShow)
        var tmp = this.questionnaireList.filter(item => {
          const parsedItem = JSON.parse(item)
          console.log("parsedItem" + item)
          return parsedItem.qn_title && parsedItem.qn_title.includes(keyword)
        });
        console.log(tmp)
        this.questionnaireListShow = tmp

        console.log("this.questionnaireListShow:" + this.questionnaireListShow)
        return tmp;
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
.fade-move,
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scaleY(0.01) translate(30px, 0);
}

.fade-leave-active {
  position: absolute;
}


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
  margin-left: 10px;
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
  bottom: 10px;
  width: 0px;
  height: 2px;
  background-color: rgb(251, 121, 0);
  transition: 0.3s;
}

.search-box {
  -webkit-tap-highlight-color: transparent;
  border-radius: 40px;
  bottom: 30px;
  box-shadow: rgba(0, 0, 0, 0.1) 0 2px 25px 0;
  box-sizing: border-box;
  color: #333333;
  display: flex;
  font-family: Poppins, sans-serif;
  font-size: 12px;
  height: 40px;
  left: 30px;
  margin: -138px 0 -22px;
  padding: 0 10px;
  position: absolute;
  text-align: left;
  background-color: #170813;
  background-image: radial-gradient(269% 155% at 50% 50%, #5A284B 0.4%, #552654C9 21.4%, #59274CAD 46.9%, #4D1730BA 100%);
}

.search-txt {
  border: none;
  background: none;
  outline: none;
  padding: 0;
  color: #fff;
  font-size: 16px;
  line-height: 40px;
  width: 0;
  transition: 0.4s;
}

.search-btn {
  color: #888888;
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
  /* background-color: #fff;
   */
  background: transparent;
  animation: rotate 0.4s linear;
}

.search-txt:focus {
  width: 200px;
  padding: 0 12px;
}

.search-txt:focus+.search-line {
  width: 200px;
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
  -webkit-tap-highlight-color: transparent;
  backdrop-filter: blur(20px);
  border-radius: 4px;
  border-style: initial;
  border-width: 10px;
  box-shadow: none;
  box-sizing: border-box;
  color: #FFFFFF;
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
  background-image: url("data:image/png;base64,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"), conic-gradient(from 90deg at 6% 277%, #B03B51 0%, transparent 100%), conic-gradient(from 90deg at 5% 270%, #AF3549 0%, rgba(0, 0, 0, 0) 100%);
  background-size: 80px 80px, auto, auto;
}



/* 确保将离开的元素从布局流中删除
  以便能够正确地计算移动的动画。 */
.moveR-leave-active {
  position: absolute;
  transition: all 0.3s ease;
  transform: translateX(100%);
}

.moveR-enter-active {
  transition: all 0.3s ease;
  transform: translateX(0);
}

.moveR-enter {
  transform: translateX(100%);
}

.moveR-enter-from {
  transform: translateX(100%);
}

.moveR-leave {
  transform: translateX(0);
}

.moveR-leave-to {
  transform: translateX(100%);
}




.questionnaire_title {
  margin: 0;
  padding: 0;
  height: 42px;
  padding-top: 10px;
  font-size: 16px;
  line-height: 22px;
  text-align: left;
  letter-spacing: normal;
  font-family: "Helvetica Neue", Helvetica, Arial,
    "PingFang SC", "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  background-image: url(../assets/SinglePlanet.png);
  background-size: 9%;
  background-repeat: no-repeat;
  background-position: 0%, 100%;
  background-clip: border-box;
  overflow: visible;
}

.questionnaire_body {
  padding-top: 5px;
  height: 80px;

}

.questionnaire_body el-button {
  color: #FFFFFF !important;
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
  ;
  /* float: right !important;
   */
  /* 
  line-height: 22px; */
  font-size: 12px;
  padding-right: 12px;
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
  text-decoration-color: rgb(255, 255, 255);
}

.item-data {
  text-decoration-color: rgb(255, 255, 255);

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