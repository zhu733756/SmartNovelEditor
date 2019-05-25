<template>
  <div>
    <p v-show="loadingShow" class="f-left">加载中...</p>
    <ul class="list-group" v-show="isRecomShow">
      <li class="list-group-item" v-for="(t,index) in recomdArcticles" :key="index">
        <a :href="t.url" target="_blank">{{t.title}}(来源：{{t.refer}})</a>
      </li>
    </ul>
  </div>

</template>

<script>
  import PubSub from 'pubsub-js';
  import axios from 'axios';

  export default {
    name: "relatedArticleInfos",
    props: {
      itemIndex: Number,
    },
    data() {
      return {
        recomdArcticles: [],
        isRecomShow: false,
        loadingShow: false,
      }
    },
    // computed:{
    //   loadingShow(){
    //     return this.recomdArcticles.length <=0;
    //   }
    // },
    mounted() {
      PubSub.subscribe("pageChanged", (msg, status) => {
        this.isRecomShow = false;
      });
      PubSub.subscribe("relatedAID_" + this.itemIndex.toString(), (msg, d) => {
        this.loadingShow = true;
        axios.post("/api/traceservice/search/", {"id": d.toString()}).then(
          response => {
            this.isRecomShow = true;
            const data = response.data;
            const items = data.length > 10 ? data.slice(0, 10) : data;
            this.recomdArcticles = items.map(item => ({
              "refer": item.refer,
              "score": item.score,
              "title": item.title,
              "url": item.url,
              "content": item.content,
              "AID": item.article_id,
            }));
          }
        ).catch(error => {
          alert("请求出错了！");
        });
        this.loadingShow = this.recomdArcticles.length<=0;
      });
    },
    methods: {
      changeStatus() {
        this.isRecomShow = !this.isRecomShow
      }
    }
  }
</script>

<style scoped>
  ul.list-group {
    margin-bottom: -20px;
    width: 600px;
  }

  .f-left {
    float: left;
    font-size: 8px;
    margin-top: 7px;
    margin-left: 2px;
  }

  ul {
    padding-top: 35px;
    padding-left: 10px;
    padding-bottom: 5px;
  }
</style>
