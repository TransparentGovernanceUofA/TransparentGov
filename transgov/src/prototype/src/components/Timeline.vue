<template>
  <div>
    <p v-for="(searchresult, index) in test" :key="index" :id="searchresult.id">{{searchresult.title}}</p>
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
      {id: 1, content: 'GFC meeting item 3', start: '2017-02-20', title: 'The various committees adjourn for bicycles'}
    ])
    
    items.add([{content: 'Eleven makes good bikes', start: '2011-10-10', title: 'bikes are better for 10'}])

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
       console.log(this.test[0].title)
       console.log("LOGGED!")
       items.add({content: this.test[0].title, start: '2000-10-10', title: 'testing'})
    }
  }
}
</script>

<style>
@import url("https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css");
</style>
