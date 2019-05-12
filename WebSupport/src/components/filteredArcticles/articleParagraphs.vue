<template>
  <div id="filtered-articles">
    <div v-for="(itemMsg,index) in articleMsg" :key="index">
      <pItem :itemMsg="itemMsg" ref="childItem"></pItem>
    </div>
  </div>
</template>

<script>
  import PubSub from 'pubsub-js';
  import pItem from './pItem';
  import axios from 'axios';
  import $ from 'jquery';

  export default {
    name: "filteredArcticles",
     data() {
      return {
        articleMsg: [],
        //{"tag":"a tag","val":"value of the tag","style":"传递的样式"}
      }
    },
    mounted() {
      PubSub.subscribe("filtered", (msg, filteredAID) => {
        console.log(filteredAID);
        axios.get("/api/search/htmlcontent/").then(
          response => {
            const data = response.data;
            for (const d in data) {
              this.articleMsg.push(data[d]);
            }
          }
        ).catch(error => {
          alert("请求出错了！");
        });
      })
    },
    components: {
      pItem
    },
  }

</script>

<style scoped>

</style>
