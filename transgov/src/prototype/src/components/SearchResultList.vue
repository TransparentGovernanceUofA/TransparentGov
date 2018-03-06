<template>
  <div id="search-result-list">
    <b-container fluid>
    <b-row>
      <b-col cols=8>
        <b-row v-for="(searchresult, index) in test" :key="index" v-bind:id="searchresult.id" class="mt-4">
          <b-col>
            <!-- <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
            </SearchResult> -->
            <b-card header-tag="header" footer-tag="footer" class="md-elevation-3">
              <h6 slot="header" class="mb-0"><span class="title">{{ searchresult.title }}</span></h6>
              <p class="card-text">
                <span class="desc" maxlength="25">{{ searchresult.description }}</span>
              </p>
            </b-card>
          </b-col>
        </b-row>
      </b-col>
      
      
      <b-col cols=4>
        This section is meant for any sort of additional visualization or information. It may make more sense to have this column created in the Results component instead
              If so move it there before filling out --->
      </b-col>
    </b-row>
    
    </b-container>
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
  /*white-space: initial;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;*/
  /*max-length*/
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
