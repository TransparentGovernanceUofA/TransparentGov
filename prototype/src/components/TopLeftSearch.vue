<template>
  <div class="top-left">
    <router-link to="/">
      <img src="./../assets/transparentGovernance2.png" id = "logo">
    </router-link>
    <input id="input-box">
    <div id = "results">
      <search-result-list id="result-view"></search-result-list>
    </div>
    <div id='"elastic-result'>
      {{ ElasticResult }}
    </div>
  </div>
</template>

<script>
import SearchResultList from './SearchResultList.vue'
import axios from 'axios'

export default{
  components: {
    SearchResultList
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
          // this.ElasticResult = resp.data[0]
          this.ElasticResult = resp.data
          console.log(this.ElasticResult)
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
#input-box{
  width: 300px;
}

#result-view{
  position: absolute;
  top: 10%;
  left: 15%;
}
</style>
