<template>
  <div class="Articles">
    <div class="fontsize">
      <h3 v-show="articleItemInfos.isPromptShow">输入文本内容，点击按钮或Enter进行搜索！</h3>
    </div>
    <div class="fontsize"><h3 v-show="articleItemInfos.loading">正在搜索中.....</h3></div>
    <div class="fontsize"><h3 v-show="!articleItemInfos.errMsg">{{articleItemInfos.errMsg}}</h3></div>
    <list :filteredItems="filteredItem"
          :deleteItems="deleteItems"
          :computedIndex="computedIndex"></list>
    <page :maxPageNum="maxPageNum"
          :currentPageNum="articleItemInfos.currentPageNum"
          :isPageShow="isPageShow"
          @queryNum="handlePage"></page>
  </div>
</template>

<script>
  import list from "../articleList/list.vue";
  import page from "../articlePage/page.vue";
  import PubSub from "pubsub-js";
  import axios from "axios";
  import localStorage from '../../util/localStorage.js'

  export default {
    name: "arcticles",
    data() {
      return {
        articleItemInfos:{
          errMsg: localStorage.readItems()?localStorage.readItems().errMsg :"",
          loading: localStorage.readItems()?localStorage.readItems().loading : false,
          isPromptShow: localStorage.readItems()?localStorage.readItems().isPromptShow : true,
          articleItems: localStorage.readItems()?localStorage.readItems().articleItems : [],
          currentPageNum: localStorage.readItems()?localStorage.readItems().currentPageNum : 1,
        }
      }
    },
    components: {
      list,
      page,
    },
    watch: {
      articleItemInfos: {
        deep: true,
        handler: localStorage.saveItems
      }
    },
    computed: {
      maxPageNum: function () {
        return Math.floor(this.articleItemInfos.articleItems.length / this.perPageNum) + 1;
      },
      perPageNum: function () {
        return 8
      },
      isPageShow: function () {
        return this.articleItemInfos.articleItems.length > 0;
      },
      filteredItem: function () {
        const startSlice = (this.articleItemInfos.currentPageNum - 1) * this.perPageNum;
        const endSlice = this.articleItemInfos.currentPageNum * this.perPageNum;
        return this.articleItemInfos.articleItems.slice(startSlice, endSlice);
      },
      //索引偏移量
      computedIndex: function () {
        return this.perPageNum * (this.articleItemInfos.currentPageNum - 1);
      },
    },
    mounted() {
      PubSub.subscribe("searchKey", (msg, searchCon) => {
        this.articleItemInfos.isPromptShow = false;
        this.articleItemInfos.loading = true;
        this.articleItemInfos.articleItems = [];
        const d = {"content": searchCon};
        axios.post("api/traceservice/search/", d).then(
          response => {
            const items = response.data;
            this.articleItemInfos.loading = false;
            this.articleItemInfos.articleItems = items.map(item => ({
              "table": item.table,
              "refer": item.refer,
              "score": item.score,
              "pub_date": item.publish_date,
              "title": item.title,
              "url": item.url,
              "platform": item.platform,
              "content": item.content,
              "AID": item.article_id,
              'ID': item.id,
            }));
          }
        ).catch(error => {
          alert("请求出错了！");
          this.articleItemInfos.isPromptShow = true;
          this.articleItemInfos.loading = false;
          this.errMsg = "请求失败！"
        });
      });
    },

    methods: {
      handlePage(p) {
        this.articleItemInfos.currentPageNum = p
      },
      deleteItems(index) {
        this.articleItemInfos.articleItems.splice(index, 1)
      },
    }

  }
</script>

<style>
  h3 {
    display: block;
    font-size: 1.17em;
    font-weight: bold;
  }

  .fontsize {
    line-height: 1.54;
    font-family: arial, sans-serif;
    font-size: small;
    text-align: left;
  }

  a:hover {
    background: none;
    box-shadow: none;
    text-decoration: underline;
    outline: none;
  }
</style>

