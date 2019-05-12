import Vue from 'vue'
import App from './App'
import axios from "axios"

axios.defaults.baseURL="http://127.0.0.1:8000";

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
});
