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
      axios.get('https://cors-anywhere.herokuapp.com/http://162.246.156.217:9200/_search')
        .then((resp) => {
          this.ElasticResult = resp.data.hits.hits
          console.log(resp)
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
