<template>
  <div class="results">
    <top-left-search></top-left-search>
    <search-result-list :test = "ElasticResult"></search-result-list>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import SearchResultList from './SearchResultList.vue'
import axios from 'axios'

export default{
  components: {
    SearchResultList,
    TopLeftSearch
  },
  name: 'ElasticResults',
  data () {
    return {
      ElasticResult: {}
    }
  },
  created () {
    this.fetchData()
  },

  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData () {
      axios.get('http://199.116.235.49/api/meetings/')
        .then((resp) => {
          console.log(resp)
          this.ElasticResult = resp.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
</style>
