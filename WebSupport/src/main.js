// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueCookie from 'vue-cookie'

axios.defaults.baseURL="http://127.0.0.1:8000";
// axios.defaults.baseURL="http://124.204.65.86:14427";

Vue.config.productionTip = false;
Vue.use(VueCookie)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});


