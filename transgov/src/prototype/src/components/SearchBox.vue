<template>
  <div id="user-searches">
    <router-link to="/">
      <img src="./../assets/transparentGovernance.png" id = "logo">
    </router-link>
    <br/>
    <!-- <input v-model="newSearchBoxText" v-on:keyup.enter="createSearchResult" id="input-box1"> -->
    <input @change="newInput()" v-model="newSearchBoxText" id="input-box1" v-on:keyup.enter="goToResults()">
    <br/>
    <router-link to="/advancedsearch">
      <md-button id="search1" class = "md-raised" :md-ripple="false">Advanced Search</md-button>
    </router-link>
    <router-link :to="{name: 'Result', params: { inputField }}">
      <md-button id="search" class = "md-raised" :md-ripple="false">search</md-button>
    </router-link>
    <router-link to="/timeline">
      <md-button id="search2" class = "md-raised" :md-ripple="false">Timeline test</md-button>
    </router-link>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      newSearchBoxText: '',
      inputField: {
        search: ''
      }
    }
  },
  methods: {
    // whenever action occurs like clicking search or enter, stores that input value into prop that will be sent
    newInput () {
      // console.log(this.newSearchBoxText)
      this.inputField.search = this.newSearchBoxText
    },

    goToResults () {
      // console.log("-----goToResults function called------")
      // console.log(this.inputField)

      let inputField = this.inputField
      this.$router.push({ name: 'Result' , params: { inputField }})
    }
  }
}
</script>

<style>
#input-box1{
  width: 500px;
  border-radius: 3px;
  height: 40px;
}
.md-raised{
  height: 25px;
  width: 200px;
}

#user-searches{
  text-align: center;
  margin-top: 150px;
}
</style>
