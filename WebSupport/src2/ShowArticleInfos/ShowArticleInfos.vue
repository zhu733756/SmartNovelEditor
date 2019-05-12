<template>
  <div class="article-show">
    <div class="title" align="center" v-if="!isClick">
      <h2>
        <a href="javascript:void(0)" @click="editArticles">
          {{title}}
        </a>
      </h2>
    </div>
    <div class="paragraphs">
    </div>
    <router-view></router-view>
  </div>
</template>

<script>

  import $ from "jquery"
  export default {
    name: "viewArticle",
    data() {
      return {
        isClick: false
      }
    },
    computed: {
      content: function () {
        return this.$route.params.content
      },
      title: function () {
        return this.$route.params.file
      },
      params: function () {
        return this.$route.params
      }
    },
    mounted(){
      const temp = $("div.paragraphs").html(this.content);
      console.log(temp);
      return temp
    },
    methods: {
      editArticles() {
        this.$router.push(
          {
            name: "editArticle",
            params: this.params
          }
        )
      }
    },
  }
</script>

<style scoped>
  div.article-show {
    margin: 10px 50px;
    max-width: 1000px;
    width: auto;
  }

  div.title, div.paragraphs {
    width: 100%;
  }

  p {
    text-indent: 50px;
    padding-bottom: 2px;
    width: 100%;
    word-wrap: break-word;
    font-size: 14px;
  }

  a:link {
    color: blue;
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
