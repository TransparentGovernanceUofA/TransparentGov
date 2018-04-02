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
          <div id="input-group-keeper">
            <b-input-group>
              <input id="input-box" v-model="searchBoxText" v-on:keyup.enter="goToResults()" class="form-control"/>
              <b-input-group-append>
                <b-button variant="outline-primary" size="sm" class="topLeftSearch" id="searchButton" v-on:click="goToResults()"><b>Search</b></b-button>
              </b-input-group-append>
            </b-input-group>
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-col v-for='(pill, index) in pills' :key='index' cols="auto">
          <Pill v-on:pill_clicked='pillClicked(pill, index)' :text='pill.name' :pill-style='pill.style' :pillable='pill.pillable'>
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
    pillClicked: function (pill, index) {
      console.log('Pill clicked')
      let new_arr = []
      if (this.$route.name === 'Advanced Search') {
        if (pill.type === 'committee') {
          // this.advancedForm.committee = null
          console.log("committee pill clicked")
          console.log(this.pills)
          for (let i = 0; i < this.pills.length; i++) {
            if (this.pills[i].type == "committee" && index != i){
              new_arr.push(this.pills[i].name)
            }    
          }
          console.log("changed", new_arr)
          this.advancedForm.committee = new_arr
        } else if (pill.type === 'date') {
          this.advancedForm.date = null
        } else {
          // this.advancedForm.people = null
          console.log("people pill clicked")
          console.log(this.pills)
          for (let i = 0; i < this.pills.length; i++) {
            if (this.pills[i].type == "people" && index != i){
              new_arr.push(this.pills[i].name)
            }    
          }
          console.log("changed", new_arr)
          this.advancedForm.people = new_arr
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
      console.log("in removePills", this.pills)
    },

    addPills: function (type, elements, dumb_fuck_arr) {

      let i
      for (i = this.pills.length - 1; i >= 0; i--) {
        let insert = true
        for (let j = 0; j < elements.length; j++) {
          console.log("Eelement", elements[j], "pill", this.pills[i].name, 'type', type)
          // checks if pill already exists
          if(elements[j] == this.pills[i].name && type==this.pills[i].type){
            insert = false
          }
          else if(type!==this.pills[i].type){
            insert = false
          }
        }
        // doesnt exist, remove it
        if(insert){
          console.log("remove")
          console.log("to remove", this.pills[i])
          this.removePills(i)
        }
      }

      // check if new pill needs to be added
      for (i = 0; i < elements.length; i++) {
        let insert = true
        for (let j = 0; j < dumb_fuck_arr.length; j++) {
          if(elements[i] == dumb_fuck_arr[j] && type==this.pills[i].type){
            insert = false
          }
        }
        if(insert){
          this.pills.push({
          id: this.pills.length,
          name: elements[i],
          type: type,
          style: 'primary',
          pillable: 'true'
        })
        }
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
      var dumb_fuck_arr = []
      for (let i = 0; i < this.pills.length; i++){
        dumb_fuck_arr.push(this.pills[i].name)
      }

      // for (let i = 0; i < this.committee.length; i++){
      //   this.addPills('committee', this.committee[i], dumb_fuck_arr)      
      // }
      this.addPills('committee', this.committee, dumb_fuck_arr)
    },
    date () {
      this.addPills('date', this.date)
    },
    people () {
      // this.addPills('people', this.people)
      var dumb_fuck_arr = []
      for (let i = 0; i < this.pills.length; i++){
        dumb_fuck_arr.push(this.pills[i].name)
      }

      // for (let i = 0; i < this.committee.length; i++){
      //   this.addPills('committee', this.committee[i], dumb_fuck_arr)      
      // }
      this.addPills('people', this.people, dumb_fuck_arr)
    }
  }
}

</script>

<style>
#input-group-keeper{
  /* This has a minimum width to prevent the search button from wrapping down below the search box on medium screens */
  /* The first value is the minimum size of the search box, the second value is the size of the search button */
  min-width: calc(200px + 65px);
}
#input-box{
  width: calc(100% - 100px);
  /* These stop the input box from getting too large or small on different displays */
  max-width: 500px;
  min-width: 200px;
  height: 35px;
}
#logo{
    width: 200px;
  }
</style>
