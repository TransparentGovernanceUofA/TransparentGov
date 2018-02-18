import Vue from 'vue'
import Router from 'vue-router'
import Result from '@/components/Result'
import SearchBox from '@/components/SearchBox'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SearchBox',
      component: SearchBox
    },
    {
      path: '/result',
      name: 'Result',
      component: Result
    }
  ]
})
