<template>
  <keep-alive>
    <component :is="tagView" :v="v"></component>
  </keep-alive>
</template>

<script>

  export default {
    name: "pItem",
    props: {
      itemMsg: Object
    },
    computed: {
      tagName() {
        return this.itemMsg.tagName;
      },
      v() {
        return this.itemMsg.val
      },
      tagView() {
        let t;
        switch (this.tagName) {
          case "title":
            t = "comp1";
            break;
          case "p":
            t = "comp1";
            break;
          case "img":
            t = "comp2";
            break;
        }
        return t;
      }
    },
    components: {
      comp1: {
        props: {
          v: String
        },
        template: "<p>{{v}}</p>"
      },
      comp2: {
        props: {
          v: String
        },
        template: "<img :src='v'>"
      }
    }

  }
</script>

<style scoped>

</style>
