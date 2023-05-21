<template>
  

  <div >
    <router-view  v-show="this.$store.state.is_creating"></router-view>
    <el-container v-show="!this.$store.state.is_creating" style="height: 745px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">

        <el-menu>
          <el-submenu index="0">
            <template slot="title"><i class="el-icon-s-data"></i>全部问卷</template>
          </el-submenu>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-plus"></i>创建问卷</template>
            <el-menu-item index="1-1" @click="pushView">从空白创建</el-menu-item>
            <el-menu-item-group title="从模板创建">
              <el-menu-item index="1-2">模板1</el-menu-item>
              <el-menu-item index="1-3">模板2</el-menu-item>
              <el-menu-item index="1-4">模板3</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-s-operation"></i>管理问卷</template>
            <el-menu-item index="2-2">俺的问卷1</el-menu-item>
            <el-menu-item index="2-3">俺的问卷2</el-menu-item>
            <el-menu-item index="2-4">俺的问卷3</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-pie-chart"></i>查看问卷</template>
            <el-menu-item index="3-2">俺的问卷1</el-menu-item>
            <el-menu-item index="3-3">俺的问卷2</el-menu-item>
            <el-menu-item index="3-4">俺的问卷3</el-menu-item>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title"><i class="el-icon-delete"></i>回收站</template>
            <el-menu-item index="4-2">俺的垃圾1</el-menu-item>
            <el-menu-item index="4-3">俺的垃圾2</el-menu-item>
            <el-menu-item index="4-4">俺的垃圾3</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-input style="width: 280px; left: 20px;" placeholder="查找问卷" suffix-icon="el-icon-search"
            v-model="TODO_input1">
          </el-input>
          <span></span>
        </el-header>

        <el-main>


          <el-row class="single_questionnaire_box">
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
              <el-button round style="background-color:rgba(227, 227, 227, 0.1);;">分析问卷</el-button>
            </div>

          </el-row>

          <el-row class="single_questionnaire_box">
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
              <el-button round style="background-color:rgba(227, 227, 227, 0.1);;">分析问卷</el-button>
            </div>

          </el-row>

          <el-row class="single_questionnaire_box">
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
              <el-button round style="background-color:rgba(227, 227, 227, 0.1);;">分析问卷</el-button>
            </div>

          </el-row>

          <el-row class="single_questionnaire_box">
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
              <el-button round style="background-color:rgba(227, 227, 227, 0.1);;">分析问卷</el-button>
            </div>

          </el-row>

        </el-main>

      </el-container>
    </el-container>
  </div>
</template>
<!-- 


  
 -->
<style scoped>
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
  left: 1%;
  width: 98%;

  height: 90px;
  border: 10px;
  padding-left: 20px;
  padding-right: 20px;
  /* padding: 0px;0 */
  margin-top: 10px;
  box-shadow: rgb(240, 240, 240) 0px 0px 4px 0px;
  border-radius: 10px;
  /* background-color: aqua; */
  /* border-bottom: 3px solid #000; */
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Microsoft YaHei", "Microsoft YaHei UI", 微软雅黑, sans-serif;
  z-index: 100;
  position: relative;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);

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

.table {}

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

<style>
.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
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
<script>

export default {
  data() {
    const item = {
      stDate: '2023-5-16',
      name: 'Loar',
      type: '考试卷',
      edDate: '2023-5-16'
    };
    return {
      tableData: Array(20).fill(item),
      userID: this.$store.state.curUserID
    }
  },
  methods: {
    pushView() {
      this.$store.state.is_creating = true,
        this.$router.push({
          name: 'questionnaire_create'
        }),

        alert(this.$store.state.is_creating)
    }
  }
};
</script>