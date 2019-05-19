<template>
  <div>
    <template v-for="(item,ind) in bookItems">
      <el-submenu index="1"  :key="ind" :index="item.mode">
        <template slot="title" style="padding-left:10px">
          <div @contextmenu="showMenu1(ind)">
            <vue-context-menu
              :contextMenuData="childMenuData"
              :transferIndex="transferIndex"
              @newData="newData(item)"
              @editBookName="editBookName(item)"
              @deleteAll="deleteAll(item)">
            </vue-context-menu>
            <span slot="title"><i class="el-icon-notebook-2"></i>{{ item.mode }}</span>
          </div>
        </template>
        <template style="padding-left:10px">
          <div v-for="(file,ind2) in item.files" :key="file+'_'+ind2">
            <div @contextmenu="showMenu2(computedIndex(ind,ind2))">
              <vue-context-menu
                :contextMenuData="childMenuData2"
                :transferIndex="transferIndex2"
                @edit="edit(item.mode,file)"
                @editTitle="editTitle(item,file)"
                @deleteArticle="deleteArticle(item,file)">
              </vue-context-menu>
              <el-menu-item @click="view(item.mode,file)">
                <span slot="title">
                   {{ file }}
                </span>
              </el-menu-item>
            </div>
          </div>
        </template>
      </el-submenu>
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
        transferIndex: null, // Show the menu that was clicked
        childMenuData: {
          menuName: Math.random().toString(36).substr(2),
          axis: {x: null, y: null},
          menulists: [
            {fnHandler: 'newData', icoName: 'el-icon-more', btnName: '新建章节'},
            {fnHandler: 'editBookName', icoName: 'el-icon-more', btnName: '修改书名'},
            {fnHandler: 'deleteAll', icoName: 'el-icon-more', btnName: '删除所有'},
          ]
        },
        transferIndex2: null, // Show the menu that was clicked
        childMenuData2: {
          menuName: "childMenuData2",
          axis: {x: null, y: null},
          menulists: [
            {fnHandler: 'edit', icoName: 'el-icon-more', btnName: '编辑'},
            {fnHandler: 'editTitle', icoName: 'el-icon-more', btnName: '修改标题'},
            {fnHandler: 'deleteArticle', icoName: 'el-icon-more', btnName: '删除'},
          ]
        },
        content: "",
      }
    },
    methods: {
       computedIndex(ind,ind2) {
        var sumIndex=0;
        while (ind >=1) {
          sumIndex += this.bookItems[ind-1].files.length;
          ind--;
        }
        return sumIndex+ind2
      },
      showMenu1(index) {
        this.transferIndex = index; // tranfer index to child component
        event.preventDefault();
        var x = event.clientX;
        var y = event.clientY;
        this.childMenuData.axis = {
          x, y
        };
      },
      showMenu2(index) {
        console.log(index)
        this.transferIndex2 = index; // tranfer index to child component
        event.preventDefault();
        var x = event.clientX;
        var y = event.clientY;
        this.childMenuData2.axis = {
          x, y
        };
      },
      editBookName(item){
        const bookName = prompt("请修改bookName:", item.mode);
        if (bookName == null || bookName == item.mode ) return;
        const patern = /[`~!@#$%^&*()_+<>?:"{},.\/;'[\]]/im;
        if (patern.test(bookName)) {
          alert("含有非法字符！");
          return
        }
        const index= this.bookItems.indexOf(item);
        this.bookItems[index].mode=bookName;
        this.bookItems["modify_link_to"]=item.mode;
      },
      newData(item) {
        const mode = item.mode;
        const files = item.files;
        const articleName = prompt("请输入ArticleName:", null);
        if (articleName == null) return;
        const patern = /[`~!@#$%^&*()_+<>?:"{},.\/;'[\]]/im;
        if (patern.test(articleName)) {
          alert("含有非法字符！");
          return
        }
        for (var i = 0; i < files.length; i++) {
          if (articleName == files[i]) {
            alert("该章节已经存在!");
            return
          }
        }
        for (var i = 0; i < this.bookItems.length; i++) {
          if (mode == this.bookItems[i].mode) {
            this.bookItems[i].files.push(articleName);
          }
        }
        const params = {
          mode: mode,
          file: articleName,
          content: ""
        };
        this.$emit("editArticle", params)
      }
      ,
      deleteAll(item) {
        console.log("删除所有！");
        const index = this.bookItems.indexOf(item);
        if (index >= 0) {
          this.bookItems.splice(index, 1)
        }
      }
      ,
      edit(mode, file) {
        this.getCustomArticle(mode,file,"editArticle");
      },
      editTitle(item,file) {
        const title = prompt("请输入articleName:", file);
        if (title == null || title == file) return;
        const patern = /[`~!@#$%^&*()_+<>?:"{},.\/;'[\]]/im;
        if (patern.test(title)) {
          alert("含有非法字符！");
          return
        }
        const index= this.deleteArticle(item,file);
        this.bookItems[index].files.push(title);
      },
      deleteArticle(item,file) {
        console.log("delete");
        const index= this.bookItems.indexOf(item);
        const fileIndex=this.bookItems[index].files.indexOf(file);
        this.bookItems[index].files.splice(fileIndex,1)
        return index
      },
      view(mode, file) {
        this.getCustomArticle(mode,file,"viewArticle");
      },
      getCustomArticle(mode,file,msg) {
        console.log(msg);
        var d = {
          mode: mode,
          file: file
        };
        axios.get("/api/custom/articles/", {params: d}).then(
          response => {
            const data = response.data;
            if (data.status == 200) {
              d["content"] = data.content;
              this.$emit(msg, d)
            }
          }).catch(
          err => {
            alert("请求出错了！")
          });
      }
    }
  }
</script>

<style scoped>

</style>
