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
                            :options="committeeOptions"
                            required
                            v-model="tempCommitteeSelect">
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
                            :options="peopleOptions"
                            required
                            v-model="tempPeopleSelect">
                </b-form-select>
              </b-form-group>
              <b-form-group id="date">
                <b-row>
                  <b-col>
                    <p> Start: </p>
                    <date-picker v-model="form.date_start" :config="config_date_start"></date-picker>
                  </b-col>
                  <b-col>
                    <div id="time-help" class="help-tip">
                      <p>Date picker, allows searching in a range of dates.</p>
                    </div>
                    <p> End: </p>
                    <date-picker v-model="form.date_end":config="config_date_end"></date-picker>
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
      let queryArray = this.query.replace('search:', '')
      this.inputField.search = queryArray
      // console.log("parseQuery", this.advanced)

      let committee = this.committees.replace('committee:', '').split(',')
      if (committee[0] !== "") {
        this.form.committee = committee
      } else {
        this.form.committee = []
      }


      let people = this.people.replace('people:', '').split(',')
      if (people[0] !== "") {
        this.form.people = people
      } else {
        this.form.people = []
      }

      let dateStr = this.dateStart.replace('dateStart:', '')
      if (dateStr !== '') {
        this.form.date_start = dateStr
      }

      dateStr = this.dateEnd.replace('dateEnd:', '')
      if (dateStr !== '') {
        this.form.date_end = dateStr
      }


    },
    fetchCommittee () {
      axios.get('http://162.246.156.217:8080/excel/committees/_search?pretty')
        .then((resp) => {
          const committee_resp = resp.data.hits.hits
          const committee_search = resp.data.hits.hits
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
      tempCommitteeSelect: null,
      tempPeopleSelect: null,
      form: {
        committee: [],
        people: [],
        date_end: null,
        date_start: null
      },
      committeeOptions: [
        // { value: null, text: '' }
      ],
      peopleOptions: [
        // { value: null, text: '' },
      ],
      config_date_start: {
        format: 'YYYY-MM-DD',
        useCurrent: true,
        showClear: true,
        showClose: true,
        maxDate: new Date()
      },
      config_date_end: {
        format: 'YYYY-MM-DD',
        useCurrent: true,
        showClear: true,
        showClose: true,
        maxDate: new Date()
      }
    }
  },
  watch: {
    tempCommitteeSelect: function (val) {
      let found = false
      for (var i = this.form.committee.length - 1; i >= 0; i--) {
        if (this.form.committee[i] === val) {
          found = true
          break
        }
      }

      if (!found) {
        this.form.committee.push(val)
      }

    },
    tempPeopleSelect: function (val) {
      let found = false
      for (var i = this.form.people.length - 1; i >= 0; i--) {
        // console.log(this.form.people[i], val)
        if (this.form.people[i] === val) {
          // console.log('Same')
          found = true
          break
        }
      }

      if (!found) {
        this.form.people.push(val)
      }

      // console.log("___________")
    }
  }
}
</script>

<style>

#time-help{
  left: 86.5%;

}
</style>
