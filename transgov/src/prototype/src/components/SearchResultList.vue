<template>
  <div id="search-result-list">
    <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
    </SearchResult>
    <!-- {{ test }} -->
  </div>
</template>

<script>
import SearchResult from './SearchResult.vue'

export default {
  components: {
    SearchResult
  },
  props: ['test']
}
</script>
