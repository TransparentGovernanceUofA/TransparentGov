<template>
  <div id="user-searches">
    <input v-model="newSearchBoxText" v-on:keyup.enter="createSearchResult" id="input-box">
    <button v-on:click="clearSearchBox" id="clear-btn">
      Clear
    </button>
    <button id="search-btn">
      Search
    </button>
  </div>
</template>

<script>
export default {
  data: function () {
    return { newSearchBoxText: '' }
  },
  methods: {
    createSearchResult () {
      console.log(this.newSearchBoxText, 'created!')
    },
    clearSearchBox () {
      console.log('search results cleared!')
    }
  }
}
</script>

<style>
#clear-btn #input-box{
  display: block;
}
</style>
