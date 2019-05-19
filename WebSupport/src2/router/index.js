import Vue from 'vue'
import Router from 'vue-router'
import OnLineResource from "../OnLineResource/OnLineResource"
import OnLineSearch from "../OnLineResource/OnLineSearch"
import CrawlStatus from "../OnLineResource/CrawlStatus"
import TinyMce from "../TinyMce"
import LocalResource from "../LocalResource/LocalResource"
import ShowArtileInfos from "../ShowArticleInfos/ShowArticleInfos"

Vue.use(Router);

export default new Router({
  routes: [
    {
      path:"/onlineResource",
      component: OnLineResource,
      children:[
        {
          path:"crawlStatus",
          component: CrawlStatus
        },
        {
          path:"onlineSearch",
          component:OnLineSearch
        }
      ]
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
