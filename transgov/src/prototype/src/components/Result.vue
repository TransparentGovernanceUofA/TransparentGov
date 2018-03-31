<template>
  <div class="results">
    <top-left-search :previousInputField="inputField" :advancedForm="advancedFilters"></top-left-search>
    <b-container fluid>
      <b-row>
        <b-col cols="auto">
          <b-btn v-b-toggle.collapse1 variant="primary" class="mt-2">Show/Hide Timeline</b-btn>
          
        </b-col>
        <b-col cols="auto">
          <div class="help-tip">
            <p>The timeline is a way to visualize your search results by the date they occured on.<br/>
              Each bubble shows the committee and day, and a line connects it to the precise location on the timeline at the bottom of the visualization.<br/>
              <strong>Controls:</strong><br/>
              [Mouse Wheel/Pinch]: Zoom <br/>
              [Click + Drag/Swipe]: Scroll left and right. Also scroll up or down there are enough results to stack.<br/>
              [Select an Item]: Jump immediately to the corresponding search result card below the timeline.
            </p>
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
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
        committee: null,
        date: null,
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
          multi_match: {
            'query': this.inputField.search,
            'type': 'cross_fields',
            'fields' : [ '_all' ],
            'fuzziness': '2',
            'operator': 'and',
            }

        },
        'highlight': {
          'fields': {
            '*': {

            },
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
        this.advancedFilters.committee = advancedArray[2]
        if (this.advancedFilters.committee === '') {
          this.advancedFilters.committee = null
        }

        this.advancedFilters.date = advancedArray[4]
        if (this.advancedFilters.date === '') {
          this.advancedFilters.date = null
        }

        this.advancedFilters.people = advancedArray[6]
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
