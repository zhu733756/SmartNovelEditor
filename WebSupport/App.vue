<template>
    <header headerData="headerData"></header>
    <body bodyData="bodyData"></body>
</template>

<script>
    import header from './components/header/header';
    import body from './components/body/body'
    export default {
        name: "App",
        data(){
          return {
            headerData:[],//{"type":"a type in p,img,header,subtitle,title","data":"data of the type"}
            bodyData:[]
          }
        },
        components:{
          header,
          body
        }
    }
</script>

<style scoped>

</style>
