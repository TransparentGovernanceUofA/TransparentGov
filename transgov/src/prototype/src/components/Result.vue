<template>
  <div class="results">
    <top-left-search :previousInputField="inputField"></top-left-search>
    <b-container fluid>
      <b-row>
        <b-col cols=12>
          <b-btn v-b-toggle.collapse1 variant="primary" class="mt-2">Toggle Timeline</b-btn>
          <b-collapse id="collapse1" class="mt-2">
            <timeline :results="ElasticResult"></timeline>
          </b-collapse>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols=8>
          <search-result-list :test = "ElasticResult"></search-result-list>
          <!-- {{ inputField.search }} -->
        </b-col>
        <b-col cols=4>
          <b-card class="mt-4 md-elevation-3" header="Exploration Graph"
                header-tag="header">
            <vis-network></vis-network>
          </b-card>
          
        </b-col>
      </b-row>
    </b-container>
    
    
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import Timeline from './Timeline.vue'
import SearchResultList from './SearchResultList.vue'
import VisNetwork from './VisNetwork.vue'
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
    TopLeftSearch,
    Timeline,
    VisNetwork
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
    '$route': 'fetchData',
    inputField: {
      handler: 'fetchData',
      deep: true
    }
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
  @import url("https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css");
</style>
