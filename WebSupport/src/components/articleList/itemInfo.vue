<template>
  <div :style="{background: bgColor}"
         @mouseenter="isShowLi(true)"
         @mouseleave="isShowLi(false)" class="item-articles">
      <div class="fontsize">
        <h3>
          <span><a :href="item.url" target="_blank">{{item.title}}</a></span>
          <span><button class="btn btn-danger" @click="doDelete" v-show="isDeleteShow">不感兴趣</button></span>
        </h3>
      </div>
      <p class="fontsize">文章ID：{{item.AID}} | 匹配得分：{{item.score}} </p>
      <p class="fontsize"> 项目名称：{{item.table}} | 来源：{{item.refer}} | 平台：{{item.platform}}</p>
      <p>
        <span class="fontsize">发布时间：{{item.pub_date}}</span>
        <span class="fontsize"><button class="btn btn-danger" v-show="isDeleteShow" @click="typeSetting">一键排版</button></span>
      </p>
    </div>
</template>

<script>
  import relatedArcticles from "./relatedArticles";
  import PubSub from "pubsub-js";

  export default {
    name: "itemInfo",
    props: {
      item: Object,
      itemIndex:Number,
      deleteItems: Function
    },
    components: {
      relatedArcticles
    },
    data() {
      return {
        bgColor: "white",
        isDeleteShow: false,
        relatedAid:this.item.ID,
      }
    },
    methods: {
      isShowLi(check) {
        if (check) {
          this.bgColor = "#DDDDDD";
          this.isDeleteShow = true;
        } else {
          this.bgColor = "white";
          this.isDeleteShow = false;
        }
      },
      doDelete() {
        this.deleteItems(this.itemIndex)
      },
      typeSetting() {
        PubSub.publish("filtered", this.relatedAid);
      },
    }
  }
</script>

<style scoped>

  p{
    margin-top: 1px;
    margin-bottom: 1px;
  }
  .btn{
    border:none;
    outline:none;
    margin-bottom: -6px;
    padding: 8px 12px;
    float: right;
    font-size: 8px;
  }
  .fontsize{
    line-height: 2.24;
  }
  .item-articles{
    width: 600px;
  }
  a{
    box-shadow: none;
  }
</style>
