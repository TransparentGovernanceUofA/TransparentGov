<template>
  <div id="search-result-list">
    <b-container fluid>
    <b-row v-for="(searchresult, index) in test" :key="index" v-bind:id="searchresult.id">
      <b-col cols=8>
        <b-card header-tag="header" footer-tag="footer">
          <h6 slot="header" class="mb-0"><span class="title"> {{ searchresult.title }}</span></h6>
          <p class="card-text">
            <span class="desc"> {{ searchresult.description }}</span>
          </p>
        </b-card>
      </b-col>
    </b-row>
    </b-container>
    <md-list>
      <!-- <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
      </SearchResult> -->
      <md-list-item >
        <div class="md-list-item-text">
          
          
          
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
/*
.md-list-item{
  left: 13%;
  width: 600px;
}
.md-list-item-text{
  padding-bottom: 15px;
}
*/
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
