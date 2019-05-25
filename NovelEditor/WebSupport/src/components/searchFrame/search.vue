<template>
  <div class="RNNXgb">
    <div class="SDKEP">
      <div class="a4bIc">
        <div class="vdLsw gsfi"></div>
        <input class="gLFyf gsfi" v-model="searchKey" @keyup.enter="search" placeholder="腾讯">
      </div>
      <div class="JC0tCe">
        <button type="button" @click="search"><span class="icon-search"></span></button>
      </div>
    </div>
  </div>
</template>

<script>

  import PubSub from 'pubsub-js';

  export default {
    name: "searchPage",
    data() {
      return {
        searchKey: '',
      }
    },
    methods: {
      search() {
        const key = this.searchKey.trim();
        if (key) {
          PubSub.publish("searchKey", key);
        } else {
            alert("输入的字段不能为空！");

        }
      },

    }
  };

</script>

<style scoped>

  .RNNXgb {
    background: #fff;
    display: flex;
    border: 1px solid #dfe1e5;
    width: auto;
    border-radius: 24px;
    z-index: 3;
    height: 44px;
    margin: 0 auto;
    /*margin-left: 36px;*/
  }


  .SDKEP {
    flex: 1;
    display: flex;
    padding: 5px 4px 0 16px;
    padding-left: 20px;
  }

  .a4bIc {
    display: flex;
    flex: 1;
    flex-wrap: wrap;
  }

  .vdLsw {
    color: transparent;
    flex: 100%;
    white-space: pre;
  }

  .gsfi {
    font: 16px arial, sans-serif;
    line-height: 34px;
    height: 34px !important;
  }

  .gLFyf {
    box-shadow: none;
    background-color: transparent;
    border: none;
    margin: 0;
    padding: 0;
    color: rgba(0, 0, 0, .87);
    word-wrap: break-word;
    outline: none;
    display: flex;
    flex: 100%;
    -webkit-tap-highlight-color: transparent;
    margin-top: -37px;
  }

  .JC0tCe {
    display: flex;
    cursor: pointer;
    align-items: center;
    border: 0;
    background: transparent;
    outline: none;
    width: 44px;
    line-height: 44px;
    margin-bottom: 3px;
}
  .JC0tCe>button{
    line-height: 23px;
  }

</style>
