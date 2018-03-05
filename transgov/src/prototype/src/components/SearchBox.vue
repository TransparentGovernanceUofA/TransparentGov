<template>
  <b-container fluid id="search-container">
    <b-row id="content-row" align-v="center" align-h="center">
      <b-col cols=8>
        <div id="user-searches" class="md-elevation-8">
          <b-row>
            <b-col>
              <router-link to="/">
                <img src="./../assets/logoClearGov-M.png" id="logo">
              </router-link>
            </b-col>
          </b-row>
          
          <b-row align-h="center">
            <b-col cols=8>
              <!-- <input v-model="newSearchBoxText" v-on:keyup.enter="createSearchResult" id="input-box1"> -->
              <b-form-input size="lg" @change="newInput()" v-model="newSearchBoxText" id="input-box1"></b-form-input>
            </b-col>
          </b-row>
          
          <b-row class="mt-4">
            <b-col>
              <router-link to="/advancedsearch">
                <b-button :variant="outline-success" id="search1">Guide</b-button>
              </router-link>
            </b-col>
            <b-col>
              <router-link :to="{name: 'Result', params: { inputField }}">
                <b-button id="search">Search</b-button>
              </router-link>
            </b-col>
            <b-col>
              <router-link to="/timeline">
                <b-button id="search2">Timeline test</b-button>
              </router-link>
            </b-col>
          </b-row> 
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
  width: 100%;
  /*border-radius: 3px;*/
}
#search-container{
  min-height: 100vh;
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
