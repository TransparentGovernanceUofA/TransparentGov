import Vue from 'vue'
import VueRouter from 'vue-router'
import Result from '@/components/Result'
import SearchBox from '@/components/SearchBox'
import AdvancedSearch from '@/components/AdvancedSearch'
import Timeline from '@/components/Timeline'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'SearchBox',
      component: SearchBox
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
      props: true
    },
    {
      path: '/advancedsearch',
      name: 'Advanced Search',
      component: AdvancedSearch
    },
    {
      path: '/timeline',
      name: 'Timeline',
      component: Timeline
    }
  ],
  mode: 'history'
})
