<template>
  <div class="row">
    <!-- 工具栏 -->
    <div class="col-md-3 d-none d-lg-block bg-light sidebar">
      
        
        <!-- 单选题工具 -->
        <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">单选题</h5>
            <i class="el-icon-circle-check"></i>
            <br>
            <p class="tool-text">问卷中用户只能选中一个选项作为答案。</p>
            <el-tooltip class="item" effect="dark" content="问卷中用户只能选中一个选项作为答案。" placement="bottom">
              <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus"
                              @click="addQuestion('single')" round>添加单选题</el-button>
            </el-tooltip>
          </div>
        </div>

        <!-- 多选题工具 -->
        <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">多选题</h5>
            <i class="el-icon-circle-check"></i><i class="el-icon-circle-check"></i>
            <br>
            <p class="tool-text">问卷中用户可以选中多个选项作为答案。</p>
            <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" @click="addQuestion('multiple')" round>添加多选题</el-button>
    
          </div>
        </div>

        <!-- 填空题工具 -->
        <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">填空题</h5>
            <i class="el-icon-edit-outline"></i>
            <br>
            <p class="tool-text">问卷中用户需要输入文本信息作为答案。</p>
            <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" @click="addQuestion('text')" round>添加填空题</el-button>
          </div>
        </div>

        <!-- 评分题工具 -->
        <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">评分题</h5>
            <i class="el-icon-star-off"></i>
            <br>
            <p class="tool-text">问卷中用户需要对某个问题进行打分。</p>
            <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" @click="addQuestion('rating')" round>添加评分题</el-button>
          </div>
        </div>

        <!-- 排序题工具 -->
        <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">排序题</h5>
            <i class="el-icon-s-data"></i>
            <br>
            <p class="tool-text">问卷中用户需要将一组选项按照自己的喜好进行排序。</p>
            <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" @click="addQuestion('sorting')" round>添加排序题</el-button>
          </div>
        </div>

        <!-- 图片选择题工具 -->
        <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">图片选择题</h5>
            <i class="el-icon-picture-outline"></i>
            <br>
            <p class="tool-text">问卷中用户需要从多个图片选项中选择一个。</p>
            <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" @click="addQuestion('image')" round>添加图片选择题</el-button>
          </div>
        </div>

        <!-- 分页器工具 -->
        <!-- <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">分页器</h5>
            <p class="tool-text">将问卷分成多个页面，每个页面包含若干个问题。</p>
            <el-button type="primary" class="btn btn-primary btn-sm" round>添加分页器</el-button>
          </div>
        </div> -->

        <!-- 进度条工具 -->
        <div class="tool mb-2">
          <div class="tool-body">
            <h5 class="tool-title">进度条</h5>
            <i class="el-icon-s-data"></i>
            <br>
            <p class="tool-text">显示当前用户填写问卷的进度。</p>
            <el-button type="primary" class="btn btn-primary btn-sm" icon="el-icon-circle-plus" round>添加进度条</el-button>
          </div>
        </div>
  
    </div>

    <!-- 问题列表 -->
    <div class="question-card" id="question-list">
      <div v-for="(question, index) in questions" :key="index" class="card mb-2" v-bind:id="question.id">
        <el-container style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
        <el-main v-if="question.isEdit">
          <span class="red_star" v-if="question.isMandatory">*&nbsp;</span>
          <span class="red_star" v-else></span>

          <span v-if="question.type === 'single'">{{ index + 1 }}.单选题</span>
          <span v-if="question.type === 'multiple'">{{ index + 1 }}.多选题</span>
          <span v-if="question.type === 'text'">{{ index + 1 }}.填空题</span>
          <div style="line-height: 30px;">&emsp;</div>

          <div class="title">标题</div>
          <el-input placeholder="请输入标题" v-model="question.title" clearable></el-input>
          <div style="line-height: 30px;">&emsp;</div>
          
          <div v-if="question.type === 'single' || question.type === 'multiple'">
          <div class="division"><span class="title">选项</span></div>
          <div class="single_choice_ques" v-for="(item, index_item) in question.options" :key="index_item">
          <el-row>
          <el-col :span="3"><div><el-button type="danger" icon="el-icon-minus" circle size="small" v-on:click="deleteNode(index, index_item)"></el-button></div></el-col>
          <el-col :span="21"><div><el-input placeholder="请输入题目内容" v-model="item.label" clearable></el-input></div></el-col>
          </el-row>
          <el-row>
            <el-col :span="3"><div><el-button type="danger" icon="el-icon-minus" circle size="small" v-on:click="deleteNode(index, index_item)"></el-button></div></el-col>
            <el-col :span="21"><div>{{ index_item }}{{ index }}</div></el-col>
          </el-row>
          </div>

          <el-row>
          <el-col :span="3"><div><el-button type="primary" icon="el-icon-plus" circle size="small" v-on:click="addNode(index)"></el-button></div></el-col>
          <el-col :span="21"><div style="line-height: 200%; color: #0099ff;">添加选项</div></el-col>
          </el-row>
          </div>

          <div v-else-if="question.type === 'text'">
            <div class="division"><span class="title">内容</span></div>
            <el-input type="textarea" autosize placeholder="请输入内容" v-model="question.answer"></el-input>
          </div>

          <div style="line-height: 30px;">&emsp;</div>
          <div class="division"><span class="title">设置</span></div>

          <el-row>
          <el-col :span="21"><div style="line-height: 200%; color: #000;">此题目必须回答</div></el-col>
          <el-col :span="3"><el-switch v-model="question.isMandatory" active-color="#0099ff" inactive-color="#c2bdbd"></el-switch></el-col>
          </el-row>
        </el-main>

        <el-main v-else>
          <span class="red_star" v-if="question.isMandatory">*&nbsp;</span>
          <span class="red_star" v-else></span>
          <span v-if="question.type === 'single'">{{ index + 1 }}.单选题</span>
          <span v-if="question.type === 'multiple'">{{ index + 1 }}.多选题</span>
          <span v-if="question.type === 'text'">{{ index + 1 }}.填空题</span>
          <div style="line-height: 30px;">&emsp;</div>
          <div>题目：{{ question.title }}</div>

          <div style="line-height: 30px;">&emsp;</div>

          <div v-if="question.type === 'single' || question.type === 'multiple'">
          <div class="division"><span class="title">选项</span></div>
          <div v-if="question.type === 'single'">
            <el-radio-group v-model="question.selectedOption">
            <el-radio v-for="(option, index_option) in question.options" :label="index_option" :key="index_option">{{ option.label }}</el-radio>
            </el-radio-group>
          </div>
          
          <div v-if="question.type === 'multiple'">
            <div v-for="(option, index_option) in question.options" :key="index_option">
              <el-checkbox :label="index_option" v-model="option.checked">{{ option.label }}</el-checkbox>
            </div>
          </div>
          </div>

          <div v-else-if="question.type === 'text'">
            <div class="division"><span class="title">内容</span></div>
            <el-input type="textarea" autosize placeholder="请输入内容" v-model="question.answer"></el-input>
          </div>

        </el-main>
        <el-footer>
            <el-button icon="el-icon-folder-checked" circle v-on:click="change_to_save_mode(index)" v-if="question.isEdit"></el-button>
            <el-button icon="el-icon-edit" circle v-on:click="change_to_edit_mode(index)" v-else></el-button>           
            &emsp;&emsp;&emsp;&emsp;
            <el-button icon="el-icon-delete" circle v-on:click="removeQuestion(index)"></el-button>
            &emsp;&emsp;&emsp;&emsp;
            <el-button icon="el-icon-top" circle v-on:click="upNode(index)"></el-button>
            &emsp;&emsp;&emsp;&emsp;
            <el-button icon="el-icon-bottom" circle v-on:click="downNode(index)"></el-button>
        </el-footer>
        </el-container>

        <div style="line-height: 30px;">&emsp;</div>

      </div>
    </div>


    <!-- 问卷大纲区域 -->
    <div class="outline-area">
      <div class="outline-title">问卷大纲</div>
      <div class="outline-list">
        <!-- <ol>
          <li size="medium" v-for="(question, index) in questions" :key="index">{{ question.title }}</li>
        </ol> -->
        <el-link class= "outline-item"   v-for="(question, index) in questions" :key="index"  @click.prevent="scrollToQuestion(question, index)"  >{{ index + 1 }}.{{ question.title }}</el-link>
      </div>
      
    </div>
  

  </div>
