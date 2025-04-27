<template>
  <div>
    <div style="margin: 10px 0">
      <el-input style=" width: 200px" placeholder="请输入处理类型" suffix-icon="el-icon-search"
                v-model="process_type"></el-input>
      <el-input style="width: 200px; margin-left: 5px" placeholder="请输入数据来源" suffix-icon="el-icon-message"
                v-model="dataSource"></el-input>
      <el-button style="margin-left: 5px" type="primary" @click="load">搜索</el-button>
      <el-button type="warning" @click="reset">重置</el-button>
    </div>
    <div style="margin: 10px 0">
      <el-popconfirm
          style="margin-left: 8px"
          confirm-button-text='确定'
          cancel-button-text='我再想想'
          icon="el-icon-info"
          icon-color="red"
          title="您确定删除这些数据吗？"
          @confirm="delbatch"
      >
        <el-button type="danger" slot="reference">批量删除<i style="margin-left: 3px"
                                                             class="el-icon-remove-outline"></i></el-button>
      </el-popconfirm>
    </div>
    <el-table :data="tableData" border stripe header-cell-class-name="headerbg"
              @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="id" label="ID" width="80"></el-table-column>
      <el-table-column prop="filename" label="文件名" width="200"></el-table-column>
      <el-table-column prop="processing_type" label="操作类型" width="150"></el-table-column>
      <el-table-column prop="data_source" label="数据来源"></el-table-column>
      <el-table-column label="操作" width="300" align="center">
        <template slot-scope="scope">
          <el-button type="success" @click="download_file(scope.row)">下载 <i class="el-icon-edit"></i></el-button>
          <el-button type="primary" @click="update_file(scope.row)">修改 <i class="el-icon-edit"></i></el-button>
          <el-popconfirm
              style="margin-left: 5px"
              confirm-button-text='确定'
              cancel-button-text='我再想想'
              icon="el-icon-info"
              icon-color="red"
              title="您确定删除吗？"
              @confirm="del(scope.row)"
          >
            <el-button type="danger" slot="reference">删除 <i class="el-icon-delete"></i></el-button>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
    <div style="padding: 10px 0">
      <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="pagenum"
          :page-sizes="[2, 5, 10, 20]"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :page-count="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import request from '@/utils/request'
import axios from 'axios'

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'file_sum',
  data () {
    return {
      tableData: [],
      total: 0,
      pagenum: 1,
      pagesize: 10,
      form: {},
      headerbg: 'headerbg',
      process_type: '',
      dataSource: '',
    }
  },
  created () {
    this.load()
  },
  methods: {
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    delbatch () {
      const ids = this.multipleSelection.map(v => v.id)
      request.post('/user/del/batch', ids).then(res => {
        if (res.data) {
          this.$message.success('批量删除成功')
          this.load()
        } else {
          this.$message.error('批量删除失败')
        }
      })
    },
    handleEdit (row) {
      this.form = row
      this.dialogFormVisible = true
    },
    del (user) {

    },
    reset () {
      this.process_type = ''
      this.dataSource = ''
      this.load()
    },
    load () {
      axios.get('http://localhost:8000/file_sum/paginate', {
        params: {
          process_type: this.process_type,
          dataSource: this.dataSource,
          page: this.pagenum,
          size: this.pagesize
        }
      }).then(res => {
        this.tableData = res.data.data
        this.total = res.data.total
      })
    },
    handleSizeChange (pagesize) {
      console.log(pagesize)
      this.pagesize = pagesize
      this.load()
    },
    handleCurrentChange (pagenum) {
      console.log(pagenum)
      this.pagenum = pagenum
      this.load()
    }
  }
}
</script>

<style>
</style>
