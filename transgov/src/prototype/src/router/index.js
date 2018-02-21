import Vue from 'vue'
import Router from 'vue-router'
import Result from '@/components/Result'
import SearchBox from '@/components/SearchBox'
import AdvancedSearch from '@/components/AdvancedSearch'

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
    },
    {
      path: '/advancedsearch',
      name: 'Advanced Search',
      component: AdvancedSearch
    }
  ]
})
