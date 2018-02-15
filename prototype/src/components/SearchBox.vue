<template>
  <div id="user-searches">
    <router-link to="/">
      <img src="./../assets/transparentGovernance.png" id = "logo">
    </router-link>
    <br/>
    <input v-model="newSearchBoxText" v-on:keyup.enter="createSearchResult" id="input-box">
    <br/>
    <!-- <button v-on:click="clearSearchBox" id="clear-btn" class="btn">
      Clear
    </button> -->
    <!-- <button v-on:click="showList" id="search-btn" class="btn"> -->
    <!-- <button v-on:click="toggleList" id="search-btn" class="btn">
      Search
    </button> -->
    <router-link to="/result">
      <button id="search" class = btn>search!</button>
    </router-link>
  </div>
</template>

<script>
export default {
  data: function () {
    return {newSearchBoxText: ''}
  },
  methods: {
    createSearchResult () {
      this.$store.dispatch('addResult', {text: this.newSearchBoxText})
      this.newSearchBoxText = ''
    },
    clearSearchBox () {
      this.$store.dispatch('clearResults')
    },
    toggleList () {
      this.$emit('toggleList', 'somevalue')
    }
  }
}
</script>

<style>
#input-box{
  width: 500px;
}
.btn{
  height: 25px;
  width: 200px;
}

#user-searches{
  text-align: center;
  margin-top: 150px;
}
</style>
