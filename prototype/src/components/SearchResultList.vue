<template>
  <div id="search-result-list">
    <ul>
      <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult._source" v-bind:id="searchresult.id">
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
  // computed: {
  //   searchresults () {
  //     return this.$store.state.searchresults
  //   }
  // },
  props: ['test']
}
</script>
