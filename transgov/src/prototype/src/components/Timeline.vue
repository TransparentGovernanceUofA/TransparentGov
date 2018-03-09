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

export default {
  name: 'app',
  mounted: function () {
  // DOM element where the Timeline will be attached
    container = document.getElementById('visualization')

    // Create a DataSet (allows two way data-binding)
    items = new vis.DataSet()
    items.add({content: "wght", start: "2015-01-01", title: "dssadsa"})

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
  props: ['results'],
  watch: {
    results: {
      handler: function() {
      },
      deep: true
    }
  }
}
</script>

<style>
@import url("https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css");
</style>
