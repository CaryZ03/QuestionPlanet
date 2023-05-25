<template>
  <div class="background">
    <div class="css_pro-edited-element-0 inherited-styles-for-exported-element">
    
        <!-- 用户头像 -->
        <div class="user-info">
          <div class="avatar-wrapper">
            <img :src="avatarUrl" alt="Avatar"  style="height: auto; object-fit: contain; width: 120px;">
            <input type="file" @change="handleAvatarUpload">
          </div>
          <div class="user-data">
            <h2>{{userName}}</h2>
            <!-- <p>{{address}}</p>
            <p>{{phone}}</p> -->
             <!-- <button @click="editUserInfo">编辑</button> -->
            <el-card class="box-card">{{ sign }}</el-card> 
            <el-button type="text" icon="el-icon-edit"  @click="changeSign" class="fr"></el-button>
          </div>
        </div>
  

        <!-- 注册信息 -->
        <div class="title"> 注册信息 </div>
        <div class="content" style="height: 328px;">
    <div class="items">
      <div style="float: left;"><b>用户名</b><span id="ctl00_ContentPlaceHolder1_lblLoginName" style="margin-right: 10px;">{{userName}}</span></div>
      <div style="clear: both;"></div>
    </div>
    <div class="items">
        <b>账号ID</b><span id="ctl00_ContentPlaceHolder1_lblUserId">44253413</span>
    </div>

    <!-- <div id="ctl00_ContentPlaceHolder1_divAccount" class="items">
        <b>账户类型</b>
        <span id="ctl00_ContentPlaceHolder1_lbType">免费版</span>
        &nbsp;&nbsp;
        <a href="https://www.wjx.cn/register/upgradevip.aspx?upgradeReason=18" id="ctl00_ContentPlaceHolder1_hrefUpgrade" title="立即升级" class="wjxui-btn wjxui-btn-orange wjxui-btn-sm fr" style="margin-right: 26px;">升级</a>
    </div> -->

    <div id="ctl00_ContentPlaceHolder1_divEmail" class="items">
        <b>邮件地址</b>
        <span id="ctl00_ContentPlaceHolder1_lblEmail" v-if="addressIsBind==false">未设置</span>
        <span id="ctl00_ContentPlaceHolder1_lblEmail" v-if="addressIsBind==true">{{address}}</span>
        <span class="fr">
            <el-button type="text" @click="bindAddress" v-if="addressIsBind==false">绑定邮箱</el-button>
            <span id="ctl00_ContentPlaceHolder1_lblEmail" v-if="addressIsBind==true">已绑定,  </span><el-button type="text" @click="unbindAddress" v-if="addressIsBind==true" >解绑</el-button>
            <!-- <span id="ctl00_ContentPlaceHolder1_lbAccountStatus" @click="bindAddress">绑定邮箱</span> -->
            <!-- <a id="ctl00_ContentPlaceHolder1_lkChangEmail" title="点击更改" onclick="" class="fr index_iconfont changeIcon"></a> -->
            <el-button type="text" icon="el-icon-edit"  @click="bindAddress"></el-button>
        </span>
    </div>
    <div id="ctl00_ContentPlaceHolder1_divPhone" class="items">
        <b>手机号码</b>
        <span id="ctl00_ContentPlaceHolder1_lblMobile" title="设置" v-if="phoneIsBind==true">{{phone}}</span>
        <span id="ctl00_ContentPlaceHolder1_lblMobile" title="设置" v-if="phoneIsBind==false">未绑定</span>
        <span class="fr">
            <el-button type="text" @click="bindPhone" v-if="phoneIsBind==false">绑定手机号</el-button>
            <span id="ctl00_ContentPlaceHolder1_lblEmail" v-if="phoneIsBind==true">已绑定,  </span><el-button type="text" @click="unbindPhone" v-if="phoneIsBind==true">解绑</el-button>
            <el-button type="text" icon="el-icon-edit"  @click="bindPhone" ></el-button>
        </span>
    </div>

    <!-- <div id="ctl00_ContentPlaceHolder1_divWeixin" class="items divWeixin">
        <b>微信</b>
        <span id="ctl00_ContentPlaceHolder1_lblwx">
            <i class="index_iconfont"></i>未绑定
        </span>

        <span class="fr">
                <a onclick="" style="margin-right: 26px;"  href="javascript:void(0);" class="wjx_alink">绑定微信</a>
        </span>
    </div> -->


    <div id="ctl00_ContentPlaceHolder1_lkPasswordBox" class="items">
            <b>密码</b>
            <a id="ctl00_ContentPlaceHolder1_lkPassword" title="修改密码" causesvalidation="false" onclick="
            " href="" class="wjx_alink" style="display: inline-block; width: 80px;">
            修改密码</a>
    </div>
    <div class="items" style="margin-top: 10px;"></div>
    <div style="clear: both;"></div>
        </div>

    </div>

    <corperation></corperation>
  </div>


