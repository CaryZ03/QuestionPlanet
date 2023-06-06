"use strict";(self["webpackChunkquestion_planet"]=self["webpackChunkquestion_planet"]||[]).push([[124],{9210:function(t,e,s){s.r(e),s.d(e,{default:function(){return c}});var i=function(){var t=this,e=t._self._c;return e("div",{staticClass:"row"},[e("div",{staticClass:"question-card",attrs:{id:"question-list"}},[e("el-container",{staticClass:"card mb-2",staticStyle:{"box-shadow":"0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"}},[e("el-main",[e("span",[t._v("问卷标题："+t._s(this.qn_title))])])],1),t._l(t.questions,(function(s,i){return e("div",{key:i,staticClass:"card mb-2"},[e("el-container",{staticStyle:{"box-shadow":"0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"}},[e("el-main",[e("span",[t._v("第"+t._s(i+1)+"题："+t._s(s.q_title)+"    ")]),"single"===s.q_type?e("span",{staticClass:"question-type"},[t._v("[单选题]")]):t._e(),"multiple"===s.q_type?e("span",{staticClass:"question-type"},[t._v("[多选题]")]):t._e(),"text"===s.q_type?e("span",{staticClass:"question-type"},[t._v("[填空题]")]):t._e(),"judge"===s.q_type?e("span",{staticClass:"question-type"},[t._v("[判断题]")]):t._e(),e("div",{staticStyle:{"line-height":"30px"}},[t._v(" ")]),"single"===s.q_type||"multiple"===s.q_type?e("el-table",{staticStyle:{width:"100%"},attrs:{data:s.q_options,"show-summary":"","default-sort":{prop:"label.label",order:"ascending"}}},[e("el-table-column",{attrs:{prop:"label.label",label:"选项",sortable:"",width:"500"}}),e("el-table-column",{attrs:{prop:"num",label:"小计",sortable:"",width:"140"}}),e("el-table-column",{attrs:{label:"比例",width:"100"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v(" "+t._s(t.calculatePercentage(e.row.num,t.a_count))+" ")]}}],null,!0)})],1):t._e(),"text"===s.q_type?e("div",[e("div",{staticClass:"division"},[e("span",{staticClass:"title"},[t._v("内容")])]),e("el-input",{attrs:{type:"textarea",autosize:"",placeholder:"请输入内容"},model:{value:s.a_content,callback:function(e){t.$set(s,"a_content",e)},expression:"question.a_content"}})],1):t._e()],1),e("el-footer",[e("el-button",{attrs:{type:"primary",round:""},on:{click:function(e){return t.change_to_bar(i)}}},[t._v("柱状图")]),t._v("    "),e("el-button",{attrs:{type:"primary",round:""},on:{click:function(e){return t.change_to_line(i)}}},[t._v("折线图")]),t._v("    "),e("el-button",{attrs:{type:"primary",round:""},on:{click:function(e){return t.change_to_pie(i)}}},[t._v("饼状图")]),t._v("    "),e("el-button",{attrs:{type:"primary",round:""},on:{click:function(e){return t.change_to_ring(i)}}},[t._v("圆环图")])],1),t.isBar?e("div",{staticClass:"echart",style:t.myChartStyle,attrs:{id:"barChart-"+i}}):t.isLine?e("div",{staticClass:"echart",style:t.myChartStyle,attrs:{id:"lineChart-"+i}}):t.isPie?e("div",{staticClass:"echart",style:t.myChartStyle,attrs:{id:"pieChart-"+i}}):t.isRing?e("div",{staticClass:"echart",style:t.myChartStyle,attrs:{id:"ringChart-"+i}}):t._e()],1),e("div",{staticStyle:{"line-height":"30px"}},[t._v(" ")])],1)}))],2)])},a=[],n=s(2210),r={data(){return{qn_title:"这是一个问卷名称",isBar:!0,isLine:!1,isPie:!1,isRing:!1,a_count:0,questions:[],myChartStyle:{float:"left",width:"100%",height:"400px"}}},created(){this.load_qn()},mounted(){},watch:{questions:{deep:!0,handler(){this.drawBarCharts(),this.drawLineCharts(),this.drawPieCharts(),this.drawRingCharts()}}},methods:{load_qn(){var t=this;this.$api.data.getQuestionnaire_Analyze(this.$store.state.analyzingNumID).then((function(e){console.log(e),console.log(e.data.result),console.log(e.data.result.questionnaire_title),t.qn_title=e.data.result.questionnaire_title,t.a_count=e.data.result.answersheet_count,t.questions=e.data.result.q_results})).catch((function(t){console.log(t)}))},drawBarCharts(){this.questions.forEach(((t,e)=>{const s="barChart-"+e,i=document.getElementById(s);console.log(i);const a=n.S1(i),r={xAxis:{data:t.q_options.map((t=>t.label.label))},yAxis:{},series:[{type:"bar",data:t.q_options.map((t=>t.num))}]};a.setOption(r),window.addEventListener("resize",(()=>{a.resize()}))}))},drawLineCharts(){this.questions.forEach(((t,e)=>{const s="lineChart-"+e,i=document.getElementById(s),a=n.S1(i),r={xAxis:{data:t.q_options.map((t=>t.label.label))},yAxis:{},series:[{type:"line",data:t.q_options.map((t=>t.num))}]};a.setOption(r),window.addEventListener("resize",(()=>{a.resize()}))}))},drawPieCharts(){this.questions.forEach(((t,e)=>{const s="pieChart-"+e,i=document.getElementById(s),a=n.S1(i),r={series:[{type:"pie",data:t.q_options.map((t=>({name:t.label.label,value:t.num})))}]};a.setOption(r),window.addEventListener("resize",(()=>{a.resize()}))}))},drawRingCharts(){this.questions.forEach(((t,e)=>{const s="ringChart-"+e,i=document.getElementById(s),a=n.S1(i),r={series:[{type:"pie",radius:["50%","70%"],data:t.q_options.map((t=>({name:t.label.label,value:t.num})))}]};a.setOption(r),window.addEventListener("resize",(()=>{a.resize()}))}))},destroyBarCharts(){this.questions.forEach(((t,e)=>{const s="barChart-"+e,i=document.getElementById(s),a=n.JE(i);a.dispose(),window.removeEventListener("resize",(()=>{a.resize()}))}))},destroyLineCharts(){this.questions.forEach(((t,e)=>{const s="lineChart-"+e,i=document.getElementById(s),a=n.JE(i);a.dispose(),window.removeEventListener("resize",(()=>{a.resize()}))}))},destroyPieCharts(){this.questions.forEach(((t,e)=>{const s="pieChart-"+e,i=document.getElementById(s),a=n.JE(i);a.dispose(),window.removeEventListener("resize",(()=>{a.resize()}))}))},destroyRingCharts(){this.questions.forEach(((t,e)=>{const s="ringChart-"+e,i=document.getElementById(s),a=n.JE(i);a.dispose(),window.removeEventListener("resize",(()=>{a.resize()}))}))},change_to_bar(t){this.isLine=!1,this.isPie=!1,this.isRing=!1,this.isBar=!0,setTimeout((()=>{this.drawBarCharts()}),100)},change_to_line(t){this.isPie=!1,this.isRing=!1,this.isBar=!1,this.isLine=!0,setTimeout((()=>{this.drawLineCharts()}),100)},change_to_pie(t){this.isLine=!1,this.isPie=!0,this.isRing=!1,this.isBar=!1,setTimeout((()=>{this.drawPieCharts()}),100)},change_to_ring(t){this.isLine=!1,this.isPie=!1,this.isRing=!0,this.isBar=!1,setTimeout((()=>{this.drawRingCharts()}),100)},calculatePercentage(t,e){return(t/e*100).toFixed(2)+"%"}}},o=r,l=s(1001),d=(0,l.Z)(o,i,a,!1,null,"8376aba4",null),c=d.exports}}]);
//# sourceMappingURL=124.02e30c1f.js.map