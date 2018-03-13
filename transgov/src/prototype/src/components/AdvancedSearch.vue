<template>
  <div class="advancedSearch">
    <top-left-search></top-left-search>
    <div id="AdvancedSearch">
      <b-container fluid >
        <b-row>
          <b-col cols=4>
            <!-- The inputs and options -->
            <b-card header="Search Options" class="mt-4 md-elevation-3">
              <b-form-select id="exampleInput1"
                            :options="topicOptions"
                            required
                            v-model="form.topic"
                            @change=changedTopicInput()>
                </b-form-select>
              </b-form-group>

              <b-form-group id="committee"
                          label="Committee"
                          label-for="exampleInput2">
                <b-form-select id="exampleInput2"
                            :options="committeeOptions"
                            required
                            v-model="form.committee"
                            @change=changedCommitteeInput()>
                </b-form-select>
              </b-form-group>

              <b-form-group id="date"
                          label="Date"
                          label-for="exampleInput3">
                <b-form-select id="exampleInput3"
                            :options="dateOptions"
                            required
                            v-model="form.date"
                            @change=changedDateInput()>
                </b-form-select>
              </b-form-group>

              <b-form-group id="text"
                          label="Text"
                          label-for="exampleInput4">
                <b-form-select id="exampleInput4"
                            :options="textOptions"
                            required
                            v-model="form.text"
                            @change=changedTextInput()>
                </b-form-select>
              </b-form-group>

              <b-form-group id="people"
                          label="People"
                          label-for="exampleInput5">
                <b-form-select id="exampleInput5"
                            :options="peopleOptions"
                            required
                            v-model="form.people"
                            @change=changedPeopleInput()>
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
                    <b-form-input v-model="SearchBoxText"></b-form-input>
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
    // changedTopicInput () {
    //   console.log(this.form.topic)
    // }
    changedTopicInput: _.debounce(function(){
        console.log(this.form.topic)
        console.log("topic changed")
        this.SearchBoxText += this.form.topic + " "
    }, 10),
    changedCommitteeInput: _.debounce(function(){
        console.log(this.form.topic)
        console.log("topic changed")
        this.SearchBoxText += this.form.committee + " "
    }, 10),
    changedDateInput: _.debounce(function(){
        console.log(this.form.topic)
        console.log("topic changed")
        this.SearchBoxText += this.form.date + " "
    }, 10),
    changedTextInput: _.debounce(function(){
        console.log(this.form.topic)
        console.log("topic changed")
        this.SearchBoxText += this.form.text + " "
    }, 10),
    changedPeopleInput: _.debounce(function(){
        console.log(this.form.topic)
        console.log("topic changed")
        this.SearchBoxText += this.form.people + " "
    }, 10)
  },
  data () {
    return {
      SearchBoxText: "",
      newTopic: "",
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
        { value: 'Stoof', text: 'Stoof' },
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
        { value: 'some', text: 'some' },
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
