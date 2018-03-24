<template>
  <div class="top-left">
    <b-container fluid>
      <b-row align-v="center" align-h="center">
        <b-col cols="auto">
          <router-link to="/">
            <img src="./../assets/logoClearGov-XS.png" id="logo"/>
          </router-link>
        </b-col>
        <b-col>
          <input id="input-box" v-model="searchBoxText" v-on:keyup.enter="goToResults()"/>
        </b-col>
        <b-col>
            <b-button variant="outline-primary" size="lg" class="search" id="searchButton" v-on:click="goToResults()">Search</b-button>
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

      let peopleStr = 'people::'
      if (this.people != null) {
        isAdvancedSearch = true
        peopleStr = 'people:' + this.people + ':'
      }

      let advancedStr = 'advanced:false'
      if (isAdvancedSearch) {
        advancedStr = 'advanced:' + committeeStr + dateStr + peopleStr
      }

      this.$router.push({name: 'Result', params: { query: search, advanced: advancedStr }})
    },
    pillClicked: function (pill) {
      // console.log('Pill clicked')

      if (this.$route.name === 'Advanced Search') {
        if (pill.type === 'committee') {
          this.advancedForm.committee = null
        } else if (pill.type === 'date') {
          this.advancedForm.date = null
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
      this.addPills('committee', this.committee)
      this.addPills('date', this.date)
      this.addPills('people', this.people)
    }
  },
  computed: {
    committee () {
      return this.advancedForm.committee
    },
    date () {
      return this.advancedForm.date
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

    committee () {
      this.addPills('committee', this.committee)
    },
    date () {
      this.addPills('date', this.date)
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
.search{
  width: 100%
}
</style>
