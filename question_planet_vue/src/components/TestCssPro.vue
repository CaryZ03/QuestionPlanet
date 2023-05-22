<template>
  <form novalidate="true" class="css_pro-edited-element-0 inherited-styles-for-exported-element">
  <div class="SignFlow-tabs">
    <div class="SignFlow-tab SignFlow-tab--active" role="button" tabindex="0">验证码登录</div>
    <div class="SignFlow-tab" role="button" tabindex="0">密码登录</div>
  </div>
  <div class="SignFlow-account">
    <div class="SignFlow-supportedCountriesSelectContainer">
      <div class="Popover ddLajxN_Q0AuobBZjX9m"><button role="combobox" aria-expanded="false" id="Popover6-toggle" aria-haspopup="true" aria-owns="Popover6-content" type="button" class="Button InputLike EQvEDwRqICOvs_x_kUWW InputButton W2ewFU1c0bx6tahox08q Select-button HrHisPElmD_XxB9LKi6j Select-plainButton h39gnJsHf0NWeCTuygxV FEfUrdfMIKpQDJDqkjte Button--plain fEPKGkUK5jyc4fUuT0QP">中国 +86<svg width="1.2em" height="1.2em" viewBox="0 0 24 24" class="ZDI ZDI--ArrowUpDown24 Select-arrow RXYxRcvJ7zVIfNZSOcHa" fill="currentColor">
            <path fill-rule="evenodd" d="M12.53 3.47a.75.75 0 0 0-1.06 0l-5 5a.75.75 0 0 0 1.06 1.06L12 5.06l4.47 4.47a.75.75 0 1 0 1.06-1.06l-5-5Zm-5 11a.75.75 0 0 0-1.06 1.06l5 5a.75.75 0 0 0 1.06 0l5-5a.75.75 0 1 0-1.06-1.06L12 18.94l-4.47-4.47Z" clip-rule="evenodd"></path>
          </svg></button></div>
    </div><span class="SignFlow-accountSeperator">&nbsp;</span>
    <div class="SignFlowInput SignFlow-accountInputContainer"><label class="SignFlow-accountInput Input-wrapper QZcfWkCJoarhIYxlM_sG"><input name="username" type="tel" class="Input i7cW1UcwT6ThdhTakqFm username-input" placeholder="手机号" value=""></label>
      <div class="SignFlowInput-errorMask SignFlowInput-requiredErrorMask SignFlowInput-errorMask--hidden"></div>
    </div>
  </div>
  <div class="SignFlow SignFlow-smsInputContainer">
    <div class="SignFlowInput SignFlow-smsInput"><label class="Input-wrapper QZcfWkCJoarhIYxlM_sG"><input name="digits" type="number" class="Input i7cW1UcwT6ThdhTakqFm username-input" placeholder="输入 6 位短信验证码" value=""></label>
      <div class="SignFlowInput-errorMask SignFlowInput-requiredErrorMask SignFlowInput-errorMask--hidden"></div>
    </div><button type="button" class="Button CountingDownButton SignFlow-smsInputButton FEfUrdfMIKpQDJDqkjte Button--plain fEPKGkUK5jyc4fUuT0QP">获取短信验证码</button>
  </div>
  <div class="Login-options"><button type="button" class="Button Login-switchType FEfUrdfMIKpQDJDqkjte Button--plain fEPKGkUK5jyc4fUuT0QP"></button><button type="button" class="Button Login-cannotLogin FEfUrdfMIKpQDJDqkjte Button--plain fEPKGkUK5jyc4fUuT0QP">
      <div>获取语音验证码</div>
    </button></div>
  <div></div><button type="submit" class="Button SignFlow-submitButton FEfUrdfMIKpQDJDqkjte Button--primary Button--blue epMJl0lFQuYbC7jrwr_o JmYzaky7MEPMFcJDLNMG">登录/注册</button>
</form>
</template>

<script>
export default {

}
</script>

<style scoped>
body {
  background: #eee;
  /* This is just a helper in case the element has a transparent background or white colors. */
}

