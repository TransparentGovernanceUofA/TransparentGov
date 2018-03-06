<template>
  <div class="advancedSearch">
    <top-left-search></top-left-search>
      <div id="AdvancedSearch">
        <!-- <center>
            ADVANCED COMPONENT STUFF HERE
        </center> -->
        <div id="topics" class="searchItem">
          <div class="title">
            <p>Topics</p>
          </div>
          <div class="select">
            <b-form-select v-model="selected" :options="topicOptions" class="mb-3" />
          </div>
        </div>

        <div id="committee" class="searchItem">
          <div class="title">
            <p>Committee</p>
          </div>
          <div class="select">
            <b-form-select v-model="selected" :options="committeeOptions" class="mb-3" />
          </div>
        </div>

        <div id="date" class="searchItem">
          <div class="title">
            <p>Date</p>
          </div>
          <div class="select">
            <b-form-select v-model="selected" :options="dateOptions" class="mb-3" />
          </div>
        </div>

        <div id="text" class="searchItem">
          <div class="title">
            <p>Text</p>
          </div>
          <div class="select">
            <b-form-select v-model="selected" :options="textOptions" class="mb-3" />
          </div>
        </div>

        <div id="people" class="searchItem">
          <div class="title">
            <p>People</p>
          </div>
          <div class="select">
            <b-form-select v-model="selected" :options="peopleOptions" class="mb-3" />
          </div>
        </div>

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
      selected: null,
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
