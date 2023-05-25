<template>
  <div id="ctl00_ContentPlaceHolder1_divCorp" class="user-company-box pull-right inherited-styles-for-exported-element">
      <div class="title">
        企业信息
      </div>
      <div class="content" style="height:328px;">
        <div class="items">
          <b>公司名称</b>
          <span style="color:#262626;line-height:20px;">
            <el-link id="ctl00_ContentPlaceHolder1_lkEnterpriseName"  class="wjx_alink" @click="bindName()" v-if="isCorpBind == false">请输入</el-link>
            <el-link v-if="isCorpBind==true" target="_blank"  icon="el-icon-edit"  @click="bindName"></el-link>
            <b id="inline-text" v-if="isCorpBind==true" >{{ corperationName }}</b>
            
          </span>
        </div>
      <div class="items clearfix">
          <b class="fl" style="margin-top:4px;">企业logo</b>
          <a target="_blank" href="https://www.wjx.cn/register/upgradevip.aspx"  class="icon_vip"></a>

      </div>
      <div class="items">
        <b class="vam"><span class="vam">自定义域名</span><el-link href="https://www.wjx.cn/help/help.aspx?helpid=62&amp;h=1" target="_blank"  icon="el-icon-question"></el-link></b>
        <!-- <a id="ctl00_ContentPlaceHolder1_lkChangeDomain" class="wjx_alink" causesvalidation="false" onclick="updateVIP(1,null,56)" href="javascript:void(0);">设置域名</a> -->
        <el-link id="ctl00_ContentPlaceHolder1_lkEnterpriseName"  class="wjx_alink" @click="open()" >设置域名</el-link>
      </div>

    </div>

</div>
</template>

<script>
export default {
    data(){
        return{
            corperationName:null,
            isCorpBind: false,
        }
    },

    methods:{
        bindName() {
        this.$prompt('请输入企业名', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '你的企业名是: ' + value
          });
          this.isCorpBind = true;
          this.corperationName = value;
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });       
        });
      },
      
      open() {
        this.$alert('设置不了一点', 'Warning', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `下次再来试试吧`
            });
          }
        });
      },
      
    }
}
</script>

<style scoped>
    body {
  background: #eee;
  /* This is just a helper in case the element has a transparent background or white colors. */
}

*, ::before {
  box-sizing: border-box;
}

#inline-text {
    display: inline;
}

div {
  -webkit-tap-highlight-color: transparent;
  margin: 0;
  padding: 0;
}

.inherited-styles-for-exported-element {
  color: #262626;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  font-size: 12px;
  list-style: none;
}

a {
  background-color: transparent;
  color: #0095ff;
  text-decoration: none;
}

::-webkit-input-placeholder {
  color: #999;
}

.iconfont {
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: .2px;
  margin-right: 5px;
  text-decoration: none;
}

.icon_vip, .icon_vip:hover {
  background-image: url(https://www.wjx.cn/Images/commonImgPC/vip@2x.png);
  background-size: cover;
}

.icon_vip {
  background-color: initial;
  display: inline-block;
  height: 24px;
  margin-left: 4px;
  vertical-align: middle;
  width: 24px;
}

.fl {
  float: left;
}

.content .items b, .content .items span, .vam {
  vertical-align: middle;
}

.clearfix {
  zoom: 1;
}

.clearfix::before {
  clear: both;
  content: "";
  display: block;
  height: 0;
  visibility: hidden;
}

a:active {
  color: #0085ff;
  outline: 0;
}

.icon_vip:hover {
  background-color: #e7f5ff;
}

.user-company-box .wjx_alink {
  margin-right: 6px;
}

.title {
  color: #323232;
  font-size: 18px;
  font-weight: 700;
  line-height: 26px;
  margin-bottom: 16px;
}

.content {
  background-color: #fff;
  border-radius: 2px;
  /* box-shadow: #e8e8e8 0 1px 4px 0, rgba(0, 0, 0, .01) 0 0 0 1px; */
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  font-size: 13px;
  height: 234px;
  padding: 20px 30px;
}

.user-company-box {
  text-align: left;
  width: 40%;
  height: 100% !important;

  padding: 7px 35px 27px 20px;
margin: 59px 105px 0 -39px;
background-image: linear-gradient(to right, rgb(199, 210, 254), rgb(254, 202, 202), rgb(254, 243, 199));
}

.content .items {
  line-height: 28px;
  margin-bottom: 4px;
}

.content .items b {
  color: #8c8c8c;
  display: inline-block;
  font-size: 13px;
  font-weight: 400;
  height: 20px;
  line-height: 20px;
}

.user-company-box .items b {
  width: 90px;
}

.iconfont {
  font-family: editIcon !important;
  font-weight: 400 !important;
}

.iconfont_help {
  color: #000 !important;
}

.fs13 {
  font-size: 13px !important;
}

.pull-right {
  float: right !important;
}

.iconfont_help:hover, .wjx_alink {
  color: #0095ff !important;
}

.wjx_alink {
  text-decoration: underline !important;
}


</style>