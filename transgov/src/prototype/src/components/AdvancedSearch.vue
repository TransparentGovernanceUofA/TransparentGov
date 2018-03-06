<template>
  <div class="advancedSearch">
    <top-left-search></top-left-search>
      <div id="AdvancedSearch">
        <!-- <center>
            ADVANCED COMPONENT STUFF HERE
        </center> -->

        <b-form-group id="topics"
                    label="Topics"
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

  data () {
    return {
      form: {
        topic: null,
        committee: null,
        date: null,
        text: null,
        people: null
      },
      topicOptions: [
        { value: null, text: '' },
        { value: 'a', text: 'USRI' },
        { value: 'b', text: 'Stoof' },
        { value: {'C': '3PO'}, text: 'Even more stoof' }
      ],
      committeeOptions: [
        { value: null, text: '' },
        { value: 'a', text: '1 committee' },
        { value: 'b', text: '2 committee' },
        { value: {'C': '3PO'}, text: '3 comimttee' }
      ],
      dateOptions: [
        { value: null, text: '' },
        { value: 'a', text: '1 idk' },
        { value: 'b', text: '2 what' },
        { value: {'C': '3PO'}, text: '3 we want for this' }
      ],
      textOptions: [
        { value: null, text: '' },
        { value: 'a', text: 'some' },
        { value: 'b', text: 'texts' },
        { value: {'C': '3PO'}, text: 'here' }
      ],
      peopleOptions: [
        { value: null, text: '' },
        { value: 'a', text: 'Eleni' },
        { value: 'b', text: 'Barbosa' },
        { value: {'C': '3PO'}, text: 'Diego' }
      ]
    }
  }
}
</script>

<style>

</style>
