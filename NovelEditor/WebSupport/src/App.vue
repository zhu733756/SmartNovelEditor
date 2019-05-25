<template>
  <div id="app">
    <div class="row">
      <div class="col-sm-3 col-sm-offset-1">
        <div class="row">
          <searchPage></searchPage>
        </div>
        <div class="row">
          <articles></articles>
        </div>
      </div>
      <div class="col-sm-3 col-sm-offset-1">
          <articleParagraphs></articleParagraphs>
      </div>
    </div>
  </div>
</template>

<script>
  import searchPage from './components/searchFrame/search.vue';
  import articles from './components/articles/articles.vue';
  import articleParagraphs from './components/filteredArcticles/articleParagraphs.vue';

  export default {
    name: 'App',
    components: {
      searchPage,
      articles,
      articleParagraphs
    },
    mounted() {
      this.$cookie.set("username",Math.random().toString(36).substr(2),{expire:7});
      this.$cookie.set("_csrf_token",Math.random().toString(36).substr(2),{expire:7});
    }
  }
</script>

<style scope>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
