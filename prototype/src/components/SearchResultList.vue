<template>
  <div id="search-result-list">
    <ul>
      <SearchResult v-for="(searchresult, index) in searchresults" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
      </SearchResult>
    </ul>
  </div>
</template>

<script>
import SearchResult from './SearchResult.vue'

export default {
  components: {
    SearchResult
  },
  computed: {
    searchresults () {
      return this.$store.state.searchresults
    }
  }
}
</script>
