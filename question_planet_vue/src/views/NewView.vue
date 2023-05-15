<template>
  <div class="edit-questionnaire">
    <!-- 工具栏 -->
    <div class="toolbar">
      <!-- 添加文本题按钮 -->
      <button @click="addTextQuestion">添加文本题</button>
      <!-- 添加单选题按钮 -->
      <button @click="addSingleChoiceQuestion">添加单选题</button>
      <!-- 添加多选题按钮 -->
      <button @click="addMultipleChoiceQuestion">添加多选题</button>
      <!-- 添加下拉选择题按钮 -->
      <button @click="addDropdownQuestion">添加下拉选择题</button>
      <!-- 添加文件上传题按钮 -->
      <button @click="addFileUploadQuestion">添加文件上传题</button>
      <!-- 添加日期选择题按钮 -->
      <button @click="addDateQuestion">添加日期选择题</button>
    </div>

    <!-- 问卷问题区域 -->
    <div class="question-area">
      <!-- 遍历问卷问题 -->
      <div v-for="(question, index) in questionnaire.questions" :key="index">
        <!-- 显示问题题干 -->
        <div class="question-title">{{ question.title }}</div>

        <!-- 根据问题类型显示不同的选项 -->
        <div v-if="question.type === 'text'">
          <!-- 文本题 -->
          <input type="text" />
        </div>
        <div v-else-if="question.type === 'single-choice'">
          <!-- 单选题 -->
          <div v-for="(option, optionIndex) in question.options" :key="optionIndex">
            <input type="radio" />
            <label>{{ option }}</label>
          </div>
        </div>
        <div v-else-if="question.type === 'multiple-choice'">
          <!-- 多选题 -->
          <div v-for="(option, optionIndex) in question.options" :key="optionIndex">
            <input type="checkbox" />
            <label>{{ option }}</label>
          </div>
        </div>
        <div v-else-if="question.type === 'dropdown'">
          <!-- 下拉选择题 -->
          <select>
            <option v-for="(option, optionIndex) in question.options" :key="optionIndex">{{ option }}</option>
          </select>
        </div>
        <div v-else-if="question.type === 'file-upload'">
          <!-- 文件上传题 -->
          <input type="file" />
        </div>
        <div v-else-if="question.type === 'date'">
          <!-- 日期选择题 -->
          <input type="date" />
        </div>

        <!-- 显示问题说明 -->
        <div class="question-description">{{ question.description }}</div>
      </div>
    </div>

    <!-- 问卷大纲区域 -->
    <div class="outline-area">
      <div>问卷大纲</div>
      <ul>
        <li v-for="(question, index) in questionnaire.questions" :key="index">{{ question.title }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 问卷数据
      questionnaire: {
        title: "问卷标题",
        description: "问卷描述",
        questions: [] // 问题列表
      }
    };
  },
  methods: {
    // 添加文本题
    addTextQuestion() {
      this.questionnaire.questions.push({
        title: "文本题",
        description: "请输入答案",
        type: "text",
        options: []
      });
    },

    // 添加单选题
    addSingleChoiceQuestion() {
      this.questionnaire.questions.push({
        title: "单选题",
        description: "请选择一个答案",
        type: "single-choice",
        options: ["选项1", "选项2", "选项3"]
      });
    },

    // 添加多选题
    addMultipleChoiceQuestion() {
      this.questionnaire.questions.push({
        title: "多选题",
        description: "请选择一个或多个答案",
        type: "multiple-choice",
        options: ["选项1", "选项2", "选项3"]
      });
    },

    // 添加下拉选择题
    addDropdownQuestion() {
      this.questionnaire.questions.push({
        title: "下拉选择题",
        description: "请选择一个答案",
        type: "dropdown",
        options: ["选项1", "选项2", "选项3"]
      });
    },

    // 添加文件上传题
    addFileUploadQuestion() {
      this.questionnaire.questions.push({
        title: "文件上传题",
        description: "请上传文件",
        type: "file-upload",
        options: []
      });
    },

    // 添加日期选择题
    addDateQuestion() {
      this.questionnaire.questions.push({
        title: "日期选择题",
        description: "请选择日期",
        type: "date",
        options: []
      });
    }
  }
};
</script>