<template>
  <div class="advancedSearch">
    <top-left-search :advancedForm="form"></top-left-search>
    <div id="AdvancedSearch">
      <b-container fluid >
        <b-row>
          <b-col cols=4>
            <!-- The inputs and options -->
            <b-card header="Search Options" class="mt-4 md-elevation-3">
              <b-form-group id="topic"
                          label="Topic"
                          label-for="exampleInput1">
                <b-form-select id="exampleInput1"
                            :options="topicOptions"
                            required
                            v-model="form.topic">
                </b-form-select>
              </b-form-group>

              <b-form-group id="committee"
                          label="Committee"
                          label-for="exampleInput2">
                <b-form-select id="exampleInput2"
                            :options="committeeOptions"
                            required
                            v-model="form.committee">
                </b-form-select>
              </b-form-group>

              <b-form-group id="date"
                          label="Date"
                          label-for="exampleInput3">
                <b-form-select id="exampleInput3"
                            :options="dateOptions"
                            required
                            v-model="form.date">
                </b-form-select>
              </b-form-group>

              <b-form-group id="text"
                          label="Text"
                          label-for="exampleInput4">
                <b-form-select id="exampleInput4"
                            :options="textOptions"
                            required
                            v-model="form.text">
                </b-form-select>
              </b-form-group>

              <b-form-group id="people"
                          label="People"
                          label-for="exampleInput5">
                <b-form-select id="exampleInput5"
                            :options="peopleOptions"
                            required
                            v-model="form.people">
                </b-form-select>
              </b-form-group>
            </b-card>
          </b-col>
          <b-col cols=8>
            <b-row>
              <!-- The output search string -->
              <b-col>
                <b-card header="Query" class="mt-4 md-elevation-3">
                  <b-form inline>
                    <b-button disabled class="mr-2">Search Query</b-button>
                    <!-- <b-form-input disabled></b-form-input> -->
                    <!-- <div v-for="(pill, index) in pills" :key="index">
                      <Pill v-on:pill_clicked="removePills(index)" :text="pill.name" :pill-style="pill.style" :pillable="pill.pillable">
                      </Pill>
                    </div> -->
                  </b-form>
                  <p class="card-text">Please use the options to the left to create your search. <br/>Note: This feature is not yet operational</p>
                </b-card>
              </b-col>
            </b-row>

            <b-row>
              <!-- The explanation box -->
              <b-col>
                <b-card header="Guide" class="mt-4 md-elevation-3" >
                  <p class="card-text">This area will help you discover the more advanced search capabilities of the system. The "Search Options" card houses several selections of known topics, people, organizations, etc. that the system knows about. By selecting any one of these fields the "Query" box will update to include the query that will be needed to search for those specific items.</p>
                </b-card>
              </b-col>
            </b-row>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import _ from 'lodash'

export default {
  props: {
    inputField: {
      type: Object,
      default: () => ({})
    }
  },
  components: {
    TopLeftSearch
  },
  methods: {
    //this method does not work, beause it grabs the result to quickly, debounce needed to delay the method
    // changedTopicInput () {
    //   console.log(this.form.topic)
    // }
    
  },
  data () {
    return {
      newSearchBoxText: '',
      advancedInputField: {
        search: ''
      },
      form: {
        topic: null,
        committee: null,
        date: null,
        text: null,
        people: null
      },
      topicOptions: [
        { value: null, text: '' },
        { value: 'USRI', text: 'USRI' },
        { value: 'Budget', text: 'Budget' },
        { value: 'Even more stoof', text: 'Even more stoof' }
      ],
      committeeOptions: [
        { value: null, text: '' },
        { value: '1 committee', text: '1 committee' },
        { value: '2 committee', text: '2 committee' },
        { value: '3 comimttee', text: '3 comimttee' }
      ],
      dateOptions: [
        { value: null, text: '' },
        { value: '1 idk', text: '1 idk' },
        { value: '2 what', text: '2 what' },
        { value: '3 we want for this', text: '3 we want for this' }
      ],
      textOptions: [
        { value: null, text: '' },
        { value: 'the', text: 'the' },
        { value: 'texts', text: 'texts' },
        { value: 'here', text: 'here' }
      ],
      peopleOptions: [
        { value: null, text: '' },
        { value: 'Eleni', text: 'Eleni' },
        { value: 'Barbosa', text: 'Barbosa' },
        { value: 'Diego', text: 'Diego' }
      ]
    }
  }
}
</script>

<style>

</style>
