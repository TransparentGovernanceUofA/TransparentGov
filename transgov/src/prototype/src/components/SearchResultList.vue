<template>
  <div id="search-result-list">
    <md-list>
      <!-- <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
      </SearchResult> -->
      <md-list-item v-for="(searchresult, index) in test" :key="index" v-bind:id="searchresult.id">
        <div class="md-list-item-text">
          <span class="title"> {{ searchresult.title }}</span>
          <span class="desc"> {{ searchresult.description }}</span>
        </div>
      </md-list-item>
    </md-list>
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

<style>
.md-list-item{
  left: 13%;
  width: 600px;
}
.md-list-item-text{
  padding-bottom: 15px;
}
.desc{
  white-space: initial;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
.title{
  /*width: 400px;*/
  font-weight: bold;
  white-space: initial;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

</style>
