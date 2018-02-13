<template>
  <div id="search-result-list">
    <ul>
      <!-- <li v-for="(searchresult, index) in searchresults" :key="index"> -->
      <SearchResult v-for="(searchresult, index) in searchresults" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
      </SearchResult>
      <!-- </li> -->
    </ul>
  </div>
</template>

<script>
import SearchResult from './SearchResult.vue'

export default {
  components: {
    SearchResult
  },
  // data: function () {
  //   return {
  //     searchresults: [
  //       { text: 'Learn Vue' },
  //       { text: 'Do hard things' }
  //     ]
  //   }
  // }
  computed: {
    searchresults () {
      return this.$store.state.searchresults
    }
  }
}
</script>
