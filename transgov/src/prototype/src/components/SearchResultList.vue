<template>
  <div id="search-result-list">
    <!-- This is a sub-component, the parent should declare a container for it -->
    <b-row v-for="(searchresult, index) in test" :key="index" v-bind:id="searchresult._id" class="mb-4" no-gutters>
      <!-- Note: the id of this row is used by the timeline component for click to focus -->
      <b-col>
        <!-- <SearchResult v-for="(searchresult, index) in test" :key="index" v-bind:searchresult="searchresult" v-bind:id="searchresult.id">
        </SearchResult> -->
        <b-card no-body header-tag="header" footer-tag="footer" class="md-elevation-3"
          border-variant="dark"
          header-bg-variant="dark"
          header-text-variant="white">

          <!-- We use a highlighted title if available, otherwise the regular title -->
          <!-- <h6 v-if="searchresult.highlight.Title" slot="header" class="mb-0">
            <span class="title" v-html="searchresult.highlight.Title[0]"></span>
            <router-link :to="{name: 'View PDF', params: { file_id:searchresult._source.url}}">
            View Original PDF
            </router-link>
          </h6> -->
          <!-- <h6 v-else slot="header" class="mb-0"> -->
          <h6 slot="header" class="mb-0">
             <!-- <span class="title" v-html="searchresult._source.Title"></span> -->
            {{searchresult._source.Title}}
            <a :href="searchresult._source.url" class="text-success">
              PDF
            </a>
          </h6>


          <!-- Tabs allow the matches for a result to be shown, but then also the meta data if they want to drill down -->
          <b-tabs card id="tabs-lvl-1">
            <b-tab title="Highlights">
                <!-- Match content, attempts to show all matches in a document, with highlights -->
                <p class="card-text clamp-3" v-for="(matches, category) in searchresult.highlight">
                  <ul>
                    <li>{{ category.slice(0,6) == "Items." ? category.slice(6) : category }}</li>
                    <ul>
                      <li v-for="match in matches"><span v-html="match"></span></li>
                    </ul>
                  </ul>
                </p>
              <p v-if="searchresult.highlight == null">We did not find any specific lines to highlight for this search.</p> 
            </b-tab>
            <b-tab title="Attendees">
                <p class="card-text" >
                  <ul>
                    <li v-for="attendee in searchresult._source.Attendees">{{attendee}}</li>
                  </ul>
                </p>
            </b-tab>
            <!-- CSS rules to handle the nested tabs rely on this being the 3rd tab, if you need to rearrange then change the rule -->
            <b-tab v-if="searchresult.highlight == null" title="Items" no-body active > <!-- select this tab if no highlights -->
                <b-tabs card>
                  <template v-for="item in searchresult._source.Items">
                    <b-tab :title="'Item ' + item['Item No.']" no-body>
                      <b-list-group flush>
                        <b-list-group-item v-for="(val, attrib) in item"><strong>{{attrib}}</strong>: {{val}}</b-list-group-item>
                      </b-list-group>
                    </b-tab>
                  </template>
                </b-tabs>
            </b-tab>
            <b-tab v-else title="Items" no-body> <!-- otherwise allow first tab to take default selection -->
                <b-tabs card>
                  <template v-for="item in searchresult._source.Items">
                    <b-tab :title="'Item ' + item['Item No.']" no-body>
                      <b-list-group flush>
                        <b-list-group-item v-for="(val, attrib) in item"><strong>{{attrib}}</strong>: {{val}}</b-list-group-item>
                      </b-list-group>
                    </b-tab>
                  </template>
                </b-tabs>
            </b-tab>
          </b-tabs>

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
  #tabs-lvl-1>.card-header{
    background-color: #e1e3e3;
  }
  .card-header em{
    background-color: #686b00;
  }
  #tabs-lvl-1>.card-header>ul>li:nth-child(3)>a.active{
    background-color: #f7f7f7;
    border-bottom-color: #f7f7f7;
  }
  a{
    color: #28a745;
  }
</style>
