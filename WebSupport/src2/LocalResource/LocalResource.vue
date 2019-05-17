<template>
  <div>
    <input v-model="searchKey"></input>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "LocalResource",
    data() {
      return {
        searchKey: "斗破苍穹",
        isloading: false,
      }
    },
    mounted() {
      if (this.searchKey) {
        const d = {
          searchKey: this.searchKey
        };
        axios.get("/api/spiders/biquge5200/search/", {params: d}).then(
          response => {
            const data = response.data;
            if (data.status == 200) {
              const jsonData = data.res;
              console.log(jsonData);
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
