<template>
  <el-container direction="vertical">
    <el-header style="text-align: right; font-size: 12px">
      <el-dropdown>
        <i class="el-icon-setting" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item></el-dropdown-item>
          <el-dropdown-item>Add</el-dropdown-item>
          <el-dropdown-item>Delete</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>Tom</span>
    </el-header>

    <el-container style="height: 1000px; border: 1px solid #eee" direction="horizontal">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu>
          <el-submenu index="1">
            <template slot="title">
              <div @contextmenu="showMenu(ContextMenuData)">
                <vue-context-menu
                  :contextMenuData="ContextMenuData"
                  @newBookName="newBookName">
                </vue-context-menu>
                <span><i class="el-icon-message"></i>我的作品</span>
              </div>
            </template>
            <sub-menu :bookItems="bookItems"
                      @viewArticle="viewArticle"
                      @editArticle="editArticle"></sub-menu>
          </el-submenu>
          <el-menu-item index="2">
            <template slot="title">
              <div @click="showLocalResource">
                <i class="el-icon-menu"></i>
                本地资源
              </div>
            </template>
          </el-menu-item>
          <el-menu-item index="3">
            <template slot="title">
              <div @click="showOnlineResource">
                <i class="el-icon-ice-cream"></i>
                在线引擎
              </div>
            </template>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <el-main>
        <div id="main">
          <transition>
            <keep-alive>
              <router-view></router-view>
            </keep-alive>
          </transition>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>

  import SubMenu from "./SubMenu"
  import axios from 'axios'
  import localStorage from '../util/localStorage'

  export default {
    data() {
      return {
        tempName: "",
        bookItems:localStorage.readItems() || [],
        content: "",
        ContextMenuData: {
          menuName: 'handlerForBookList',
          axis: {x: null, y: null},
          menulists: [
            {fnHandler: 'newBookName', icoName: 'el-icon-more', btnName: '新建书籍'},
          ]
        },
      }
    },
    watch:{
      bookItems:{
          deep:true,
          handler: localStorage.saveItems
      }
    },
    methods: {
      showOnlineResource() {
        this.$router.push({
          path: "/onlineResource"
        })
      },
      viewArticle(params) {
        this.$router.push({
          name: "showArticleInfos",
          params: params
        })
      },
      editArticle(params) {
        this.$router.push({
          name: "editArticle",
          params: params
        })
      },
      showLocalResource() {
        this.$router.push({
          path: "/localResource"
        })
      },
      showMenu(contextMenuData) {
        //绑定window.event
        event.preventDefault();
        var x = event.clientX;
        var y = event.clientY;
        // Get the current location
        contextMenuData.axis = {
          x, y
        }
      },
      newBookName() {
        const bookName = prompt("请输入BookName:", null);
        if (bookName == null) return;
        const patern = /[`~!@#$%^&*()_+<>?:"{},.\/;'[\]]/im;
        if (patern.test(bookName)) {
          alert("含有非法字符！");
          return
        }
        for (var i = 0; i < this.bookItems.length; i++) {
          if (bookName == this.bookItems[i].mode) {
            alert("该书籍名已经存在!");
            return
          }
        }
        this.bookItems.push({
          mode: bookName,
          files: []
        });
      },
      getBookList() {
        axios.get('/api/custom/books/infos/').then(
          response => {
            const data = response.data;
            if (data.status == 200) {
              this.bookItems = JSON.parse(data.res);
            }
          }).catch(err => {
          alert("请求出错了！" + err)
          });
      },
      saveBookItemsDB(){
        axios.post('/api/storage/books/infos/',
            {
              "bookItems":this.bookItems
            },
          ).then(
            response => {
              const data = response.data;
              if (data.status == 200) {
                console.log("storage");
              }
          }).catch(err => {
          alert("请求出错了！" + err);
        });
      }
    },
    mounted() {
      if(this.bookItems.length==0){
        this.getBookList()
      } else {
        this.saveBookItemsDB()
      }
    },
    components: {
      SubMenu,
    }
  }
  ;
</script>

<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }

  .el-menu-item-group__title {
    padding-left: 0px;
  }
</style>
