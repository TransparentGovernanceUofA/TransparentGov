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
      // basic query for es; for now searching 'exact term' over all fields
      const query = {
        query: {
          match_phrase: {
            '_all': {
              'query': this.inputField.search,
              'prefix_length': '3',
              'fuzziness': '2',
              'operator': 'and',
            }
            // this.inputField.search
          }
        },
        'highlight': {
          'fields': {
            'title': {
              'no_match_size': 300,
              'number_of_fragments': 0
            },
            'description': {
              'no_match_size': 500,
              'number_of_fragments': 5
            }
          }
        }
      }

      // using axios, get es results
      // console.log('http://162.246.156.217:8080/_search?q=' + this.inputField.search)
      axios.get('http://162.246.156.217:8080/meeting_minutes/modelresult/_search/', {
        params: {
          source: JSON.stringify(query),
          source_content_type: 'application/json'
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
