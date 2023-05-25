<template>
    <div class="user-register-box pull-left inherited-styles-for-exported-element">
        <div class="title">
            注册信息
        </div>

        <div class="content" style="height:328px">
            <div class="items">
                <div style="float:left;"><b>用户名</b><span id="ctl00_ContentPlaceHolder1_lblLoginName"
                        style="margin-right:10px;" class="">18655369985</span></div>

                <div style="clear:both;"></div>

            </div>
            <div class="items">
                <b class="">账号ID</b><span id="ctl00_ContentPlaceHolder1_lblUserId">44253413</span>
            </div>
            <div id="ctl00_ContentPlaceHolder1_divAccount" class="items">
                <b class="">账户类型</b><span id="ctl00_ContentPlaceHolder1_lbType" class="">免费版</span>&nbsp;&nbsp;<a
                    href="https://www.wjx.cn/register/upgradevip.aspx?upgradeReason=18"
                    id="ctl00_ContentPlaceHolder1_hrefUpgrade" title="立即升级" style="margin-right:26px"
                    class="wjxui-btn wjxui-btn-orange wjxui-btn-sm fr">升级</a>
            </div>

            <div id="ctl00_ContentPlaceHolder1_divEmail" class="items">
                <b>邮件地址</b><span id="ctl00_ContentPlaceHolder1_lblEmail">未设置</span><span class="fr"><span
                        id="ctl00_ContentPlaceHolder1_lbAccountStatus">设置后可用邮件地址登录</span>&nbsp;&nbsp;<a
                        id="ctl00_ContentPlaceHolder1_lkChangEmail" title="点击更改" class="fr index_iconfont changeIcon"
                        onclick="var d=new Date();var url='/register/changeemail.aspx?t='+d.valueOf();PDF_launch(url,420,250,null,'验证邮件地址');"
                        href="javascript:void(0);"></a></span>

            </div>
            <div id="ctl00_ContentPlaceHolder1_divPhone" class="items">
                <b>手机号码</b><span id="ctl00_ContentPlaceHolder1_lblMobile" title="设置">18655369985</span><span
                    class="fr"><span id="ctl00_ContentPlaceHolder1_lblMobileStatus">已验证，<a href="javascript:void(0);"
                            onclick="unbindMobile();" class="wjx_alink">解绑</a></span>
                    &nbsp;&nbsp;<a id="ctl00_ContentPlaceHolder1_lkChangeMobile" class="fr index_iconfont changeIcon"
                        onclick="validateMobile();" href="javascript:void(0);"></a></span>
            </div>
            <div id="ctl00_ContentPlaceHolder1_divWeixin" class="items divWeixin">
                <b>微信</b><span id="ctl00_ContentPlaceHolder1_lblwx"><i class="index_iconfont"></i>未绑定</span>
                <span class="fr">
                    <a onclick="PDF_launch(&quot;/wjx/manage/guanzhu.aspx&quot;,355,415,null,&quot;绑定微信&quot;);"
                        id="ctl00_ContentPlaceHolder1_bindweixin" class="wjx_alink" href="javascript:void(0);"
                        style="margin-right:26px;">绑定微信</a>
                </span>


            </div>
            <div id="ctl00_ContentPlaceHolder1_lkPasswordBox" class="items">
                <b>密码</b><a id="ctl00_ContentPlaceHolder1_lkPassword" title="修改密码" class="wjx_alink"
                    causesvalidation="false"
                    onclick="var d=new Date();var url='/register/changepassword.aspx?t='+d.valueOf();PDF_launch(url,420,240);"
                    href="javascript:void(0);" style="display:inline-block;width:80px;">修改密码</a>
            </div>
            <div class="items" style="margin-top:10px;">



            </div>

            <div style="clear: both"></div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
body {
    background: #eee;
    /* This is just a helper in case the element has a transparent background or white colors. */
}

*,
::before {
    box-sizing: border-box;
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
    float: right;
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

a:active {
    color: #0086e6;
    outline: 0;
}

@media �screen,
screen {
    .user-register-box .fr {
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

.user-register-box {
    text-align: left;
    width: 484px;
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
    box-shadow: #e8e8e8 0 1px 4px 0, rgba(0, 0, 0, .01) 0 0 0 1px;
    font-size: 13px;
    height: 234px;
    padding: 20px 30px;
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

.content .items b,
.content .items span {
    vertical-align: middle;
}

.index_iconfont {
    font-family: index_iconfont !important;
    font-weight: 400 !important;
}

.wjxui-btn,
.wjxui-btn:hover {
    color: #fff !important;
}

.pull-left {
    float: left !important;
}

.wjx_alink {
    color: #0095ff !important;
    text-decoration: underline !important;
}</style>