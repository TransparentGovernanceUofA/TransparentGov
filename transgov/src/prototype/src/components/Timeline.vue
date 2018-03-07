<template>
  <div>
    <div id="visualization">
    </div>
  </div>
</template>

<script>
import vis from 'vis'
var container = {}
var items = {}
var options = {}
var timeline = {}
var test = {}

export default {
  name: 'app',
  mounted: function () {
  // DOM element where the Timeline will be attached
    container = document.getElementById('visualization')

    // Create a DataSet (allows two way data-binding)
    items = new vis.DataSet([
      {id: 1, content: 'Placeholder', start: '2018-03-07', title: '@TODO figure out how to handle missing data?'}
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
  },
  props: ['test'],
  watch: {
    test: function() {
      this.test.forEach(function(item, index) {
        items.add({content: item.title, start: item.timestamp, title: item.description})
      })
    }
  }
}
</script>

<style>
@import url("https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css");
</style>
