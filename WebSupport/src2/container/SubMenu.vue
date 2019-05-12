<template>
  <div>
    <template v-for="(item,ind) in bookItems">
      <el-submenu index="1" v-if="item.files.length>0" :key="ind" :index="item.mode">
        <template slot="title" style="padding-left:10px">
          <div @contextmenu="showArticleMenu(childMenuData)">
            <vue-context-menu
              :contextMenuData="childMenuData"
              @newData="newData"
              @deleteAll="deleteAll"
            >
            </vue-context-menu>
            <span slot="title"><i class="el-icon-menu"></i>{{ item.mode }}</span>
          </div>
        </template>
        <template style="padding-left:10px">
          <div v-for="(file,ind2) in item.files" :key="file">
            <el-menu-item @click="view(item.mode,file)" >
              <span slot="title">
                 {{ file }}
              </span>
            </el-menu-item>
          </div>
        </template>
      </el-submenu>
      <el-menu-item v-else :index="item.mode" :key="ind" style="padding-left: 50px;">
        <div @contextmenu="showArticleMenu(childMenuData)">
          <vue-context-menu
            :contextMenuData="childMenuData"
            @newData="newData"
            @deleteAll="deleteAll"
          ></vue-context-menu>
          <span slot="title"><i class="el-icon-menu"></i>{{ item.mode }}</span>
        </div>
      </el-menu-item>
    </template>
  </div>
</template>

<script>
  import axios from "axios"

  export default {
    name: "SubMenu",
    props: [
      'bookItems'
    ],
    data() {
      return {
        childMenuData: {
          menuName: Math.random().toString(36).substr(2),
          axis: {x: null, y: null},
          menulists: [
            {fnHandler: 'newData', icoName: 'el-icon-more', btnName: '新建章节'},
            {fnHandler: 'deleteAll', icoName: 'el-icon-more', btnName: '删除所有'},
          ]
        },
        content: "",
        data :{}
      }
    },
    watch: {
      data: function (val) {
          axios.get("/api/custom/articles/", {params: val}).then(
            response => {
              const data = response.data;
              if (data.status == 200) {
                const content = data.content;
                if (content) {
                  const params=val;
                  params["content"] = content;
                  this.$emit("viewArticle", params)
                }
              }
            }).catch(
            err => {
              alert("请求出错了！")
            });
        },
    },
    methods: {
      showArticleMenu(childMenuData) {
        this.$emit("showArticleMenu", childMenuData)
      },
      newData() {
        console.log("new data!")
      },
      deleteAll() {
        console.log("删除所有！")
      },
      view(mode,file) {
        console.log("view");
        this.data={
          mode:mode,
          file:file
        }
      },
    }
  }
</script>

<style scoped>

</style>
