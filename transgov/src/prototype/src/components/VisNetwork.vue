<template>
  <div id='test'>
    <div id="mynetwork"></div>
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
  mounted: function draw() {
      var nodes = [
        {id: 0, label: "0", group: 'source'},
        {id: 1, label: "1", group: 'organization'},
        {id: 2, label: "2", group: 'organization'},
        {id: 3, label: "3", group: 'organization'},
        {id: 4, label: "4", group: 'organization'},
        {id: 5, label: "5", group: 'organization'},
        {id: 6, label: "6", group: 'organization'},
        {id: 7, label: "7", group: 'organization'},
        {id: 8, label: "8", group: 'organization'},
        {id: 9, label: "9", group: 'organization'},
        {id: 10, label: "10", group: 'person'},
        {id: 11, label: "11", group: 'person'},
        {id: 12, label: "12", group: 'person'},
        {id: 13, label: "13", group: 'person'},
        {id: 14, label: "14", group: 'person'},
        {id: 15, group: 'group'},
        {id: 16, group: 'group'},
        {id: 17, group: 'group'},
        {id: 18, group: 'group'},
        {id: 19, group: 'group'},
        {id: 20, label: "diamonds", group: 'motionPass'},
        {id: 21, label: "diamonds", group: 'motionPass'},
        {id: 22, label: "diamonds", group: 'motionFail'},
        {id: 23, label: "diamonds", group: 'motionFail'},
    ];
    var edges = [
        {from: 1, to: 0},
        {from: 2, to: 0},
        {from: 4, to: 3},
        {from: 5, to: 4},
        {from: 4, to: 0},
        {from: 7, to: 6},
        {from: 8, to: 7},
        {from: 7, to: 0},
        {from: 10, to: 9},
        {from: 11, to: 10},
        {from: 10, to: 4},
        {from: 13, to: 12},
        {from: 14, to: 13},
        {from: 13, to: 0},
        {from: 16, to: 15},
        {from: 17, to: 15},
        {from: 15, to: 10},
        {from: 19, to: 18},
        {from: 20, to: 19},
        {from: 19, to: 4},
        {from: 22, to: 21},
        {from: 23, to: 22},
        {from: 23, to: 0},
    ]

    // create a network
    var container = document.getElementById('mynetwork');
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {
        nodes: {
            shape: 'dot',
            size: 20,
            font: {
                size: 15,
                color: 'black'
            },
            borderWidth: 2
        },
        edges: {
            width: 2
        },
        groups: {
          person: {
            shape: 'icon',
            icon: {
              face: 'FontAwesome',
              code: '\uf2bd',
              size: 50,
              color: 'blue'
            }
          },
          group: {
            shape: 'icon',
            icon: {
              face: 'FontAwesome',
              code: '\uf0c0',
              size: 50,
              color: 'red'
            }
          },
          organization: {
            color: {background: 'green'},
            shape: 'icon',
            icon: {
              face: 'FontAwesome',
              code: '\uf1ad',
              size: 50,
              color: 'orange'
            }
          },
          motionPass: {
            shape: 'icon',
            icon: {
              face: 'FontAwesome',
              code: '\uf058',
              size: 50,
              color: 'green'
            }
          },
          motionFail: {
            shape: 'icon',
            icon: {
              face: 'FontAwesome',
              code: '\uf057',
              size: 50,
              color: 'red'
            }
          }
        }
    };
    var network = new vis.Network(container, data, options);
    },
  components: {
  }
}
</script>

<style>
@import url("https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css");
@import url("http://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");

#mynetwork{
  height: 400px;
  }
</style>
