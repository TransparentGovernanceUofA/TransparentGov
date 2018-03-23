<template>
  <div class="viewPDF">
    <top-left-search :previousInputField="inputField"></top-left-search>
    <b-container fluid>
      <b-row>
        <!--
        <b-col cols="6">
          <b-card header-tag="header" footer-tag="footer" class="md-elevation-3">

            <h6 v-if= searchresult slot="header" class="mb-0" v-for="title in searchresult.highlight.title">
              <span class="title" v-html="title"></span>
            </h6>
            <p class="card-text" v-for="desc in searchresult.highlight.description">
              <span class="desc" v-html="desc"></span>
            </p>

          </b-card>
        </b-col>
        <b-col cols="6">
        </b-col>
        -->
      </b-row>
    </b-container>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import axios from 'axios'

export default{
  props: {
    inputField: {
      type: Object,
      default: () => ({})
    },
    // file_id is accessing whats appended to the URL, ie /file/:file_id
    file_id: {
      type: String
    }
  },
  components: {
    TopLeftSearch
  },
  name: 'ElasticResults',
  data () {
    return {
      ElasticResult: {}
    }
  },
  created () {
    // console.log('Created----' + this.query)
    this.parseQuery()
    this.fetchData()
  },

  watch: {
    // query is accessing whats appended to the URL, ie /file/:file_id
    file_id: function () {
      // console.log('watch')
      this.parseQuery()
      this.fetchData()
    }
  },

  methods: {
    fetchData () {
      /*
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
        */
    },

    parseQuery () {
      //var queryArray = this.query.split(':')
      //this.inputField.search = queryArray[1]
      // console.log(this.inputField.search)
    }
  }
}
</script>

<style>
</style>