<template>
<div class="row">
  <ul v-show="isPageShow" class="pagination search-wrapper" :maxPageNum="maxPageNum" >
    <li  v-show="isPrevShow">
      <a href="javascript:void(0)"  @click="prev">上一页</a>
    </li>
    <li  v-show="isFirstShow" >
      <a href="javascript:void(0)" @click="first">首页</a>
    </li>
    <li v-for="(index,pag) in pageSum" :key="index" :class="{active:isActive(index)}" >
      <a href="javascript:void(0)"  @click="sendPage(index)" >{{index}}</a>
    </li>
    <li v-show="isEllipsisShow">
      <a href="javascript:void(0)">...</a>
    </li>
    <li  v-show="isNextShow">
      <a href="javascript:void(0)" @click="next">下一页</a>
    </li>
    <li  v-show="isLastShow">
      <a href="javascript:void(0)" @click="last">尾页</a>
    </li>
  </ul>
</div>
</template>

<script>
  import PubSub from "pubsub-js"
    export default {
        name: "page",
        props:{
          perPage:{
            type:Number,
            default:5
          },
          maxPageNum:{
            type:Number,
            default:1
          },
          currentPageNum:{
            type:Number,
            default:1
          },
          perPageNum : {
            type : Number,
            default : 8
          },
          isPageShow:Boolean
        },
        watch:{
          currentPageNum(p1,p2){
              PubSub.publish("pageChanged",true)
          }
        },
        computed:{
          pageSum:function(){
            return Math.min(this.currentPageNum,this.perPage)
          },
          isPrevShow:function(){
            return this.currentPageNum>1
          },
          isFirstShow:function(){
            return this.currentPageNum>=1
          },
          isNextShow:function(){
            return this.currentPageNum<=this.maxPageNum-1
          },
          isLastShow:function(){
            return this.currentPageNum<this.maxPageNum
          },
          isEllipsisShow:function(){
            return this.currentPageNum > this.perPages
          },
        },
        methods:{
          sendPage:function (page) {
            if (page!=this.currentPageNum)
              this.$emit("queryNum",page);
          },
          first:function () {
            this.sendPage(1)
          },
          last:function () {
            this.sendPage(this.maxPageNum)
          },
          prev:function () {
            if (this.isPrevShow)
              {this.sendPage(this.currentPageNum-1)}
          },
          next:function () {
            if (this.isNextShow)
              {this.sendPage(this.currentPageNum+1)}
          },
          isActive:function(ind){
            return ind==this.currentPageNum?"active":""
          }
        }
    }
</script>

<style scoped>
  .row {
    margin-top: 15px;
    margin-bottom: 15px;
  }

  .pagination li.active, .pagination .active >a {
    color: #3c3c3c;
    background-color: white;
    border-color: #ddd;
    outline: none;
  }

  .pagination >li >a {
     color: #3c3c3c;
  }
</style>
