<template>
  <div id="search-result-list">
    <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult._source" v-bind:id="searchresult.id">
    </SearchResult>
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
