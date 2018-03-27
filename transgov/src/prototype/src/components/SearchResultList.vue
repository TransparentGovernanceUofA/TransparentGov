<template>
  <div id="search-result-list">
    <!-- This is a sub-component, the parent should declare a container for it -->
    <b-row v-for="(searchresult, index) in test" :key="index" v-bind:id="searchresult.id" class="mt-4" no-gutters>
      <b-col>
        <!-- <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
        </SearchResult> -->
        <b-card header-tag="header" footer-tag="footer" class="md-elevation-3">
          <!-- <h6 slot="header" class="mb-0"><span class="title">{{ searchresult._source.title }}</span></h6>
          <p class="card-text clamp-3">
            <span class="desc">{{ searchresult._source.description }}</span>
          </p> -->
          
          <h6 v-if= searchresult slot="header" class="mb-0" v-for="title in searchresult.highlight.title">
            <span class="title" v-html="title"></span>
            <router-link :to="{name: 'View PDF', params: { file_id:'file_id:' + searchresult._source.django_id}}">
            See more
            </router-link>
          </h6>
          <p class="card-text clamp-3" v-for="desc in searchresult.highlight.description">
            <span class="desc" v-html="desc"></span>
          </p>

        </b-card>
      </b-col>
    </b-row>
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
.clamp-3{
  max-height: 4.5em;
  overflow: hidden;
}

em{
  font-style:normal;
  font-weight: bold;
  background-color: #FFFFCC;
}
</style>
