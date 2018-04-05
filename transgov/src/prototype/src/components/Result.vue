<template>
  <div class="results">
    <top-left-search :previousInputField="inputField" :advancedForm="advancedFilters"></top-left-search>
    <b-container fluid>
      <b-row v-show="searching == true" id="loading_anim" align-h="center" class="mt-5 mb-5">
        <b-col cols="auto">
          <div class="la-ball-atom la-dark la-3x" >
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
        </b-col>
      </b-row>
      <b-row v-show="searching == true" align-h="center">
        <b-col cols="auto">
          Asking the government...
        </b-col>
      </b-row>

      <b-row v-show="empty == false">
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
      <b-row class = "mt-2">
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
      <b-row align-h="center" class="mt-2">
        <b-col v-show="searching == false && empty == false" cols="auto">
          End of Search Results
        </b-col>
        <b-col v-show="searching == false && empty == true" cols="auto">
          <p>No results containing all your search terms were found.<br/>

          Your search: <strong>{{inputField.search}}</strong> - did not match any documents.<br/>
          <br/>
          <strong>Suggestions:</strong><br/>

          - Make sure that all words are spelled correctly.<br/>
          - Try different keywords.<br/>
          - Try more general keywords.</p>
        </b-col>
      </b-row>
      <div class="spacer">
        <!-- The only purpose of this div is to give scroll space to allow the user to scroll to the very last card freely -->
      </div>
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
      },
      searching: true,
      empty: true
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
      // console.log('advanced Changed')
      this.parseQuery()
      // this.fetchData()
    }
  },

  methods: {
    fetchData () {
      this.searching = true
      // basic query for es; for now searching 'exact term' over all fields
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
          // Update the display, hide the loading animation, reveal the timeline, place an indicator at the end of the search results
          if (this.ElasticResult.length == 0){
            this.empty = true
          } else {
            this.empty = false
          }
          this.searching = false
        })
        .catch((err) => {
          console.log(err)
        })
    },
    parseQuery () {
      this.searching = true
      let queryArray = this.query.replace('search:', '')
      this.inputField.search = queryArray

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
          if (this.ElasticResult.length == 0){
            this.empty = true
          } else {
            this.empty = false
          }
          this.searching = false
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}

</script>

