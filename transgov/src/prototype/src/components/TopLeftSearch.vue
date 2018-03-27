<template>
  <div class="top-left">
    <b-container fluid>
      <b-row align-v="center" align-h="center">
        <b-col cols="auto">
          <router-link to="/">
            <img src="./../assets/logoOpenGov2-3.svg" id="logo" class="m-2"/>
          </router-link>
          
        </b-col>
        <b-col>
          <input id="input-box" v-model="searchBoxText" v-on:keyup.enter="goToResults()"/>
          <!-- <input id="input-box" v-if = "truthy" v-model="searchBoxText" v-on:keyup.enter="goToResults()"/> -->
          <!-- <input id="input-box" disabled v-model="searchBoxText" v-on:keyup.enter="goToResults()"/> -->
          <!-- <input id="input-box" v-else disabled v-model="searchBoxText" v-on:keyup.enter="goToResults()"/> -->
        </b-col>
      </b-row>
      <b-row>
        <b-col v-for='(pill, index) in pills' :key='index' cols="auto">
          <Pill v-on:pill_clicked='pillClicked(pill)' :text='pill.name' :pill-style='pill.style' :pillable='pill.pillable'>
          </Pill>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Pill from './Pill.vue'
export default {
  data: function () {
    return {
      pills: [],
      searchBoxText: '',
      inputField: {
        search: 'search:'
      }
    }
  },
  components: {
    Pill
  },
  // the searchBox component will pass this prop for the search term
  props: ['previousInputField', 'advancedForm'],
  // props: ['previousInputField'],
  created () {
    // console.log('created')
    // check if the prop has been passed
    if (this.previousInputField != null) {
      // console.log('not null')
      // use the passed prop to set the default input box text
      this.inputField = this.previousInputField
      this.searchBoxText = this.inputField.search
    }

    this.loadPills()
    // this.searchBoxText = this.$parent.inputField.search
  },
  methods: {
    goToResults () {
      // console.log('goToResults')
      // console.log(this.pills)

      this.inputField.search = 'search:' + this.searchBoxText
      let search = this.inputField.search
      // console.log(search)

      let isAdvancedSearch = false

      let topicStr = 'topic::'
      if (this.topic != null) {
        isAdvancedSearch = true
        topicStr = 'topic:' + this.topic + ':'
      }

      let committeeStr = 'committee::'
      if (this.committee != null) {
        isAdvancedSearch = true
        committeeStr = 'committee:' + this.committee + ':'
      }

      let dateStr = 'date::'
      if (this.date != null) {
        isAdvancedSearch = true
        dateStr = 'date:' + this.date + ':'
      }

      let textStr = 'text::'
      if (this.text != null) {
        isAdvancedSearch = true
        textStr = 'text:' + this.text + ':'
      }

      let peopleStr = 'people::'
      if (this.people != null) {
        isAdvancedSearch = true
        peopleStr = 'people:' + this.people + ':'
      }

      let advancedStr = 'advanced:false'
      if (isAdvancedSearch) {
        advancedStr = 'advanced:' + topicStr + committeeStr + dateStr + textStr + peopleStr
      }

      this.$router.push({name: 'Result', params: { query: search, advanced: advancedStr }})
    },
    pillClicked: function (pill) {
      // console.log('Pill clicked')

      if (this.$route.name === 'Advanced Search') {
        if (pill.type === 'topic') {
          this.advancedForm.topic = null
        } else if (pill.type === 'committee') {
          this.advancedForm.committee = null
        } else if (pill.type === 'date') {
          this.advancedForm.date = null
        } else if (pill.type === 'text') {
          this.advancedForm.text = null
        } else {
          this.advancedForm.people = null
        }
      } else if (this.$route.name === 'Result') {
        // console.log('Pill clicked from the results page')
        let query = this.$route.params.query
        let advanced = this.$route.params.advanced

        this.$router.push({name: 'Advanced Search', params: { query: query, advanced: advanced }})
      }
    },
    removePills: function (id) {
      this.pills.splice(id, 1)
    },

    addPills: function (type, element) {
      // console.log('add Pills')
      // if pill is changed to null, remove the cooresponding pill
      if (element == null) {
        for (let i = 0; i < this.pills.length; i++) {
          if (this.pills[i].type === type) {
            this.removePills(i)
          }
        }
      } else {
        for (let i = 0; i < this.pills.length; i++) {
          // remove respective pill if its value is changed but type remained the same
          if (this.pills[i].type === type && this.pills[i].name !== element) {
            this.removePills(i)
          }
        }
        // add pills
        this.pills.push({
          id: this.pills.length,
          name: element,
          type: type,
          style: 'primary',
          pillable: 'true'
        })
      }
    },
    loadPills: function () {
      this.addPills('topic', this.topic)
      this.addPills('committee', this.committee)
      this.addPills('date', this.date)
      this.addPills('text', this.text)
      this.addPills('people', this.people)
    }
  },
  computed: {
    topic () {
      return this.advancedForm.topic
    },
    committee () {
      return this.advancedForm.committee
    },
    date () {
      return this.advancedForm.date
    },
    text () {
      return this.advancedForm.text
    },
    people () {
      return this.advancedForm.people
    }
  },
  // recognize when change occurs in advancedInput and update the text box
  watch: {
    // advancedInputField(){
    //   this.truthy = false
    //   this.searchBoxText = ''
    //   for(var i=0; i < this.advancedInputField.length; i++){
    //     this.searchBoxText += this.advancedInputField[i].name + ' '
    //   }
    // }

    topic () {
      // console.log('topic changed')
      this.addPills('topic', this.topic)
    },
    committee () {
      this.addPills('committee', this.committee)
    },
    date () {
      this.addPills('date', this.date)
    },
    text () {
      this.addPills('text', this.text)
    },
    people () {
      this.addPills('people', this.people)
    }
  }
}

</script>

<style>
  #input-box{
    width: 100%;

    /* These stop the input box from getting too large or small on different displays */
    max-width: 500px; 
    min-width: 200px;

    height: 35px;
  }
  #logo{
    width: 200px;
  }
</style>
