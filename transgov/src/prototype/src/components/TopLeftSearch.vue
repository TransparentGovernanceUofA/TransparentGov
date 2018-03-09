<template>
  <div class="top-left">
    <router-link to="/">
      <img src="./../assets/logoClearGov-XS.png" id="logo"/>
    </router-link>
    <input id="input-box" v-model="searchBoxText" v-on:keyup.enter="goToResults()"/>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      searchBoxText: '',
      inputField: {
        search: ''
      }
    }
  },
  // the searchBox component will pass this prop for the search term
  props: ['previousInputField'],
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
      this.inputField.search = this.searchBoxText
      let inputField = this.inputField
      // console.log(inputField)

      // router push wont reload if the path is the same, but the param will change, so Result has to watch for changes on inputField
      this.$router.push({name: 'Result', params: { inputField }})
    }
  }
}

</script>

<style>
#input-box{
  /*position:absolute;*/
  width: 500px;
  /*border-radius: 3px;
  top: 30px;*/
  height: 35px;
}
</style>