<style>
  .spacer{
    height: 99vh;
  }
  /*!
   * Load Awesome v1.1.0 (http://github.danielcardoso.net/load-awesome/)
   * Copyright 2015 Daniel Cardoso <@DanielCardoso>
   * Licensed under MIT
   */
  .la-ball-atom,
  .la-ball-atom > div {
      position: relative;
      -webkit-box-sizing: border-box;
         -moz-box-sizing: border-box;
              box-sizing: border-box;
  }
  .la-ball-atom {
      display: block;
      font-size: 0;
      color: #fff;
  }
  .la-ball-atom.la-dark {
      color: #333;
  }
  .la-ball-atom > div {
      display: inline-block;
      float: none;
      background-color: currentColor;
      border: 0 solid currentColor;
  }
  .la-ball-atom {
      width: 32px;
      height: 32px;
  }
  .la-ball-atom > div:nth-child(1) {
      position: absolute;
      top: 50%;
      left: 50%;
      z-index: 1;
      width: 60%;
      height: 60%;
      background: #00887a;
      border-radius: 100%;
      -webkit-transform: translate(-50%, -50%);
         -moz-transform: translate(-50%, -50%);
          -ms-transform: translate(-50%, -50%);
           -o-transform: translate(-50%, -50%);
              transform: translate(-50%, -50%);
      -webkit-animation: ball-atom-shrink 4.5s infinite linear;
         -moz-animation: ball-atom-shrink 4.5s infinite linear;
           -o-animation: ball-atom-shrink 4.5s infinite linear;
              animation: ball-atom-shrink 4.5s infinite linear;
  }
  .la-ball-atom > div:not(:nth-child(1)) {
      position: absolute;
      left: 0;
      z-index: 0;
      width: 100%;
      height: 100%;
      background: none;
      -webkit-animation: ball-atom-zindex 3s 0s infinite steps(2, end);
         -moz-animation: ball-atom-zindex 3s 0s infinite steps(2, end);
           -o-animation: ball-atom-zindex 3s 0s infinite steps(2, end);
              animation: ball-atom-zindex 3s 0s infinite steps(2, end);
  }
  .la-ball-atom > div:not(:nth-child(1)):before {
      position: absolute;
      top: 0;
      left: 0;
      width: 10px;
      height: 10px;
      margin-top: -5px;
      margin-left: -5px;
      content: "";
      background: currentColor;
      border-radius: 50%;
      opacity: .75;
      -webkit-animation: ball-atom-position 3s 0s infinite ease, ball-atom-size 3s 0s infinite ease;
         -moz-animation: ball-atom-position 3s 0s infinite ease, ball-atom-size 3s 0s infinite ease;
           -o-animation: ball-atom-position 3s 0s infinite ease, ball-atom-size 3s 0s infinite ease;
              animation: ball-atom-position 3s 0s infinite ease, ball-atom-size 3s 0s infinite ease;
  }
  .la-ball-atom > div:nth-child(2) {
      -webkit-animation-delay: 1.5s;
         -moz-animation-delay: 1.5s;
           -o-animation-delay: 1.5s;
              animation-delay: 1.5s;
  }
  .la-ball-atom > div:nth-child(2):before {
      -webkit-animation-delay: 0s, -2.25s;
         -moz-animation-delay: 0s, -2.25s;
           -o-animation-delay: 0s, -2.25s;
              animation-delay: 0s, -2.25s;
  }
  .la-ball-atom > div:nth-child(3) {
      -webkit-transform: rotate(120deg);
         -moz-transform: rotate(120deg);
          -ms-transform: rotate(120deg);
           -o-transform: rotate(120deg);
              transform: rotate(120deg);
      -webkit-animation-delay: -.5s;
         -moz-animation-delay: -.5s;
           -o-animation-delay: -.5s;
              animation-delay: -.5s;
  }
  .la-ball-atom > div:nth-child(3):before {
      -webkit-animation-delay: -2s, -1.5s;
         -moz-animation-delay: -2s, -1.5s;
           -o-animation-delay: -2s, -1.5s;
              animation-delay: -2s, -1.5s;
  }
  .la-ball-atom > div:nth-child(4) {
      -webkit-transform: rotate(240deg);
         -moz-transform: rotate(240deg);
          -ms-transform: rotate(240deg);
           -o-transform: rotate(240deg);
              transform: rotate(240deg);
      -webkit-animation-delay: .5s;
         -moz-animation-delay: .5s;
           -o-animation-delay: .5s;
              animation-delay: .5s;
  }
  .la-ball-atom > div:nth-child(4):before {
      -webkit-animation-delay: -1s, -.25s;
         -moz-animation-delay: -1s, -.25s;
           -o-animation-delay: -1s, -.25s;
              animation-delay: -1s, -.25s;
  }
  .la-ball-atom.la-sm {
      width: 16px;
      height: 16px;
  }
  .la-ball-atom.la-sm > div:not(:nth-child(1)):before {
      width: 4px;
      height: 4px;
      margin-top: -2px;
      margin-left: -2px;
  }
  .la-ball-atom.la-2x {
      width: 64px;
      height: 64px;
  }
  .la-ball-atom.la-2x > div:not(:nth-child(1)):before {
      width: 20px;
      height: 20px;
      margin-top: -10px;
      margin-left: -10px;
  }
  .la-ball-atom.la-3x {
      width: 96px;
      height: 96px;
  }
  .la-ball-atom.la-3x > div:not(:nth-child(1)):before {
      width: 30px;
      height: 30px;
      margin-top: -15px;
      margin-left: -15px;
  }
  /*
   * Animations
   */
  @-webkit-keyframes ball-atom-position {
      50% {
          top: 100%;
          left: 100%;
      }
  }
  @-moz-keyframes ball-atom-position {
      50% {
          top: 100%;
          left: 100%;
      }
  }
  @-o-keyframes ball-atom-position {
      50% {
          top: 100%;
          left: 100%;
      }
  }
  @keyframes ball-atom-position {
      50% {
          top: 100%;
          left: 100%;
      }
  }
  @-webkit-keyframes ball-atom-size {
      50% {
          -webkit-transform: scale(.5, .5);
                  transform: scale(.5, .5);
      }
  }
  @-moz-keyframes ball-atom-size {
      50% {
          -moz-transform: scale(.5, .5);
               transform: scale(.5, .5);
      }
  }
  @-o-keyframes ball-atom-size {
      50% {
          -o-transform: scale(.5, .5);
             transform: scale(.5, .5);
      }
  }
  @keyframes ball-atom-size {
      50% {
          -webkit-transform: scale(.5, .5);
             -moz-transform: scale(.5, .5);
               -o-transform: scale(.5, .5);
                  transform: scale(.5, .5);
      }
  }
  @-webkit-keyframes ball-atom-zindex {
      50% {
          z-index: 10;
      }
  }
  @-moz-keyframes ball-atom-zindex {
      50% {
          z-index: 10;
      }
  }
  @-o-keyframes ball-atom-zindex {
      50% {
          z-index: 10;
      }
  }
  @keyframes ball-atom-zindex {
      50% {
          z-index: 10;
      }
  }
  @-webkit-keyframes ball-atom-shrink {
      50% {
          -webkit-transform: translate(-50%, -50%) scale(.8, .8);
                  transform: translate(-50%, -50%) scale(.8, .8);
      }
  }
  @-moz-keyframes ball-atom-shrink {
      50% {
          -moz-transform: translate(-50%, -50%) scale(.8, .8);
               transform: translate(-50%, -50%) scale(.8, .8);
      }
  }
  @-o-keyframes ball-atom-shrink {
      50% {
          -o-transform: translate(-50%, -50%) scale(.8, .8);
             transform: translate(-50%, -50%) scale(.8, .8);
      }
  }
  @keyframes ball-atom-shrink {
      50% {
          -webkit-transform: translate(-50%, -50%) scale(.8, .8);
             -moz-transform: translate(-50%, -50%) scale(.8, .8);
               -o-transform: translate(-50%, -50%) scale(.8, .8);
                  transform: translate(-50%, -50%) scale(.8, .8);
      }
  }
</style>
