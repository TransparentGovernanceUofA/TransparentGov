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

// Temporarily using this function for demo purposes
// Credit to: https://stackoverflow.com/questions/9035627/elegant-method-to-generate-array-of-random-dates-within-two-dates
function randomDate (start, end) {
  return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()))
}

export default {
  name: 'app',
  mounted: function () {
  // DOM element where the Timeline will be attached
    container = document.getElementById('visualization')

    // Create a DataSet (allows two way data-binding)
    items = new vis.DataSet()
    items.add({content: 'wght', start: '2015-01-01', title: 'dssadsa'})

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
      handler: function () {
        items.clear() // Prevents duplication of results - potential bottleneck if dynamically adding data to a large result set
        this.results.forEach(function (item, index) {
          try {
            items.add({content: item._source.title, start: randomDate(new Date(2012, 0, 1), new Date()), title: item._source.description})
          } catch (e) {
            console.log('There was an error adding an item')
          }
        })
      },
      deep: true
    }
  }
}
</script>

<style>
@import url("https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css");
</style>
