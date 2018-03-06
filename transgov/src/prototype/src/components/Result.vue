<template>
  <div class="results">
    <top-left-search></top-left-search>

    <b-container fluid>
      <b-row>
        <b-col cols=12>
          <b-btn v-b-toggle.collapse1 variant="primary" class="mt-2">Toggle Timeline</b-btn>
          <b-collapse id="collapse1" class="mt-2">
            <timeline></timeline>
          </b-collapse>
        </b-col>
      </b-row>
    </b-container>

    <search-result-list :test = "ElasticResult"></search-result-list>
    <!-- {{ inputField.search }} -->
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import Timeline from './Timeline.vue'
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
    TopLeftSearch,
    Timeline
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
      console.log('http://162.246.156.217:8080/_search?q=' + this.inputField.search)
      axios.get('http://162.246.156.217:8080/_search?q=', {
        params: {
          q: this.inputField.search
        }
      })
        .then((resp) => {
          console.log(resp)
          this.ElasticResult = resp.data.hits.hits
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
