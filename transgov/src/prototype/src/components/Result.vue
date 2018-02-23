<template>
  <div class="results">
    <top-left-search></top-left-search>
    <search-result-list :test = "ElasticResult"></search-result-list>
    <!-- {{ inputField.search }} -->
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import SearchResultList from './SearchResultList.vue'
import axios from 'axios'

export default{
  props: {
    inputField: {
      type: Object,
      default: () => ({})
    }
  },
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
      console.log('http://199.116.235.49/api/meetings/' + this.inputField.search)
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
