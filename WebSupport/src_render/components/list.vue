<template>
  <div>
    <div v-for="(itemMsg,index) in articleMsg" :key="index">
      <item :itemMsg="itemMsg" ref="childItem"></item>
    </div>
  </div>
</template>

<script>
  import item from "./item";
  import axios from 'axios';

  export default {
    name: "list",
    data() {
      return {
        articleMsg: [],
        //{"tag":"a tag","val":"value of the tag","style":"传递的样式"}
      }
    },
    components: {
      item
    },
    mounted() {
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
      console.log(this.articleMsg);
    }
  }
</script>

<style scoped>

</style>
