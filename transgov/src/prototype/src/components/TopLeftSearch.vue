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
          <!-- <input id="input-box" v-if = "truthy" v-model="searchBoxText" v-on:keyup.enter="goToResults()"/> -->
          <!-- <input id="input-box" disabled v-model="searchBoxText" v-on:keyup.enter="goToResults()"/> -->
          <!-- <input id="input-box" v-else disabled v-model="searchBoxText" v-on:keyup.enter="goToResults()"/> -->
        </b-col>
      </b-row>
    </b-container>
    
    
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      truthy: true,
      searchBoxText: '',
      inputField: {
        search: 'search:'
      }
    }
  },
  // the searchBox component will pass this prop for the search term
  props: ['previousInputField', 'advancedInputField'],
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
    // this.searchBoxText = this.$parent.inputField.search
  },
  methods: {
    goToResults () {
      // console.log('TESTING')
      this.inputField.search = 'search:' + this.searchBoxText
      let search = this.inputField.search
      this.$router.push({name: 'Result', params: { query: search }})
    }
  },
  // recognize when change occurs in advancedInput and update the text box
  watch: {
    advancedInputField () {
      this.truthy = false
      this.searchBoxText = ''
      for (var i = 0; i < this.advancedInputField.length; i++) {
        this.searchBoxText += this.advancedInputField[i].name + ' '
      }
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
</style>
