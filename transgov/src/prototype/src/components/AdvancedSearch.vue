<template>
  <div class="advancedSearch">
    <top-left-search :previousInputField="inputField" :advancedForm="form"></top-left-search>
    <!-- {{ form }} -->
    <div id="AdvancedSearch">
      <b-container fluid >
        <b-row>
          <b-col md=4 order="2" order-md="1">
            <!-- The inputs and options -->
            <b-card header="Search Options" class="mt-4 md-elevation-3">
              <div class="help-tip">
                <p>List of committees at the University of Alberta. <br>
                Multiple committees can be selected by pressing "Ctrl" and clicking on committees</p>
              </div>
              <b-form-group id="committee"
                          label="Committee"
                          label-for="exampleInput2">
                <b-form-select id="exampleInput2"
                            multiple
                            :select-size="3"
                            :options="committeeOptions"
                            required
                            v-model="form.committee">
                </b-form-select>
              </b-form-group>
              <div class="help-tip">
                <p>Various members that take part in Governance discussions. <br>
                Multiple members can be selected by pressing "Ctrl" and clicking on names</p>
              </div>
              <b-form-group id="people"
                          label="People"
                          label-for="exampleInput5">
                <b-form-select id="exampleInput5"
                            multiple
                            :select-size="3"
                            :options="peopleOptions"
                            required
                            v-model="form.people">
                </b-form-select>
              </b-form-group>
              <b-form-group id="date">
                <b-row>
                  <b-col>
                    <p> Start: </p>
                    <date-picker v-model="date_start" :config="config_date_start"></date-picker>
                  </b-col>
                  <b-col>
                    <div id="time-help" class="help-tip">
                      <p>Date picker, allows searching in a range of dates.</p>
                    </div>
                    <p> End: </p>
                    <date-picker v-model="date_end":config="config_date_end"></date-picker>
                  </b-col>
                </b-row>
              </b-form-group>
            </b-card>
          </b-col>
          <b-col md=8 order="1" order-md="2">
          <!-- The explanation box -->
            <b-card header="Guide" class="mt-4 md-elevation-3" >
              <p class="card-text">This area will help you discover the more advanced search capabilities of the system. The "Search Options" card houses several selections of known topics, people, organizations, etc. that the system knows about. By selecting any one of these fields the "Query" box will update to include the query that will be needed to search for those specific items.</p>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import axios from 'axios'

export default {
  props: {
    inputField: {
      type: Object,
      default: () => ({})
    },
    query: {
      type: String
    },
    advanced: {
      type: String
    }
  },
  components: {
    TopLeftSearch,
  },
  created () {
    this.parseQuery()
    this.fetchCommittee()
    this.fetchPeople()
  },
  methods: {
    // this method does not work, beause it grabs the result to quickly, debounce needed to delay the method
    // changedTopicInput () {
    //   console.log(this.form.topic)
    // }

    parseQuery () {
      var queryArray = this.query.split(':')
      this.inputField.search = queryArray[1]

      var advancedArray = this.advanced.split(':')
      if (advancedArray[1] !== 'false') {
        this.form.committee = advancedArray[2]
        if (this.form.committee === '') {
          this.form.committee = null
        }

        // this.form.date = advancedArray[4]
        // if (this.form.date === '') {
        //   this.form.date = null
        // }

        this.form.people = advancedArray[6]
        console.log("form", this.form.people)
        if (this.form.people === '') {
          this.form.people = null
        }
      }
      // console.log(this.form)
      // console.log(this.inputField.search)
    },
    fetchCommittee () {
      axios.get('http://162.246.156.217:8080/excel/committees/_search?pretty')
        .then((resp) => {
          const committee_resp = resp.data.hits.hits
          for(var i = 0; i < committee_resp.length; i++) {
            this.committeeOptions.push(committee_resp[i]._source.Committee)
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    fetchPeople () {
      axios.get('http://162.246.156.217:8080/excel/members/_search?size=1200&q=*:*')
        .then((resp) => {
          const people_resp = resp.data.hits.hits
          for(var i = 0; i < people_resp.length; i++) {
            this.peopleOptions.push(people_resp[i]._source['Contact Name'])
          }
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  data () {
    return {
      newSearchBoxText: '',
      advancedInputField: {
        search: ''
      },
      form: {
        committee: [],
        people: []
      },
      committeeOptions: [
        // { value: null, text: '' }
      ],
      peopleOptions: [
        // { value: null, text: '' },
      ],
      date_start: null,
      config_date_start: {
        format: 'DD/MM/YYYY',
        useCurrent: false,
        showClear: true,
        showClose: true,
        maxDate: new Date()
      },
      date_end: new Date(),
      config_date_end: {
        format: 'DD/MM/YYYY',
        useCurrent: false,
        showClear: true,
        showClose: true,
        maxDate: new Date()
      }
    }
  }
}
</script>

<style>

#time-help{
  left: 86.5%;

}
</style>
