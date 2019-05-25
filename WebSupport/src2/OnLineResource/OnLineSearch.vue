<template>
  <div>
    <div style="margin-top: 15px;">
      <el-input placeholder="请输入内容" v-model="searchKey" class="input-with-select" @keyup.enter="search">
        <el-select placeholder="请选择站点" v-model="select" slot="prepend" style="width: 200px;">
          <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
        <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
      </el-input>
      <span class="goods">
        <el-badge :value="goodsSum" :max="99">
          <el-button type="text" @click="dialogFormVisible = true" size="small" >
            <i class="el-icon-goods"></i>
            我的需求单
          </el-button>
        </el-badge>
      </span>
    </div>

    <el-dialog title="我的搜索" :visible.sync="dialogFormVisible">
      <el-table :data="formItems"
                tooltip-effect="dark"
                style="width: 100%"
                :default-sort="{prop: 'author', order: 'ascending'}">
        <el-table-column type="index" label="#" width="100"></el-table-column>
        <el-table-column prop="bookname" label="书名" width="180"></el-table-column>
        <el-table-column prop="author" label="作者" width="180"></el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <el-button @click="handleDelete(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div style="margin-top: 20px">
        <el-button @click="back()">返回</el-button>
        <el-button @click="sumbitMenu()">提交</el-button>
      </div>
    </el-dialog>
    <div v-show="isloading">
      搜索中....
      <i class="el-icon-loading"></i>
    </div>
    <div v-show="isResultsShow">
      <el-divider content-position="left">搜索结果:</el-divider>
      <el-table :data="searchItems"
                tooltip-effect="dark"
                style="width: 100%"
                :default-sort="{prop: 'update_time', order: 'ascending'}">
        <el-table-column label="书名" width="200">
          <template slot-scope="scope">
            <el-link :underline="false" :href="scope.row.href" target="_blank">{{scope.row.bookname}}</el-link>
          </template>
        </el-table-column>
        <el-table-column prop="author" label="作者" width="200"></el-table-column>
        <el-table-column prop="update_time" sortable label="更新时间" width="200"></el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <el-button @click="handleAdd(scope.row)" type="text" size="small">加入</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-divider content-position="left">没有了</el-divider>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: "OnLineSearch",
    data() {
      return {
        options: [
          {
            label: "biquge5200",
            value: "选项1"
          },
          {
            label: "biquge5201",
            value: "选项2"
          },
        ],
        select: "",
        searchKey: "",
        isloading: false,
        searchItems: [],
        dialogTableVisible: false,
        dialogFormVisible: false,
        formItems: [],
        formLabelWidth: '120px'
      }
    },
    computed: {
      isResultsShow() {
        return this.searchItems.length !== 0
      },
      goodsSum() {
        return this.formItems.length
      }
    },
    methods: {
      open(msg) {
        const h = this.$createElement;
        this.$notify({
          title: '操作',
          message: h('i', {style: 'color: teal'}, msg)
        });
      },
      search() {
        if (this.searchKey) {
          const d = {
            searchKey: this.searchKey
          };
          this.isloading = true;
          axios.get("/api/spiders/biquge5200/search/", {params: d}).then(
            response => {
              const data = response.data;
              if (data.status == 200) {
                this.isloading = false;
                const jsonData = data.res;
                this.searchItems = jsonData;
              } else {
                alert("搜索失败！");
                this.isloading = false;
              }
            }).catch(
            err => {
              alert("请求出错了！")
            });
        } else {
          alert("搜索值不能为空！")
        }
      },
      handleAdd(row) {
        const index = this.formItems.indexOf(row);
        if (index >= 0) {
          this.open("已经存在，无法加入！");
          return
        }
        this.formItems.push(row);
        this.open("加入成功！");
      },
      handleDelete(row) {
        const index = this.formItems.indexOf(row);
        this.formItems.splice(index, 1);
        this.open("删除成功！");
      },
      back() {
        this.dialogFormVisible = false;
      },
      sumbitMenu() {
        var urls = [];
        if (this.formItems.length == 0) {
          alert("当前队列为空，不能提交！")
          return
        }
        for (var i = 0; i < this.formItems.length; i++) {
          urls.push(this.formItems[i].href);
        }
        const infos = {
          spider: this.select,
          urls: urls
        };
        axios.post("/api/spiders/infos/", infos).then(
          response => {
            const data = response.data;
            if (data.status == 200) {
              this.open("加入队列成功！");
            } else {
              this.open("加入队列失败！");
            }
          }).catch(
          err => {
            alert("请求出错了！")
          });
        this.dialogFormVisible = false;
        this.formItems = []
      }
    }
  }
</script>

<style scoped>

  .el-input {
    width: 80%;
    max-width: 800px;
  }

  span.goods {
    width: 10%;
    padding-left: calc(3%);
    margin-right: calc(3%);
    margin-top: 15px;
    margin-bottom: 15px;
  }

  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }

</style>
