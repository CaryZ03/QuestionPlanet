<template>
  <el-container style="height: 745px; border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu :default-openeds="['1', '3']">
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-message"></i>创建问卷</template>
          <el-menu-item index="1-1">从空白创建</el-menu-item>
          <el-menu-item-group title="从模板创建">
            <el-menu-item index="1-2">模板1</el-menu-item>
            <el-menu-item index="1-3">模板2</el-menu-item>
            <el-menu-item index="1-4">模板3</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title"><i class="el-icon-message"></i>管理问卷</template>
          <el-menu-item index="2-2">俺的问卷1</el-menu-item>
          <el-menu-item index="2-3">俺的问卷2</el-menu-item>
          <el-menu-item index="2-4">俺的问卷3</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-message"></i>查看问卷</template>
          <el-menu-item index="3-2">俺的问卷1</el-menu-item>
          <el-menu-item index="3-3">俺的问卷2</el-menu-item>
          <el-menu-item index="3-4">俺的问卷3</el-menu-item>
        </el-submenu>
        <el-submenu index="4">
          <template slot="title"><i class="el-icon-message"></i>回收站</template>
          <el-menu-item index="4-2">俺的垃圾1</el-menu-item>
          <el-menu-item index="4-3">俺的垃圾2</el-menu-item>
          <el-menu-item index="4-4">俺的垃圾3</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-dropdown>
          <i class="el-icon-setting" style="margin-right: 15px"></i>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>查看</el-dropdown-item>
            <el-dropdown-item>新增</el-dropdown-item>
            <el-dropdown-item>删除</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <span></span>
      </el-header>

      <el-main class="table">
        <el-table :data="tableData">
          <el-table-column prop="stDate" label="日期" width="140">
          </el-table-column>
          <el-table-column prop="name" label="问卷名" width="120">
          </el-table-column>
          <el-table-column prop="type" label="问卷类型" width="120">
          </el-table-column>
          <el-table-column prop="edDate" label="截止日期">
          </el-table-column>
          <button>{{userID}}</button>
        </el-table>
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped>
.table {

}

.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>

<script>
export default {
  data() {
    const item = {
      stDate: '2023-5-16',
      name: 'Loar',
      type: '考试卷',
      edDate: '2023-5-16'
    };
    return {
      tableData: Array(20).fill(item),
      userID:this.$store.state.curUserID
    }
  }
};
</script>