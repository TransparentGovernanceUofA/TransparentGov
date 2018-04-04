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
      console.log('advanced Changed')
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
      // console.log("parseQuery", this.advanced)

      let committee = this.committees.replace('committee:', '').split(',')
      if (committee[0] !== "") {
        this.advancedFilters.committee = committee
      } else {
        this.advancedFilters.committee = []
      }
      // console.log("parseQuery", this.advancedFilters.committee)

      // console.log('|' + this.people + '|')
      let people = this.people.replace('people:', '').split(',')
      if (people[0] !== "") {
        this.advancedFilters.people = people
      } else {
        this.advancedFilters.people = []
      }
      // console.log('People', people)
      // console.log("parseQuery", this.advancedFilters.people)


      let dateStr = this.dateStart.replace('dateStart:', '')
      if (dateStr !== '') {
        this.advancedFilters.date_start = dateStr
      }
      // console.log("parseQuery", this.advancedFilters.date_start)

      dateStr = this.dateEnd.replace('dateEnd:', '')
      if (dateStr !== '') {
        this.advancedFilters.date_end = dateStr
      }
      // console.log("parseQuery", this.advancedFilters.date_end)

      





      // var advancedArray = this.advanced.split(':')
      // console.log('advancedArray', advancedArray)
      // if (advancedArray[1] !== 'false') { // if there are advanced terms
      //   let split = advancedArray[2].split(",")
      //   if(split[0] == ""){
      //     //do nothing
      //   }
      //   else{
      //     this.advancedFilters.committee = advancedArray[2].split(",")
      //   }

      //   let date_start = advancedArray[4]
      //   if (date_start === "") {
      //     this.advancedFilters.date_start = null
      //   } else {
      //     this.advancedFilters.date_start = new Date(date_start)
      //   }

      //   let date_end = advancedArray[6]
      //   if (date_end === "") {
      //     this.advancedFilters.date_end = null
      //   } else {
      //     this.advancedFilters.date_end = new Date(date_end)
      //   }

      //   // this.advancedFilters.committee = advancedArray[2].split(",")
      //   split = advancedArray[8].split(",")
      //   if(split[0] == ""){
      //     //do nothing
      //   }
      //   else{
      //     this.advancedFilters.people = advancedArray[8].split(",")
      //   }
      //   console.log(advancedFilters.people)
      //   console.log("advanced committee in result", this.advancedFilters)
        
      // }
      // console.log(this.advancedFilters)
      // console.log(this.inputField.search)
    }
  }
}

</script>

<style>
</style>
