<template>
  <b-container fluid id="search-container">
    <b-row id="content-row" align-v="center" align-h="center">
      <b-col cols=8>
        <div id="user-searches" class="md-elevation-8">
          <router-link to="/">
            <img src="./../assets/logoClearGov-M.png" id="logo">
          </router-link>
          <br/>
          <!-- <input v-model="newSearchBoxText" v-on:keyup.enter="createSearchResult" id="input-box1"> -->
          <input @change="newInput()" v-model="newSearchBoxText" id="input-box1">
          <br/>
          <router-link to="/advancedsearch">
            <md-button id="search1" class = "md-raised" :md-ripple="false">Advanced Search</md-button>
          </router-link>
          <router-link :to="{name: 'Result', params: { inputField }}">
            <md-button id="search" class = "md-raised" :md-ripple="false">search!</md-button>
          </router-link>
          <router-link to="/timeline">
            <md-button id="search2" class = "md-raised" :md-ripple="false">Timeline test</md-button>
          </router-link>
        </div>
      </b-col>
    </b-row>
  </b-container>
  
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
body{
  background-image: url("https://i.imgur.com/qZxEk6z.jpg");
  background-size: cover;
}
#user-searches{
  text-align: center;
  background: white;
  padding: 20px;
  /*margin-top: 150px;*/
}
#content-row{
  height: 80vh;
}
</style>
