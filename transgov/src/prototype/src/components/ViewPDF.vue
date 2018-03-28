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
        <b-col>
          <p>We recieved this file ID: {{file_id}}</p>
          <div>
            <input type="checkbox" v-model="show">
            <select v-model="src" style="width: 30em">
              <option v-for="item in pdfList" :value="item" v-text="item"></option>
            </select>
            <input v-model.number="page" type="number" style="width: 5em"> /{{numPages}}
            <button @click="rotate += 90">&#x27F3;</button>
            <button @click="rotate -= 90">&#x27F2;</button>
            <button @click="$refs.pdf.print()">print</button>
            <div style="width: 50%">
              <div v-if="loadedRatio > 0 && loadedRatio < 1" style="background-color: green; color: white; text-align: center" :style="{ width: loadedRatio * 100 + '%' }">{{ Math.floor(loadedRatio * 100) }}%</div>
              <pdf v-if="show" ref="pdf" style="border: 1px solid red" :src="file_id" :page="page" :rotate="rotate" @password="password" @progress="loadedRatio = $event" @error="error" @num-pages="numPages = $event"></pdf>
            </div>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import axios from 'axios'
import pdf from 'vue-pdf'

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
    TopLeftSearch,
    pdf
  },
  name: 'ElasticResults',
  data () {
    return {
      ElasticResult: {},
      show: true,
      pdfList: [],
      src:'',
      loadedRatio: 0,
      page: 1,
      numPages: 0,
      rotate: 0,
    }
  },
  created () {
    // console.log('Created----' + this.query)
    this.parseQuery()
    this.fetchData()
    pdfList.clear()
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
    },
    password: function(updatePassword, reason) {
      updatePassword(prompt('password is "test"'));
    },
    error: function(err) {
      console.log(err);
    }
  }
}
</script>

<style>
</style>