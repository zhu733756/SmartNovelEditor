import Vue from 'vue'
import App from './App'
import axios from 'axios'
import VueCookie from 'vue-cookie'
import ElementUI from 'element-ui';
import router from "./router"
import 'element-ui/lib/theme-chalk/index.css';
import VueContextMenu from 'vue-contextmenu'

axios.defaults.baseURL="http://127.0.0.1:8000";

Vue.config.productionTip = false;
Vue.use(VueCookie);
Vue.use(VueContextMenu);
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  render: h => h(App)
});
