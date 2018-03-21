<template>
  <div class="results">
    <top-left-search :previousInputField="inputField" :advancedForm="advancedFilters"></top-left-search>
    <b-container fluid>
      <b-row>
        <b-col cols=12>
          <b-btn v-b-toggle.collapse1 variant="primary" class="mt-2">Show/Hide Timeline</b-btn>
          <b-collapse id="collapse1" class="mt-2">
            <timeline :results="ElasticResult"></timeline>
          </b-collapse>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <search-result-list :test = "ElasticResult"></search-result-list>
          <!-- {{ inputField.search }} -->
        </b-col>
        <!--
        <b-col cols=4>
          <b-card class="mt-4 md-elevation-3" header="Exploration Graph"
                header-tag="header">
            <vis-network></vis-network>
          </b-card>

        </b-col>
        -->
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
    },
    // query is accessing whats appended to the URL, ie /result/query
    query: {
      type: String
    },
    advanced: {
      type: String
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
      ElasticResult: {},
      advancedFilters: {
        topic: null,
        committee: null,
        date: null,
        text: null,
        people: null
      }
    }
  },
  created () {
    // console.log('Created----' + this.query)
    this.parseQuery()
    this.fetchData()
  },

  watch: {
    // query is accessing whats appended to the URL, ie /result/query
    query: function () {
      // console.log('query Changed')
      this.parseQuery()
      this.fetchData()
    },
    advanced: function () {
      // console.log('advanced Changed')
      this.parseQuery()
      this.fetchData()
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
              'operator': 'and'
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
              'fragment_size': 300,
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
    },

    parseQuery () {
      
      let queryArray = this.query.replace('search:', '')
      this.inputField.search = queryArray

      var advancedArray = this.advanced.split(':')
      if (advancedArray[1] !== 'false') {
        this.advancedFilters.topic = advancedArray[2]
        if (this.advancedFilters.topic === '') {
          this.advancedFilters.topic = null
        }

        this.advancedFilters.committee = advancedArray[4]
        if (this.advancedFilters.committee === '') {
          this.advancedFilters.committee = null
        }

        this.advancedFilters.date = advancedArray[6]
        if (this.advancedFilters.date === '') {
          this.advancedFilters.date = null
        }

        this.advancedFilters.text = advancedArray[8]
        if (this.advancedFilters.text === '') {
          this.advancedFilters.text = null
        }

        this.advancedFilters.people = advancedArray[10]
        if (this.advancedFilters.people === '') {
          this.advancedFilters.people = null
        }
      }
      // console.log(this.advancedFilters)
      // console.log(this.inputField.search)
    }
  }
}

</script>

<style>
</style>