</template>

<script>

// const vm = new Vue({
//   el: '#question-list',
//   data:{
//     seen:true
//   }
// }
// )

export default {
  data() {
    return {
      questions: [],
    };
  },
  methods: {
    // 添加问题
    addQuestion(type) {
      let question = {
        type: type,
        isEdit: true,
        isMandatory: true,
        title: "",
        options: [],
        selectedOption: null,
        answer: "",
        stars: [false, false, false, false, false],
        images: [
          {src: "https://via.placeholder.com/150x150?text=Image+1"},
          {src: "https://via.placeholder.com/150x150?text=Image+2"},
          {src: "https://via.placeholder.com/150x150?text=Image+3"},
          {src: "https://via.placeholder.com/150x150?text=Image+4"},
          {src: "https://via.placeholder.com/150x150?text=Image+5"},
        ],
      
      };
      if (type === "single" || type === "multiple") {
        question.options = [
          { label: "选项1", checked: false },
          { label: "选项2", checked: false },
        ];
      } else if (type === "rating") {
        question.stars = [false, false, false, false, false];
      }
      // 为题目卡片动态生成唯一 ID
      question.id = 'question-' + (this.questions.length+1 );
      this.questions.push(question);
    },

    // 选择题添加选项
    addNode(index) {
      this.questions[index].options.push({label: "选项", checked: false});
    },
    //删除样本div
    deleteNode(index, i) {
      this.questions[index].options.splice(i, 1);  //删除index为i,位置的数组元素
    },
    // 题目上移
    upNode(i) {
      if(i <= 0) return

          [this.questions[i-1],this.questions[i]] = [this.questions[i],this.questions[i-1]]

          this.$forceUpdate()
    },
    //题目下移
    downNode(i) {
      if(i >= this.questions.length - 1) return

      [this.questions[i+1],this.questions[i]] = [this.questions[i],this.questions[i+1]]

          this.$forceUpdate()
    },

    //退出编辑模式
    change_to_save_mode(index) {
      this.questions[index].isEdit = false;
    },

    //退出编辑模式
    change_to_edit_mode(index) {
      this.questions[index].isEdit = true;
    },

    // 删除问题
    removeQuestion(index) {
      this.questions.splice(index, 1);
    },

    // 评分题选择星星
    selectStar(question, starIndex) {
      for (let i = 0; i < question.stars.length; i++) {
        if (i <= starIndex) {
          question.stars.splice(i, 1, true);
        } else {
          question.stars.splice(i, 1, false);
        }
      }
    },

    // 排序题拖动事件
    dragStart(event, question, option) {
      event.preventDefault();
      event.stopPropagation();
      event.dataTransfer.setData("text/plain", "");
      event.target.parentElement.classList.add("dragging");
      this.dragOption = option;
      this.dragQuestion = question;
    },
    dragEnd(event, question, option) {
      event.preventDefault();
      event.stopPropagation();
      event.target.parentElement.classList.remove("dragging");
      let newIndex = question.options.indexOf(option);
      let oldIndex = question.options.indexOf(this.dragOption);
      if (newIndex > oldIndex) {
        question.options.splice(newIndex + 1, 0, this.dragOption);
      } else {
        question.options.splice(newIndex, 0, this.dragOption);
      }
      question.options.splice(oldIndex, 1);
      this.dragOption = null;
      this.dragQuestion = null;
    },

    // 图片选择题选择图片
    selectImage(question, index) {
      question.images.forEach((image, imageIndex) => {
        if (index === imageIndex) {
          image.selected = true;
        } else {
          image.selected = false;
        }
      });
    },



    


    scrollToQuestion(question, index) {
      
      this.$nextTick(()=>{
          
      //获取锚点值
      const hash = '.outline-item #question-' + (index+1 );


      // 查找对应的问题卡片元素
      //const questionCard = document.querySelector(hash);
      const questionCard  = document.getElementById(question.id);
      console.log(questionCard);
      // const questionCard = document.querySelector(hash);
      if (!questionCard) {
        return;
      }
      // // 滚动到可视区域
      // questionCard.scrollIntoView({ behavior: "smooth" });
        questionCard.scrollIntoView({ behavior: "smooth" });
      })
      
    }




  },


  

  
  

};
</script>

