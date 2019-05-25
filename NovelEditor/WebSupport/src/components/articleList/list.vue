<template>
  <div class="row">
    <ul class="list-group search-wrapper">
      <li class="list-group-item " v-for="(item,index) in filteredItems" :key="computedItem(index)">
        <itemInfo :item="item"  :deleteItems="deleteItems" :itemIndex="computedItem(index)"></itemInfo>
        <relatedArticles :item="item" :itemIndex="computedItem(index)"></relatedArticles>
      </li>
    </ul>
  </div>
</template>

<script>
  import itemInfo from "./itemInfo.vue"
  import relatedArticles from "./relatedArticles.vue"

  export default {
    name: "list",
    props: {
      filteredItems: Array,
      deleteItems: Function,
      computedIndex:Number
    },
    methods:{
      computedItem:function (index) {
        return this.computedIndex+index
      }
    },
    components: {
      itemInfo,
      relatedArticles,
    },
  }
</script>

<style scoped>
  .list-group-item {
    border: 0px;
    margin: 1px 0px;
    padding: 0px 0px;
    padding-bottom: 23px;
  }
</style>
