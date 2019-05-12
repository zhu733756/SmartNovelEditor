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
                     @newdata="newdata">
                   </vue-context-menu>
                  <span><i class="el-icon-message"></i>我的作品</span>
                </div>
            </template>
            <!--url:[{mode:多兰大陆,files:[第一章，第二章]},....]-->
            <sub-menu :bookItems="bookItems" @viewArticle="viewArticle" @showArticleMenu="showMenu"></sub-menu>
          </el-submenu>
          <el-menu-item index="2">
            <!--url:[{bookname:斗破苍穹,author:天蚕土豆,type:novel,articleList:[]},....]-->
            <template slot="title">
              <div @click="showLocalResource">
                  <i class="el-icon-menu"></i>
                  本地资源
              </div>
            </template>
          </el-menu-item>
          <el-menu-item index="3">
            <!--url:[{bookname:斗破苍穹,author:天蚕土豆,type:novel,spider:biquge5200,progressBar:50%,status:preparing},....]-->
            <template slot="title">
              <div @click="showCrawlStaus">
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

  export default {
    name: "home",
    data() {
      return {
        tempName: "",
        bookItems: [],
        content: "",
        ContextMenuData: {
          menuName: 'demo1',
          axis: {x: null, y: null},
          menulists: [
            {fnHandler: 'newdata', icoName: 'el-icon-more', btnName: '新建书籍'},
          ]
        },
      }
    },
    methods: {
      showCrawlStaus() {
        this.$router.push({
          path: "/crawlStatus"
        })
      },
      viewArticle(params){
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
      newdata() {
        console.log('newdata!')
      }
    },
    mounted() {
      axios.get('/api/custom/books/infos/').then(
        response => {
          const data = response.data;
          if (data.status == 200) {
            this.bookItems = JSON.parse(data.res);
          }
        }).catch(err => {
        alert("请求出错了！" + err);
      });
    }
    ,
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
