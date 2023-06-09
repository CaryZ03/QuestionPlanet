<template>
  <div id="ctl00_ContentPlaceHolder1_divCorp" class="user-company-box pull-right inherited-styles-for-exported-element">
      <div class="title ">
        企业信息
      </div>
      <div class="content hvr-grow-shadow" style="height:328px;">
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

      <img class="man" src="../assets/man - 副本.png" alt="Avatar" style="height: auto; object-fit: contain; width: 120px;">
      <!-- <img class="moon" src="../assets/planet4 - 副本.png" alt="Avatar" style="height: auto; object-fit: contain; width: 120px;"> -->
    </div>

</div>
</template>

<script>
export default {
    name:"company",
     
    data(){
        return{
      corperationName:null,
      isCorpBind: false,
      address: null,
      addressIsBind: false,
      phoneIsBind: false,
      phone: null,
    

      userKey: 114514,
      sign: '还没有签名捏',

      userName: this.$store.state.curUsername,
      userId: this.$store.state.curUserID,
      avatarUrl: 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202005%2F10%2F20200510010150_2zSAt.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1687439195&t=d763d2921c0bd1ae6f6629ed0afcdd65'
        }
    },

    methods:{

      uploadData(data) {
      console.log("data to be upload is: "+JSON.stringify(data));
      this.$api.userInfo.postUserInfo_ChangeUserInfo(JSON.stringify(data)).then((response) => {
        console.log("response data is: "+JSON.stringify(response.data))
        if (response.data.errno == 0) {
          console.log("上传用户信息成功")
        }
      }).catch(error => {
        alert("上传用户信息失败")
        console.log(error)
      })
    },



      bindName() {
        //获取数据

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
        
          const tmp = {
          "uid": this.userId,
          "username": this.userName,
          "password1": this.userKey,
          "password2": this.userKey,
          "signature": this.sign,
          "email": this.address,
          "tel": this.phone,
          "company":this.corperationName,
          }
          this.uploadData(tmp);

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

      mounted: function () {
        console.log("mounted begins");
        const tmpUser = {
          "uid": this.$store.state.curUserID
        }
        this.$api.userInfo.getUserInfo_GetUserInfo(this.$store.state.curUserID).then((response) => {
          console.log(tmpUser)
          console.log(response.data)
          if (response.data.errno == 0) {
            console.log("获取用户信息成功")
            console.log(response.data.user_info)
            const userObj = JSON.parse(response.data.user_info);

            this.userId = userObj.user_id;
            this.userName = userObj.user_name;
            this.userKey = userObj.user_password;
            this.address = userObj.user_email;
            this.phone = userObj.user_tel;
            this.sign = userObj.user_signature;
            if(this.sign == null)
              this.sign = "还没有签名捏";
            if (this.address != null)
              this.addressIsBind = true;
            if (this.phone != null)
              this.phoneIsBind = true;
          }
        }).catch(error => {
          alert("获取用户信息失败")
          console.log(error)
        })

    },

    // props:{
    //         parentdata:{
    //             type:String,
    //             default:""
    //         }
    //     }

      
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

.content .man{
   width: 300px !important;
  position: static;
  opacity: 100% !important;

}

.content .moon{
  width: 200px !important;
  position: static;
  opacity: 100% !important;
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
  color: #eeeeee;
  font-size: 18px;
  font-weight: 700;
  line-height: 26px;
  margin-bottom: 16px;

  /* margin: -47px -1px 16px -131px; */
  margin: -47px -1px 16px -15.0763%;
}

.content {
  background-color: #fff;
  border-radius: 2px;
  /* box-shadow: #e8e8e8 0 1px 4px 0, rgba(0, 0, 0, .01) 0 0 0 1px; */
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  font-size: 13px;
  height: 471px !important;
 
  padding: 20px 30px;
  /* margin: -3px 0 0 -130px; */
  margin: -3px 0 0 -15.6489%;
  opacity: 80%;
}

.user-company-box {
  text-align: left;
  width: 40%;
  height: 100% !important;

  /* padding: 7px 35px 27px 20px; */
  padding: 7px 35px 27px 55px;
  margin: 59px 105px 0 -39px;

/* background-image: linear-gradient(to right, rgb(199, 210, 254), rgb(254, 202, 202), rgb(254, 243, 199)); */
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

.hvr-grow-shadow {
  /* display: inline-block; */
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: box-shadow, transform;
  transition-property: box-shadow, transform;
}
.hvr-grow-shadow:hover, .hvr-grow-shadow:focus, .hvr-grow-shadow:active {
  box-shadow: 0 10px 10px -10px rgba(0, 0, 0, 0.5);
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}



</style>