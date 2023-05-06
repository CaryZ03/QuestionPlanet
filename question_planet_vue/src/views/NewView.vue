<template>
    <div class="toolbar">
      <el-row class="toolbar-row" v-for="(row, rowIndex) in tools" :key="rowIndex">
        <el-col v-for="(tool, colIndex) in row" :key="colIndex" :span="8" class="toolbar-item">
          <el-tooltip :content="tool.name" placement="bottom">
            <el-button :icon="tool.icon"></el-button>
          </el-tooltip>
        </el-col>
      </el-row>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tools: [
          [
            { name: '搜索', icon: 'el-icon-search' },
            { name: '编辑', icon: 'el-icon-edit' },
            { name: '删除', icon: 'el-icon-delete' }
          ],
          [
            { name: '上传', icon: 'el-icon-upload' },
            { name: '下载', icon: 'el-icon-download' },
            { name: '刷新', icon: 'el-icon-refresh' }
          ]
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  .toolbar {
    display: flex;
    flex-wrap: wrap;
    margin: -10px;
  }
  
  .toolbar-row {
    width: calc(100% + 20px);
    margin: 10px;
  }
  
  .toolbar-item {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
  }
  </style>