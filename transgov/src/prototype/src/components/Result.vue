<template>
  <div class="results">
    <top-left-search :previousInputField="inputField" :advancedForm="advancedFilters"></top-left-search>
    <!-- {{ advancedFilters }} -->
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
    committees: {
      type: String
    },
    people: {
      type: String
    },
    dateStart: {
      type: String
    },
    dateEnd: {
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
        committee: [],
        people: [],
        date_end: null,
        date_start: null
      }
    }
  },
  created () {
    this.parseQuery()
    // this.fetchData()
  },

  watch: {
    // query is accessing whats appended to the URL, ie /result/query
    query: function () {
      // console.log('query Changed')
      this.parseQuery()
      // this.fetchData()
    },
    advanced: function () {
      console.log('advanced Changed')
      this.parseQuery()
      // this.fetchData()
    }
  },

  methods: {
    fetchData () {
      const query = {
        query: {
          multi_match: {
            'query': this.inputField.search,
            'type': 'cross_fields',
            'fields': [ 'Description', 'Items.Agenda Title^3' ],
            'fuzziness': '2',
            'operator': 'and'
          }
        },
        'highlight': {
          'fields': {
            '*': {

            }
          }
        }
      }

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
      // console.log("parseQuery", this.advanced)

      var committeeDict = {
        'General Faculties Council': 'gfc',
        'Academic Planning Committee': 'apc',
        'Academic Standards Committee': 'asc',
        'Committee on Learning Environment': 'cle',
        'Campus Law Review Committee': 'clrc',
        'Executive Committee': 'exec',
        'Facilities Development Committee': 'fdc',
        'Undergraduate Awards and Scholarship Committee': 'uasc'
      }

      var committeeList = []
      var q = ''

      let committee = this.committees.replace('committee:', '').split(',')
      if (committee[0] !== '') {
        this.advancedFilters.committee = committee
        for (var key in committee) {
          let committeeName = committee[key]
          var value = committeeDict[committeeName]
          committeeList.push(value)
        }
      } else {
        this.advancedFilters.committee = []
        committeeList = ['gfc', 'apc', 'asc', 'fdc', 'exec', 'cle', 'clrc', 'uasc']
      }

      let people = this.people.replace('people:', '').split(',')
      if (people[0] !== '') {
        this.advancedFilters.people = people
      } else {
        this.advancedFilters.people = []
      }
      let peopleString = people.toString().replace(',', ' ')

      let dateStr = this.dateStart.replace('dateStart:', '')
      if (dateStr !== '') {
        this.advancedFilters.date_start = dateStr
      }

      dateStr = this.dateEnd.replace('dateEnd:', '')
      if (dateStr !== '') {
        this.advancedFilters.date_end = dateStr
      }

      let input = this.inputField.search + ' ' + peopleString
      if (input === ' ') {
        q = '*'
      } else {
        q = this.inputField.search + ' ' + peopleString
      }

      const advancedQuery = {

        'query': {
          'filtered': {
            'query': {
              'query_string': {
                'query': q,
                'fields': [ 'Items.Agenda Title^10',
                  'Attendees^3',
                  'Items.Presenter^3',
                  'Items.Proposed By^3',
                  'Description' ]
              }
            },
            'filter': {
              'bool': {
                'must': [
                  { 'terms': {
                    'Committee': committeeList }
                  },
                  { 'range': {
                    'Date': {
                      'gte': this.advancedFilters.date_start,
                      'lte': this.advancedFilters.date_end }}
                  }
                ]
              }
            }
          }
        },
        'highlight': {
          'fields': {
            '*': { }
          }
        }
      }

      axios.get('http://162.246.156.217:8080/meeting_minutes/modelresult/_search/?size=1000', {
        params: {
          source: JSON.stringify(advancedQuery),
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
</style>
