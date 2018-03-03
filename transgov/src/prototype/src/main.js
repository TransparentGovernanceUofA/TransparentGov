import Vue from 'vue'
import App from './App'
import router from './router/router.js'
import store from './store/store.js'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'

Vue.use(VueMaterial)

import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue)

// import { MdButton } from 'vue-material/dist/components'
// import 'vue-material/dist/vue-material.min.css'

// Vue.use(MdButton)
// Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store: store
})
