<template>
  <div class="row">
    <button class="btn btn-danger f-left" @click="relatedRecom">相关推荐</button>
    <relatedArticleInfos :itemIndex="itemIndex" :isRecomShow="isRecomShow" ref="getChildData"></relatedArticleInfos>
  </div>
</template>

<script>
  import PubSub from 'pubsub-js';
  import relatedArticleInfos from './relatedArticleInfos'
  export default {
    name: "relatedArcticles",
    props: {
      itemIndex: Number,
      item:Object
    },
    data() {
      return {
        relatedAID: this.item.ID,
        isRecomShow:false
      }
    },
    components:{
      relatedArticleInfos
    },
    methods: {
      relatedRecom() {
        if(this.$refs.getChildData.recomdArcticles.length){
          this.$refs.getChildData.changeStatus();
          return
        }
        PubSub.publish("relatedAID_" + this.itemIndex, this.relatedAID);
      }
    }
  }
</script>

<style scoped>
  .row {
    margin-top: 0px;
    margin-bottom: -20px;
  }

  .f-left {
    float: left;
    font-size: 8px;
    margin-top: 2px;
    margin-left: 15px;
  }

  .row button{
    border:none;
    outline:none;
  }
</style>
