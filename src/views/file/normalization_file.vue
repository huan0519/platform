<template>
  <div>
    <div style="margin: 10px 0">
      <el-input style=" width: 200px" placeholder="请输入文件名" suffix-icon="el-icon-search"
                v-model="process_type"></el-input>
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
      <el-table-column prop="file_type" label="文件类型" width="150"></el-table-column>
      <el-table-column prop="upload_time" label="上传时间"></el-table-column>
      <el-table-column label="操作" width="300" align="center">
        <template slot-scope="scope">
          <el-button type="primary" @click="download_file(scope.row)">下载 <i class="el-icon-edit"></i></el-button>
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
    <el-dialog title="文件信息" :visible.sync="dialogFormVisible" width="30%">
      <el-form label-width="80px" size="small">
        <el-form-item label="文件名">
          <el-input v-model="form.filename" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="操作类型">
          <el-input disabled v-model="form.processing_type" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="数据来源">
          <el-input v-model="form.data_source" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </div>
    </el-dialog>
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
      dialogFormVisible:false,
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
    del (user) {

    },
    reset () {
      this.process_type = ''
      this.dataSource = ''
      this.load()
    },
    load () {
      axios.get('http://localhost:8000/normalized_file/paginate', {
        params: {
          processing_type: this.process_type,
          data_source: this.dataSource,
          page: this.pagenum,
          size: this.pagesize
        }
      }).then(res => {
        this.tableData = res.data.data
        this.total = res.data.total
      })
    },
    download_file(row){
      this.form = row;
      axios.get('http://localhost:8000/download/normalized_file/'+ this.form.id, {
        responseType: 'blob',
      } )
          .then(response => {
            const blob = new Blob([response.data], { type: 'text/csv;charset=utf-8' });
            const downloadUrl = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = downloadUrl;

            let filename = '归一化结果';
            link.download = filename;

            document.body.appendChild(link);
            link.click();

            URL.revokeObjectURL(downloadUrl);
            document.body.removeChild(link);
          })
          .catch(error => {
            console.error('下载失败：', error);
          });
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