/* When exporting elements with child elements that were edited, edited classes has !important on every CSS declaration.
This will be fixed on future updates (requires a lot of work due to the nature of CSS selectors complexity). Sorry for the inconvenience. You can remove it, but be careful and check if some other selector won't override it. */
button {
  appearance: none;
  font-family: inherit;
  font-feature-settings: inherit;
  font-kerning: inherit;
  font-optical-sizing: inherit;
  font-variant: inherit;
  font-variation-settings: inherit;
  font-weight: inherit;
  margin: 0;
  outline: 0;
}

.FEfUrdfMIKpQDJDqkjte {
  background-image: none;
  border-radius: 3px;
  border-style: solid;
  border-width: 1px;
  color: #8590a6;
  cursor: pointer;
  display: inline-block;
  font-size: 14px;
  line-height: 32px;
  padding: 0 16px;
  text-align: center;
}

.JmYzaky7MEPMFcJDLNMG {
  border-color: #056de8;
}

.fEPKGkUK5jyc4fUuT0QP {
  background-color: transparent;
  border-radius: 0;
  border-style: none;
  height: auto;
  line-height: inherit;
  padding: 0;
}

.SignFlow {
  overflow: hidden;
}

.SignFlow-submitButton {
  height: 36px;
  margin-top: 30px;
  width: 100%;
}

.InputLike {
  background-color: #fff;
  border-radius: 3px;
  box-sizing: border-box;
  transition: background .2s, border .2s;
}

.InputButton {
  -webkit-box-align: center;
  align-items: center;
  display: flex;
}

.Popover {
  display: inline-block;
  position: relative;
}

.Select-button {
  text-align: left;
}

.Select-plainButton {
  border: 1px solid transparent;
  padding: 0;
}

.Select-arrow {
  margin-left: 8px;
}

.Input-wrapper {
  -webkit-box-align: center;
  align-items: center;
  background-color: #fff;
  box-sizing: border-box;
  display: flex;
  font-size: 14px;
  position: relative;
  transition: background .2s, border .2s;
}

.Input, .SignFlowInput {
  -webkit-box-flex: 1;
  flex: 1 1 0;
}

.Input {
  background-color: transparent;
  border-style: none;
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  overflow: hidden;
  padding: 0;
  resize: none;
}

.SignFlowInput {
  position: relative;
}

.SignFlowInput-errorMask {
  background-color: #fff;
  box-sizing: border-box;
  color: #f1403c;
  cursor: text;
  font-size: 14px;
  position: absolute;
  transition: opacity .25s;
}

.SignFlowInput-errorMask--hidden {
  height: 0;
  margin: 0;
  opacity: 0;
  padding-bottom: 0;
  padding-right: 0;
  padding-top: 0;
}

.SignFlowInput-requiredErrorMask {
  padding-left: 0;
  text-align: left;
  width: 100%;
}

.SignFlow-accountInputContainer {
  -webkit-box-flex: 1;
  flex: 1 1 0;
  overflow: hidden;
}

.SignFlow-account {
  -webkit-box-align: center;
  align-items: center;
  border-bottom: 1px solid #ebebeb;
  display: flex;
  margin-top: 24px;
}

.SignFlow-supportedCountriesSelectContainer {
  display: inline-block;
  min-width: 72px;
}

.SignFlow-accountSeperator {
  background-color: #ebebeb;
  height: 22px;
  margin: 0 12px;
  width: 1px;
}

.SignFlow-smsInputContainer {
  position: relative;
}

.SignFlow-smsInputButton {
  padding: 4px 0;
  position: absolute;
  right: 0;
  top: 24px;
  transform: translateY(-50%);
}

.Login-options {
  -webkit-box-pack: justify;
  background-color: #fff;
  display: flex;
  height: 20px;
  justify-content: space-between;
  margin-top: 12px;
}

.Login-switchType {
  color: #056de8;
}

.Login-cannotLogin {
  color: #444;
  float: right;
}

.SignFlow-tabs {
  margin-top: 16px;
  text-align: left;
}

