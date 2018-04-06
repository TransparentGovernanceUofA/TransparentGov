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
  
function onSelect (properties) {
  if (properties.items.length == 0){
    return
  }
  var result_card = document.getElementById(items.get(properties.items[0]).id);
  result_card.scrollIntoView();
}

export default {
  name: 'app',
  mounted: function () {
    
    // DOM element where the Timeline will be attached
    container = document.getElementById('visualization')

    // Create a DataSet (allows two way data-binding)
    items = new vis.DataSet()

    // Configuration for the Timeline
    options = {
      tooltip: {
        followMouse: true,
        overflowMethod: 'cap'
      },
      minHeight: "200px",
      maxHeight: "400px"
    }

    // Create a Timeline
    timeline = new vis.Timeline(container, items, options)
    
    // add event listener
    timeline.on('select', onSelect);
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
            items.add({id: item._id, content: item._source.Title, start: item._source.Date, title: "Click to jump to result"})
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
  .vis-item{
    color: white;
    border-color: #009221;
    background-color: #28a745;
  }
  .vis-item.vis-selected{
    color: #343a40; 
  }
</style>