<style scoped>
/* 样式代码 */
.sidebar {
  position: fixed;
  top: 4rem;
  left: 0;
  bottom: 0;
  z-index: 100;
  padding: 1rem;
  width: 30%;
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

.outline-area{
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

.outline-list{
  
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

.outline-title{
  border-radius: 4px ;
  background-color: white;
  left: 10%;
  width: 90%;
  
}

.outline-item{
  box-shadow: none !important;
  /* border: 1px solid #dee2e6 !important; */
  border-radius: 0.25rem !important;
  margin: 0rem;


  display: block;
  padding: 0.5rem;
  text-align: left!important;
  width:90%;
  /* background-color: #9b5d5d; */
}

.tool{
  box-shadow: none !important;
  border: 1px solid #dee2e6 !important;
  border-radius: 0.25rem !important;
  margin: 0.5rem;
  width:45%;
  background-color: #ffffff;
  /* height: 10rem; */
}

.tool-body{
  padding: 0.5rem !important;
  
}

.tool-title{
  font-size: 1rem !important;
  margin-bottom: 0.5rem !important;
}

.tool-text{
  font-size: .875rem !important;
  color: #6c757d !important;
  margin-bottom: 1rem !important;
}
.question-card{
  position: fixed;
  top: 4rem;
  left: 35%;
  bottom: 0;
  z-index: 100;
  padding: 1rem;
  width: 44%;
  overflow-y: scroll;
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
    position:absolute;
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
  
  .el-header, .el-footer {
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
  }
  
  body > .el-container {
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