.SignFlow-tab {
  color: #444;
  cursor: pointer;
  display: inline-block;
  font-size: 16px;
  height: 49px;
  line-height: 46px;
  margin-right: 24px;
}

.SignFlow-tab--active {
  color: #121212;
  font-synthesis-small-caps: none;
  font-synthesis-style: auto;
  font-synthesis-weight: none;
  font-weight: 600;
  position: relative;
}

.SignFlow-smsInputButton {
  color: #056de8;
}

input.Input {
  line-height: 24px;
}

.Input:not(input) {
  line-height: 24px;
}

.Input::-webkit-input-placeholder {
  color: #8590a6;
}

.Input::placeholder {
  color: #8590a6;
}

.SignFlowInput-errorMask::before {
  background-color: initial;
  background-image: linear-gradient(90deg, rgba(255, 255, 255, 0), #fff);
  content: "";
  left: -16px;
  position: absolute;
  top: 0;
}

.SignFlowInput-requiredErrorMask::before {
  height: 0;
  opacity: 0;
  overflow: hidden;
  width: 0;
}

.SignFlow-tab--active::after {
  background-color: #056de8;
  bottom: 0;
  content: "";
  display: block;
  height: 3px;
  position: absolute;
  width: 100%;
}

.FEfUrdfMIKpQDJDqkjte:focus {
  outline: 0;
  transition: box-shadow .3s, -webkit-box-shadow .3s;
}

.FEfUrdfMIKpQDJDqkjte:disabled {
  cursor: default;
  opacity: .5;
  pointer-events: none;
}

.epMJl0lFQuYbC7jrwr_o.JmYzaky7MEPMFcJDLNMG {
  background-color: #056de8;
  color: #fff;
}

.fEPKGkUK5jyc4fUuT0QP:hover {
  background-color: transparent;
}

.SignFlow .SignFlow-smsInput {
  width: auto;
}

.Input:disabled {
  color: #bfbfbf;
}

.Input:focus {
  outline: 0;
}

.SignFlowInput .Input-wrapper {
  color: #8590a6;
}

.username-input {
  color: #444;
}

.SignFlow-smsInputContainer {
  border-bottom: 1px solid #ebebeb;
  margin-top: 11px;
}

.Login-cannotLogin:hover {
  color: gray;
}

.Input-wrapper {
  border-radius: 0;
  border-style: none;
  height: 44px;
  padding: 0;
  width: 100%;
}

.SignFlowInput input.Input {
  height: 48px;
}

input:-webkit-autofill {
  box-shadow: #fff 0 0 0 30px inset;
}

.SignFlow input[type=number]::-webkit-outer-spin-button {
  appearance: none;
  margin: 0;
}

.epMJl0lFQuYbC7jrwr_o.JmYzaky7MEPMFcJDLNMG:hover {
  background-color: #0461cf;
  border-color: #0461cf;
}

.SignFlow-accountInput.Input-wrapper {
  border-style: none;
}

.SignFlowInput-requiredErrorMask {
  right: auto !important;
}

.css_pro-edited-element-0 {
  background-color: #fa8bff !important;
  background-image: linear-gradient(45deg, #fa8bff 0, #2bd2ff 52%, #2bff88 90%) !important;
  border-style: solid !important;
  border-width: 1px !important;
  box-shadow: rgba(50, 50, 93, .25) 0 50px 100px -20px, rgba(0, 0, 0, .3) 0 30px 60px -30px, rgba(10, 37, 64, .35) 0 -2px 6px 0 inset !important;
  color: #121212 !important;
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Microsoft YaHei", "Source Han Sans SC", "Noto Sans CJK SC", "WenQuanYi Micro Hei", sans-serif !important;
  line-height: 1.7 !important;
  margin-left: 16px !important;
  overflow: hidden !important;
  padding: 0 24px 30px !important;
  text-align: center !important;
  text-decoration-style: solid !important;
}

html {
  font-size: 12px;
  /* This is IMPORTANT since some copied values use "REM" units */
}
</style>