</template>

<script>
import { dataTool } from 'echarts';
import UserInfo from '@/components/UserInfo.vue';
export default {
    methods:{
        bindAddress() {
        this.$prompt('请输入邮箱', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
          inputErrorMessage: '邮箱格式不正确'
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '你的邮箱是: ' + value
          });
          this.addressIsBind = true;
          this.address = value;
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });       
        });
      },

      unbindAddress() {
        this.$confirm('此操作将解绑邮箱, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '解绑成功!'
          });
          this.address = null;
          this.addressIsBind = false;
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消'
          });          
        });
      },


      bindPhone() {
        this.$prompt('请输入手机号', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputPattern: /^1[3456789]\d{9}$/,
          inputErrorMessage: '手机号格式不正确'
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '你的手机号是: ' + value
          });
          this.phoneIsBind = true;
          this.phone = value;
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });       
        });
      },

      unbindPhone() {
        this.$confirm('此操作将解绑手机号, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '解绑成功!'
          });
          this.phone= null; 
          this.phoneIsBind = false;
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消'
          });          
        });
      },
    

      changeSign() {
        this.$prompt('请输入新的签名', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '签名设置成功 '
          });
          this.sign = value;
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });       
        });
      },

      handleAvatarUpload (event) {
      // 处理上传头像逻辑
    },
      editUserInfo () {
      // 进入用户信息编辑页面
    },
  


    },

    
    data(){
        return{
            address:114 ,
            addressIsBind: false,
            phoneIsBind: false,
            phone: 321321321,

            userKey:114514,
            sign: '还没有签名捏',

            userName: '张三',
            avatarUrl: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202005%2F10%2F20200510010150_2zSAt.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1687439195&t=d763d2921c0bd1ae6f6629ed0afcdd65'
        };
    },


    components:{
      corperation: UserInfo,
    }
    
}
</script>

<style scoped>
    body {
  background: #c02f2f;
  /* This is just a helper in case the element has a transparent background or white colors. */
}

/* When exporting elements with child elements that were edited, edited classes has !important on every CSS declaration.
This will be fixed on future updates (requires a lot of work due to the nature of CSS selectors complexity). Sorry for the inconvenience. You can remove it, but be careful and check if some other selector won't override it. */
*, div {
  margin: 0;
  padding: 0;
}

*, ::before {
  box-sizing: border-box;
}

div {
  -webkit-tap-highlight-color: transparent;
}

a {
  background-color: transparent;
}

::-webkit-input-placeholder {
  color: #999;
}

.index_iconfont {
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: .2px;
  font-size: 16px;
  margin-right: 5px;
  text-decoration: none;
}

.fr {
  float: right !important;
}

.wjxui-btn {
  appearance: none;
  border-radius: 2px;
  border-style: initial;
  border-width: 0;
  box-sizing: border-box;
  cursor: pointer;
  display: inline-block;
  font-weight: 400;
  outline: 0;
  text-align: center;
  text-decoration: none;
  transition: all .2s;
  vertical-align: middle;
  white-space: nowrap;
}

