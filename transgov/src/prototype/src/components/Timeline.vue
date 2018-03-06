<template>
  <div id="visualization">
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import vis from 'vis'
var container = {}
var items = {}
var options = {}
var timeline = {}

export default {
  name: 'app',
  mounted: function () {
  // DOM element where the Timeline will be attached
    container = document.getElementById('visualization')

    // Create a DataSet (allows two way data-binding)
    items = new vis.DataSet([
      {id: 1, content: 'GFC meeting item 3', start: '2017-02-20', title: 'The various committees adjourn for bicycles'},
      {id: 2, content: 'Branding committee meeting item 7', start: '2016-01-04', title: 'When the bicycles were allowed for retreat'},
      {id: 3, content: 'Meeting notes 7', start: '2008-08-02', title: 'How were bicycles allowed on the streets?'},
      {id: 4, content: 'Incident report', start: '1889-01-01', title: 'new invention, \'Bicycle\', allowed for use at UofA'},
      {id: 5, content: 'Title 2', start: '2009-07-03', title: 'Statement about bicycles'},
      {id: 6, content: 'What another title', start: '2018-04-02', title: 'and another statement about bikes'},
      {id: 7, content: 'The guardian issue 5', start: '2013-08-12', title: 'how could you use the bicycle so irresponsibly'},
      {id: 8, content: 'Meeting minutes 2018', start: '2003-03-23', title: 'another bicycle quote'},
      {id: 9, content: 'Why would I write another statement on bikes?', start: '2014-12-24', title: 'because bikes'},
      {id: 10, content: 'Because not bikes', start: '2012-12-12', title: 'bikes'},
      {id: 11, content: 'Eleven makes a good bike', start: '2011-10-10', title: 'bikes are better for 10'}
    ])

    // Configuration for the Timeline
    options = {
      tooltip: {
        followMouse: true,
        overflowMethod: 'cap'
      }
    }

    // Create a Timeline
    timeline = new vis.Timeline(container, items, options)
  },
  components: {
  }
}
</script>

<style>
@import url("https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css");
</style>
