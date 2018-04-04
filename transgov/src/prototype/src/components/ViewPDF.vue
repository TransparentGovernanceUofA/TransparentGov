<template>
  <div class="viewPDF">
    <top-left-search :previousInputField="inputField"></top-left-search>
    <b-container fluid>
      <b-row>
        <b-col>
          <!-- <p>We recieved this file ID: {{file_id}}</p> -->
          <b-card class="mt-4 md-elevation-3" no-body>
            <div slot="header">
              <p>Show File: <input type="checkbox" v-model="show"></p>
              <p>
                Page: <input v-model.number="page" type="number" style="width: 5em" min="1" :max="numPages"> /{{numPages}}
              </p>
              <p>
                <button @click="rotate += 90" class="btn btn-primary">&#x27F3;</button>
                <button @click="rotate -= 90" class="btn btn-primary">&#x27F2;</button>
                <button @click="$refs.pdf.print()" class="btn btn-primary">Print</button>
              </p>
            </div>
            <div>
              <div v-if="loadedRatio > 0 && loadedRatio < 1" style="background-color: blue; color: white; text-align: center" :style="{ width: loadedRatio * 100 + '%' }">{{ Math.floor(loadedRatio * 100) }}%</div>
              <pdf v-if="show" ref="pdf" :src="file_id" :page="page" :rotate="rotate" @password="password" @progress="loadedRatio = $event" @error="error" @num-pages="numPages = $event"></pdf>
            </div>
          </b-card>
          
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
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
      show: false,
      pdfList: [],
      src:'',
      loadedRatio: 0,
      page: 1,
      numPages: 0,
      rotate: 0,
    }
  },
  created () {
    this.fetchData()
    pdfList.clear()
  },
  mounted () {
    this.show = true; // hack to attempt to ensure that the pdf loads
  },
  watch: {
    // query is accessing whats appended to the URL, ie /file/:file_id
    file_id: function () {
      this.fetchData()
    }
  },

  methods: {
    fetchData () {
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