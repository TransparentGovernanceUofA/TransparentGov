<template>
  <div id="search-result-list">
    <!-- This is a sub-component, the parent should declare a container for it -->
    <b-row v-for="(searchresult, index) in test" :key="index" v-bind:id="searchresult.id" class="mt-4" no-gutters>
      <b-col>
        <!-- <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
        </SearchResult> -->
        <b-card no-body header-tag="header" footer-tag="footer" class="md-elevation-3">
          
          <!-- We use a highlighted title if available, otherwise the regular title -->
          <h6 v-if="searchresult.highlight.Title" slot="header" class="mb-0">
            <span class="title" v-html="searchresult.highlight.Title[0]"></span>
            <router-link :to="{name: 'View PDF', params: { file_id:searchresult._source.url}}">
            View Original PDF
            </router-link>
          </h6>
          <h6 v-else slot="header" class="mb-0">
            {{searchresult._source.Title}}
            <router-link :to="{name: 'View PDF', params: { file_id:searchresult._source.url}}">
            View Original PDF
            </router-link>
          </h6>
          
          <!-- Match content, attempts to show all matches in a document -->
          <p class="card-text clamp-3" v-for="(matches, category) in searchresult.highlight">
            <ul>
              <li>{{ category.slice(0,6) == "Items." ? category.slice(6) : category }}</li>
              <ul>
                <li v-for="match in matches"><span v-html="match"></span></li>
              </ul>
            </ul>
          </p>
        </b-card>
        <!-- Upgraded version in the works
        <b-card no-body header-tag="header" footer-tag="footer" class="md-elevation-3">
          <h6 v-if= searchresult slot="header" class="mb-0">
            {{searchresult._source.Title}}
            <router-link :to="{name: 'View PDF', params: { file_id:searchresult._source.url}}">
            View Original PDF
            </router-link>
          </h6>
          <b-tabs card>
            <b-tab title="Highlights">
                If highlights start working put them in here, otherwise comment out this tab
            </b-tab>
            <b-tab title="Attendees">
                If highlights start working put them in here, otherwise comment out this tab
            </b-tab>
            <b-tab title="Items" no-body>
                <b-tabs card>
                  <b-tab title="Tab 1" active>
                    Tab Contents 1
                  </b-tab>
                  <b-tab title="Tab 2">
                    Tab Contents 2
                  </b-tab>
                </b-tabs>
            </b-tab>
            <div v-for="desc in searchresult._source.Items">
              <b-tab title="Tab 1">
                Tab Contents 1
              </b-tab>
            </div>
          </b-tabs>
        </b-card>
        -->
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