.wjxui-btn-orange {
  background-color: #ff8000;
}

.wjxui-btn-sm {
  font-size: 14px;
  height: 26px;
  line-height: 26px;
  padding: 0 9px;
}

.changeIcon {
  color: #8c8c8c;
  font-size: 10px;
  text-align: center;
}

.title {
  color: #eeeeee;
  font-size: 18px;
  font-weight: 700;
  line-height: 26px;
  margin-bottom: 16px;

}

.content {
  background-color: #fff;
  border-radius: 2px;
  box-shadow: #e8e8e8 0 1px 4px 0, rgba(0, 0, 0, .01) 0 0 0 1px;
  font-size: 13px;
  height: 234px;
  padding: 20px 30px;

  width: 90%;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}

a:active {
  color: #0086e6;
  outline: 0;
}

@media �screen, screen {
  .fr {
    float: none;
  }
}

.wjxui-btn:disabled {
  background-color: #d9d9d9;
  border: 1px solid #ccc;
  color: #a6a6a6;
  cursor: not-allowed;
  opacity: 1;
}

.wjxui-btn-orange:hover {
  background-color: #fca404;
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
  width: 74px;
}

.content .items b, .content .items span {
  vertical-align: middle;
}

.index_iconfont {
  font-family: index_iconfont !important;
  font-weight: 400 !important;
}

.wjx_alink {
  color: #0095ff !important;
  text-decoration: underline !important;
}

.wjxui-btn {
  color: #fff !important;
}

.css_pro-edited-element-0 {

  /* position: fixed !important;
  bottom: 79px !important;
  top: 87px !important; */

  -webkit-tap-highlight-color: transparent !important;
  color: #262626 !important;
  float: left !important;
  font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif !important;
  font-size: 12px !important;
  list-style: none !important;
  text-align: left !important;

  /* margin: 0 !important;
  padding: 0 0 0 15% !important;
  width: 80% !important; */

  width: 40%;
padding: 0 0 0 3.2%;
margin: 0 -31px 0 168px;

  /* background-color: #f7f7f7; */
  /* background-image: url("../assets/waoku.jpg" ) ; */
  background-image: linear-gradient(to right, rgb(199, 210, 254), rgb(254, 202, 202), rgb(254, 243, 199));
}

.css_pro-edited-element-0, .css_pro-edited-element-0::before {
  box-sizing: border-box !important;
}

html {
  font-size: 16px;
  /* This is IMPORTANT since some copied values use "REM" units */
}




/* new */
.user-info {
  display: flex;
  margin: 20px 20px 20px 0px;

  background-color: #fff;
  border-radius: 2px;
  box-shadow: #e8e8e8 0 1px 4px 0, rgba(0, 0, 0, .01) 0 0 0 1px;
  font-size: 13px;
  height: 30%;
  

  width: 90%;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}

.avatar-wrapper {
  width: 120px;
  height: 120px;
  overflow: hidden;
  border-radius: 50%;
  border: 1px solid #ccc;
  margin-right: 20px;
  position: relative;
}

.avatar-wrapper input[type=file] {
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.user-data button {
  padding: 6px 20px;
  background-color: #409EFF;
  color: #fff;
  border-radius: 4px;
  cursor: pointer;
}

.user-data button:hover {
  background-color: #66b1ff;
}

.user-data h2{
  color: #070606;
  display: inline-block;
  font-weight: 400;

  font-size: 26px;
/* font-weight: normal; */
list-style: none;
margin: 0;
padding: 0;
text-align: left;
line-height: 61px;
letter-spacing: 5px;
}

.user-data{
    width: 70%;
}

.box-card{
    font-size: 13px;
list-style: none;
text-align: left;
margin: 0 0 14px;
padding: 1px 20px 0px;
}

.background{
  background-color: #bf2828 !important;
  height: 100% !important;
  width: 100% !important;
}

</style>