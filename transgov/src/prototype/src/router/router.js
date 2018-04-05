import Vue from 'vue'
import VueRouter from 'vue-router'
import Result from '@/components/Result'
import SearchBox from '@/components/SearchBox'
import AdvancedSearch from '@/components/AdvancedSearch'
import Timeline from '@/components/Timeline'
import ViewPDF from '@/components/ViewPDF'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'SearchBox',
      component: SearchBox
    },
    {
      // the result page use dynamic route matching to store the query as part of the URL
      path: '/result/:query/:committees/:people/:dateStart/:dateEnd',
      name: 'Result',
      component: Result,
      props: true
    },
    {
      // the PDF results page uses dynamic route matching to make stable links to pdf files
      path: '/file/:file_id',
      name: 'View PDF',
      component: ViewPDF,
      props: true
    },
    {
      path: '/advancedsearch/:query/:committees/:people/:dateStart/:dateEnd',
      name: 'Advanced Search',
      component: AdvancedSearch,
      props: true
    }
  ],
  mode: 'history'
})
