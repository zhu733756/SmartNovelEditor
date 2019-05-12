import Vue from 'vue'
import Router from 'vue-router'
import CrawlStatus from "../CrawlStatus/CrawlStatus"
import TinyMce from "../TinyMce"
import LocalResource from "../LocalResource/LocalResource"
import ShowArtileInfos from "../ShowArticleInfos/ShowArticleInfos"

Vue.use(Router);

export default new Router({
  routes: [
    {
      path:"/crawlStatus",
      component: CrawlStatus
    },
    {
      name:"editArticle",
      path:"/editArticle/:mode/:file",
      component: TinyMce
    },
    {
      name:"showArticleInfos",
      path:"/showArticleInfos/:mode/:file",
      component: ShowArtileInfos
    },

    {
      path: "/localResource",
      component: LocalResource
    },

  ]
})
