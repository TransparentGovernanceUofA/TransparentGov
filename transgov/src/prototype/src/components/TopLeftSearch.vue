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
      // console.log('Pill clicked', pill.type)
      let new_arr = []
      if (this.$route.name === 'Advanced Search') {
        if (pill.type === 'committee') {
          // this.advancedForm.committee = null
          // update advancedForm.committee with only pills that were not clicked on
          for (let i = 0; i < this.pills.length; i++) {
            if (this.pills[i].type == "committee" && index != i){
              new_arr.push(this.pills[i].name)
            }    
          }
          this.advancedForm.committee = new_arr
        } 
        // else if (pill.type === 'date') {
        //   this.advancedForm.date = null
        // } 
        else {
          // this.advancedForm.people = null
          // update advancedForm.committee with only pills that were not clicked on
          for (let i = 0; i < this.pills.length; i++) {
            if (this.pills[i].type == "people" && index != i){
              new_arr.push(this.pills[i].name)
            }    
          }
          this.advancedForm.people = new_arr
        }
      } 
      else if (this.$route.name === 'Result') {
        // console.log('Pill clicked from the results page')
        let query = this.$route.params.query
        let advanced = this.$route.params.advanced
        console.log("back to advanced search", "query:", query, "advanced", advanced)
        this.$router.push({name: 'Advanced Search', params: { query: query, advanced: advanced }})
      }
    },
    removePills: function (id) {
      this.pills.splice(id, 1)
    },

    addPills: function (type, elements, original) {
      // console.log("add pills function called", this.pills.length, this.pills)
      let i
      for (i = this.pills.length - 1; i >= 0; i--) {
        let insert = true
        for (var j = 0; j < elements.length; j++) {
          console.log("Eelement", elements[j], "pill", this.pills[i].name, 'type', type)
          // checks if pill already exists
          if(elements[j] == this.pills[i].name && type==this.pills[i].type){
            console.log("pill and input exist")
            insert = false
            break
          }
        }
        // doesnt exist, remove it
        if(insert && this.pills[i].type == type){
          this.removePills(i)
        }
      }

      // check if new pill needs to be added
      for (i = 0; i < elements.length; i++) {
        let insert = true
        for (let j = 0; j < original.length; j++) {
          if(elements[i] == original[j]){

            insert = false
          }
        }
        if(insert){
          console.log("insert new pill", elements[i])
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
      var original = []
      // typeof===string means its coming from result, else coming from advancedSearch
      if(typeof(this.committee) === 'string' && this.committee!= null){
        this.addPills('committee', this.committee.split(","), original)
      }
      else if(this.committee!= null){
        this.addPills('committee', this.committee, original)
      }

      if(typeof(this.people) === "string"){
        console.log("frm")
        this.addPills('people', this.people.split(","), original)
      }
      else{
        this.addPills('people', this.people, original)
      }
    }
  },
  computed: {
    committee () {
      console.log("computed committee")
      return this.advancedForm.committee
    },
    date () {
      return this.advancedForm.date
    },
    people () {
      console.log("computed people")
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
      var original = []
      for (let i = 0; i < this.pills.length; i++){
        original.push(this.pills[i].name)
      }
      this.addPills('committee', this.committee, original)
    },
    // date () {
    //   this.addPills('date', this.date)
    // },
    people () {
      var original = []
      for (let i = 0; i < this.pills.length; i++){
        original.push(this.pills[i].name)
      }
      this.addPills('people', this.people, original)
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
