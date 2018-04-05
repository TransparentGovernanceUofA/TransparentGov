import Vue from 'vue'
import App from './App'
import router from './router/router.js'
import store from './store/store.js'

import VueMaterial from 'vue-material'
import BootstrapVue from 'bootstrap-vue'
import 'vue-material/dist/vue-material.min.css'
import datePicker from 'vue-bootstrap-datetimepicker'
import 'bootstrap/dist/css/bootstrap.css'
import 'eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css'
import VueModalTor from 'vue-modaltor'

Vue.use(VueModalTor)
Vue.use(datePicker)
Vue.use(VueMaterial)

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
