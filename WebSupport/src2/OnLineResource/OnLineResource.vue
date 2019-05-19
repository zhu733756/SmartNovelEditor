<template>
  <div class="input-label">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="在线搜索" name="onlineSearch"></el-tab-pane>
      <el-tab-pane label="爬虫进度条" name="crawlStatus"></el-tab-pane>
    </el-tabs>
    <transition>
      <keep-alive>
        <router-view></router-view>
      </keep-alive>
    </transition>
  </div>
</template>

<script>
  export default {
    name: "OnLineResource",
    data() {
      return {
        activeName: 'onlineSearch'
      }
    },
    methods: {
      handleClick(tab, event) {
        this.$router.push({
          path:"/onlineResource/"+this.activeName
        })
      }
    }
  }
</script>

<style scoped>

  div.input-label {
    /*border: solid 1px ;*/
    width: 60%;
    margin-left: 20px;
  }

  div > el-button {
    width: 80%;
  }

  a:link {
    color: black;
    text-decoration: none;
  }

  a:visited {
    color: purple;
    text-decoration: none;
  }

  a:hover {
    color: red;
    text-decoration: none;
  }

</style>
