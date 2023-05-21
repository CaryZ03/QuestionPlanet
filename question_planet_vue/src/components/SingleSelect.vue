<template>
    <div class="field ui-field-contain inherited-styles-for-exported-element" topic="1" id="div1" req="1"
        data-role="fieldcontain" type="3">
        <div class="field-label">1. 选择<span class="req">*</span></div>
        <div class="ui-controlgroup column1">
            <div class="ui-radio"><span class="jqradiowrapper"><input type="radio" value="1" id="q1_1" name="q1"
                        style="display:none;"><a class="jqradio" href="javascript:;"></a></span>
                <div class="label" for="q1_1">ppt</div>
            </div>
            <div class="ui-radio"><span class="jqradiowrapper"><input type="radio" value="2" id="q1_2" name="q1"
                        style="display:none;"><a class="jqradio" href="javascript:;"></a></span>
                <div class="label" for="q1_2">材料</div>
            </div>
        </div>
        <div class="errorMessage"></div>
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

* {
    box-sizing: border-box;
    margin: 0;
}

.inherited-styles-for-exported-element,
input {
    font-family: "PingFang SC", "helvetica neue", arial, 阿里巴巴普惠体, "思源黑体 CN", "microsoft yahei ui", "microsoft yahei", "sans-serif";
}

.inherited-styles-for-exported-element {
    color: #262626;
    font-size: 16px;
    word-break: break-word;
}

*,
::after,
a,
div {
    -webkit-tap-highlight-color: transparent;
}

a,
div {
    outline: 0;
}

input {
    appearance: none;
    outline: 0;
}

a {
    text-decoration: none;
}

*,
.ui-controlgroup {
    padding: 0;
}

.jqradio,
.ui-radio a.jqradio::after {
    background-color: #fff;
    border-radius: 50px;
}

.jqradio,
div.field {
    border-style: solid;
    border-width: 1px;
}

.jqradio {
    appearance: none;
    border-color: #a6a6a6;
    box-shadow: rgba(0, 0, 0, .08) 0 1px 0 0;
    display: inline-block;
    padding: 8px;
    position: relative;
}

.jqradiowrapper {
    display: block;
    float: left;
}

.errorMessage {
    background-color: #ffecec;
    color: #262626;
    display: none;
    font-size: 14px;
    line-height: 20px;
    margin-top: 10px;
    padding: 8px 4px 8px 36px;
    position: relative;
    transition: all .5s;
}

.ui-controlgroup {
    border-style: initial;
    border-width: 0;
    margin: 0;
}

div.field {
    border-color: transparent;
    clear: both;
    padding: 20px 19px;
}

span.req {
    color: #ff4040 !important;
    left: -12px;
    margin: 2px 0 0 2px;
    position: absolute;
    top: 0;
}

div.field-label {
    color: #262626;
    display: block;
    overflow-wrap: break-word;
    position: relative;
}

.errorMessage::before {
    background-color: initial;
    background-image: url(https://www.wjx.cn/images/comImg/erroricon.png);
    background-size: cover;
    content: "";
    height: 20px;
    left: 8px;
    position: absolute;
    top: 8px;
    width: 20px;
}

div.field {
    margin: 0 0 10px;
}

div.field-label {
    -webkit-font-smoothing: antialiased;
    font-size: 17px !important;
    font-weight: 500;
    line-height: 26px;
    padding: 0 0 10px !important;
}

.ui-controlgroup .ui-radio {
    background-color: #fff;
    border-style: initial;
    border-width: 0;
    flex: 0 0 auto;
    min-height: 38px;
    position: relative;
}

.ui-radio:hover {
    background-color: #f9f9f9;
}

.ui-radio a.jqradio::after {
    content: " ";
    font-size: 32px;
    height: 8px;
    left: 4px;
    opacity: 1;
    position: absolute;
    top: 4px;
    transform: scale(1.2);
    transition: all .3s cubic-bezier(.78, .14, .15, .86);
    width: 8px;
}

.ui-controlgroup .ui-radio .label {
    color: #595959;
    cursor: pointer;
    display: block;
    font-size: 16px;
    line-height: 22px;
    margin-left: 36px;
    min-height: 36px;
    padding: 8px 10px 8px 0;
    text-align: left;
}

.jqradiowrapper {
    margin: 9px 4px 0 12px !important;
}</style>