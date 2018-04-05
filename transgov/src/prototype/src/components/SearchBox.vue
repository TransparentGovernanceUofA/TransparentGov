<template>
  <b-container fluid id="search-container">
    <b-row id="content-row" align-v="center" align-h="center">
      <b-col md=8>
        <div id="user-searches" class="md-elevation-8">
          <b-row>
            <b-col>
              <button @click="open=true" id="helpBtn"><img src="./../assets/manual-icon-vector.svg"></button>
              <router-link to="/">
                <img src="./../assets/logoOpenGov2-3anim.svg" class="m-2"/>
              </router-link>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <small>Transparent and Open Governance at the University of Alberta</small>
            </b-col>
          </b-row>

          <b-row class="mt-2" align-h="center">
            <b-col lg=8>
              <!-- b-form-input breaks the listening for key up of enter -->
              <input v-model="newSearchBoxText" @change="newInput()" v-on:keyup.enter="goToResults()" id="input-box1" class="form-control" :placeholder='inputPrompt' />
              <!-- <b-form-input size="lg" @change="newInput()" v-model="newSearchBoxText" id="input-box1" v-on:keyup.enter="goToResults()"></b-form-input> -->
            </b-col>
          </b-row>

          <b-row class="mt-2" align-h="center">
            <b-col class="mt-2 mt-lg-0" lg=4 order="2" order-lg="1">
              <router-link :to="{name: 'Advanced Search', params: { query:'search:', committees:'committee:', people:'people:', dateStart:'dateStart:', dateEnd: 'dateEnd:'}}">
                <b-button variant="outline-primary" size="lg" class="search" id="advancedSearchButton">Advanced Guide</b-button>
              </router-link>
            </b-col>
            <b-col lg=4 order="1" order-lg="2">
              <!-- <router-link :to="{name: 'Result', params: { query: 'search:' + newSearchBoxText, committees:'committee:', people:'people:', dateStart:'dateStart:', dateEnd: 'dateEnd:'}}"> -->
                <b-button variant="outline-primary" size="lg" class="search" id="searchButton" v-on:click="goToResults()">Search</b-button>
              <!-- </router-link> -->
            </b-col>
            <!-- <button @click="open=true" id="helpBtn"><img src="./../assets/manual-icon-vector.svg">modal-basic</button> -->
          </b-row>
          <b-row id="helpButton" class="m-0">
            <b-col class="mt-2 p-0">
                <b-button @click="open=true" variant="outline-primary" size="lg" class="search" >Help</b-button>
            </b-col>
          </b-row>
          <vue-modaltor :visible="open" :bgOverlay="'1d720c'" @hide="hideModal">
            <div id="mainDiv">
              <div id="intro">
                <h1> What is OpenGov? </h1>
                <p> OpenGov is an initiative taken by the University of Alberta General Faculties Council (GFC) to create transparency and ease of access to information regarding it's decisions and delegations. OpenGov is a search service allowing users to query and receive results based on publicly accessible information about GFC meeting minutes, agendas and meeting material documents. 

                Use OpenGov to prepare for a meeting or even to deep dive into a specific topic.</p>
              </div>

              <h5> Search </h5>
              <div id="search">
                <p> The basic search is an easy way to search for a specific topic in a quick and efficient way. Type what you interested in into the searh bar and hit the "Search" button and see what results appear!</p>
              </div>

              <div id="advanced">
                <h5> Advanced Search </h5>
                <p>Advanced Search houses a more specialized feature set to narrow down results. Access “Advanced Search” by clicking “Advanced Guide” on the home page. On this page, you can enter your search term(s) and manipulate options to filter by "Committee" or "People". You can outline a Start Date and End Date to trim down your results.

                Once you’ve hit search your results will be generated and displayed. You can sort each returned document by the Highlights (which has the highlighted search text in it) or by Attendees or Items. For a further dive you can click “View Original PDF” and have the PDF served to your window. 

                From here you can rotate, print and use the PDF.</p>
              </div>

              <div id="timeline">
                <h5> Timeline </h5>
                <p> To use the timeline, first search for an item that has results. Click the Show/Hide Timeline to toggle it on or off. The timeline is a way to visualize your search results by the date they occurred on. Each bubble shoes the committee and day, and a line connects it to the precise location on the timeline at the bottom of the visualization.

                You can manipulate the timeline by Zooming (using your Mouse Wheel / Pinch) and scroll left and right by clicking and dragging or swiping. 

                Selecting an item on the time line jumps immediately to the corresponding search result card below the timeline. </p>
              </div>

              <div id = "general">
                <h5> General </h5>
                <p>If at any point you want to return to the homepage, click the OpenGov logo in the top left-hand corner.

                If at any point you are confused, you can click the "?" icon beside the feature to get help. </p>
              </div>
            </div>
          </vue-modaltor>
          <!--
          <b-row>
            <b-col>
              <router-link :to="{name: 'Timeline'}">
                <b-button id="search2">Timeline test</b-button>
              </router-link>
            </b-col>
          </b-row>
          -->

        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  data: function () {
    return {
      newSearchBoxText: '',
      inputField: {
        search: 'search:'
      },
      inputPrompt: '',
      open: false,
      props: {
        // this is for toggle show modal 
        // :visible:false
        visible: {
          type: Boolean,
          required: false,
          default: false
        },
        // this is for bgcolor overlay
        bgOverlay:{
          type: String,
          required: false,
          default: '#fff'
        }
        // defaultWidth:{
        //   type: String,
        //   required: false,
        //   default: '30%'
        // }
      }
    }
  },
  methods: {
    // whenever action occurs like clicking search or enter, stores that input value into prop that will be sent
    newInput () {
      // console.log(this.newSearchBoxText)
      // console.log(this.$route.params)
      // the string 'search:' is appended to both mark what comes next as the search term and to make sure that whats being appended to the URL is not empty
      this.inputField.search = 'search:' + this.newSearchBoxText
    },

    goToResults () {
      // console.log('-----goToResults function called------')
      // console.log(this.inputField)

      if (this.inputField.search == 'search:') {
        this.inputPrompt = 'Search for...'
      } else {
        let search = this.inputField.search
      this.$router.push({name: 'Result', params: { query: search, committees:'committee:', people:'people:', dateStart:'dateStart:', dateEnd: 'dateEnd:'}})
      }
    },
    hideModal () {
      this.open = false
    }
  }
}
</script>

<style>
#input-box1{
  width: 100%;
  /*border-radius: 3px;*/
}
#search-container{
  min-height: 100vh;
  background-image: url("https://i.imgur.com/qZxEk6z.jpg");
  background-size: cover;
}
#user-searches{
  text-align: center;
  background: white;
  padding: 20px;
  /*margin-top: 150px;*/
}
#content-row{
  height: 80vh;
}
.search{
  width: 100%;
}
@keyframes hideshow {
  0% { transform: translate(0px, 0px); }
  5% { transform: translate(-100px, 0px); }
  80% { transform: translate(-100px, 0px); }
  85% { transform: translate(0px, 0px); }
  100% { transform: translate(0px, 0px); }
} 

/* The element to apply the animation to */

#rect1 {
    animation-name: hideshow;
    animation-duration: 20s;
    animation-iteration-count: infinite;
}

#helpBtn{
  background-color: white;
  border: none;
  color: white;
  float: right;
  height: 75px;
  width: 75px;
  display: unset;
}
#helpButton{
  display: none;
}
  
@media screen and (max-width: 992px) {
  #helpBtn {
    display: none;
  }
  #helpButton {
    display: unset;
  }
}
</style>
