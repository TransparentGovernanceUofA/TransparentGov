<template>
  <div class="viewPDF">
    <p>We recieved this file ID: {{file_id}}</p>
    
    <canvas id="theCanvas"></canvas>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'
import pdfjsLib from 'pdfjs-dist'
import pdfjsViewer from 'pdfjs-dist'


export default{
  props: {
    inputField: {
      type: Object,
      default: () => ({})
    },
    // file_id is accessing whats appended to the URL, ie /file/:file_id
    file_id: {
      type: String
    }
  },
  components: {
    TopLeftSearch,
  },
  name: 'ElasticResults',
  data () {
    return {
      ElasticResult: {},
    }
  },
  created () {
  },
  mounted () {
    // Any copyright is dedicated to the Public Domain.
    // http://creativecommons.org/licenses/publicdomain/

    // Hello world example for webpack.

    var pdfjsLib = require('pdfjs-dist');

    var pdfPath = '/static/GFC/2017-09-25/Past-Meeting-Material.pdf';

    // Setting worker path to worker bundle.
    pdfjsLib.GlobalWorkerOptions.workerSrc =
      '../../build/webpack/pdf.worker.bundle.js';

    // Loading a document.
    var loadingTask = pdfjsLib.getDocument(pdfPath);
    loadingTask.promise.then(function (pdfDocument) {
      // Request a first page
      return pdfDocument.getPage(1).then(function (pdfPage) {
        // Display page on the existing canvas with 100% scale.
        var viewport = pdfPage.getViewport(1.0);
        var canvas = document.getElementById('theCanvas');
        canvas.width = viewport.width;
        canvas.height = viewport.height;
        var ctx = canvas.getContext('2d');
        var renderTask = pdfPage.render({
          canvasContext: ctx,
          viewport: viewport
        });
        return renderTask.promise;
      });
    }).catch(function (reason) {
      console.error('Error: ' + reason);
    });
  },
  watch: {
    // query is accessing whats appended to the URL, ie /file/:file_id
    file_id: function () {
      this.fetchData()
    }
  },

  methods: {
    fetchData () {
    },
    password: function(updatePassword, reason) {
      updatePassword(prompt('password is "test"'));
    },
    error: function(err) {
      console.log(err);
    }
  }
}
</script>

<style>
  /* Copyright 2016 Mozilla Foundation
   *
   * Licensed under the Apache License, Version 2.0 (the "License");
   * you may not use this file except in compliance with the License.
   * You may obtain a copy of the License at
   *
   *     http://www.apache.org/licenses/LICENSE-2.0
   *
   * Unless required by applicable law or agreed to in writing, software
   * distributed under the License is distributed on an "AS IS" BASIS,
   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   * See the License for the specific language governing permissions and
   * limitations under the License.
   */
  /*
  * {
    padding: 0;
    margin: 0;
  }

  html {
    height: 100%;
    width: 100%;
    overflow: hidden;
    font-size: 10px;
  }

  header {
    background-color: #f4f4f4;
  }

  header h1 {
    border-bottom: 1px solid #d8d8d8;
    color: #858585;
    font-size: 23px;
    font-style: italic;
    font-weight: normal;
    overflow: hidden;
    padding: 10px;
    text-align: center;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  body {
    background: url(./../assets/images/document_bg.png);
    color: #fff;
    font-family: sans-serif;
    font-size: 10px;
    height: 100%;
    width: 100%;
    overflow: hidden;
    padding-bottom: 5rem;
  }

  section {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    font-size: 2rem;
  }

  footer {
    background-image: url(./../assets/images/toolbar_background.png);
    height: 4rem;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1;
    box-shadow: 0 -0.2rem 0.5rem rgba(50, 50, 50, 0.75);
  }

  .toolbarButton {
    display: block;
    padding: 0;
    margin: 0;
    border-width: 0;
    background-position: center center;
    background-repeat: no-repeat;
    background-color: transparent;
  }

  .toolbarButton.pageUp {
    position: absolute;
    width: 18%;
    height: 100%;
    left: 0;
    background-image: url(./../assets/images/icon_previous_page.png);
    background-size: 2rem;
  }

  .toolbarButton.pageDown {
    position: absolute;
    width: 18%;
    height: 100%;
    left: 18%;
    background-image: url(./../assets/images/icon_next_page.png);
    background-size: 2rem;
  }

  #pageNumber {
    -moz-appearance: textfield; 
    position: absolute;
    width: 28%;
    height: 100%;
    left: 36%;
    text-align: center;
    border: 0;
    background-color: transparent;
    font-size: 1.2rem;
    color: #FFF;
    background-image: url(./../assets/images/div_line_left.png), url(./../assets/images/div_line_right.png);
    background-repeat: no-repeat;
    background-position: left, right;
    background-size: 0.2rem, 0.2rem;
  }

  .toolbarButton.zoomOut {
    position: absolute;
    width: 18%;
    height: 100%;
    left: 64%;
    background-image: url(./../assets/images/icon_zoom_out.png);
    background-size: 2.4rem;
  }

  .toolbarButton.zoomIn {
    position: absolute;
    width: 18%;
    height: 100%;
    left: 82%;
    background-image: url(./../assets/images/icon_zoom_in.png);
    background-size: 2.4rem;
  }

  .toolbarButton[disabled] {
    opacity: .3;
  }

  .hidden {
    display: none;
  }
  [hidden] {
    display: none !important;
  }

  #viewerContainer {
    position: absolute;
    overflow: auto;
    width: 100%;
    top: 5rem;
    bottom: 4rem;
    left: 0;
    right: 0;
  }

  canvas {
    margin: auto;
    display: block;
  }

  .pdfViewer .page .loadingIcon {
    width: 2.9rem;
    height: 2.9rem;
    background: url("./../assets/images/spinner.png") no-repeat left top / 38rem ;
    border: medium none;
    animation: 1s steps(10, end) 0s normal none infinite moveDefault;
    display: block;
    position: absolute;
    top: calc((100% - 2.9rem) / 2);
    left: calc((100% - 2.9rem) / 2);
  }

  @keyframes moveDefault {
    from {
      background-position: 0 top;
    }

    to {
      background-position: -39rem top;
    }
  }

  #loadingBar {
    position: relative;
    height: .6rem;
    background-color: #333;
    border-bottom: 1px solid #333;
    margin-top: 5rem;
  }

  #loadingBar .progress {
    position: absolute;
    left: 0;
    width: 0;
    height: 100%;
    background-color: #ddd;
    overflow: hidden;
    transition: width 200ms;
  }

  @keyframes progressIndeterminate {
    0% { left: 0; }
    50% { left: 100%; }
    100% { left: 100%; }
  }

  #loadingBar .progress.indeterminate {
    background-color: #999;
    transition: none;
  }

  #loadingBar .indeterminate .glimmer {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 5rem;

    background-image: linear-gradient(to right, #999 0%, #fff 50%, #999 100%);
    background-size: 100% 100%;
    background-repeat: no-repeat;

    animation: progressIndeterminate 2s linear infinite;
  }

  #errorWrapper {
    background: none repeat scroll 0 0 #FF5555;
    color: white;
    left: 0;
    position: absolute;
    right: 0;
    top: 3.2rem;
    z-index: 1000;
    padding: 0.3rem;
    font-size: 0.8em;
  }

  #errorMessageLeft {
    float: left;
  }

  #errorMessageRight {
    float: right;
  }

  #errorMoreInfo {
    background-color: #FFFFFF;
    color: black;
    padding: 0.3rem;
    margin: 0.3rem;
    width: 98%;
  } */
</style>