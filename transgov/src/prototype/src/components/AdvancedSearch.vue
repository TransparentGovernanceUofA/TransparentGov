<template>
  <div class="advancedSearch">
    <top-left-search :previousInputField="inputField" :advancedForm="form"></top-left-search>
    <div id="AdvancedSearch">
      <b-container fluid >
        <b-row>
          <b-col md=4 order="2" order-md="1">
            <!-- The inputs and options -->
            <b-card header="Search Options" class="mt-4 md-elevation-3">
              <div class="help-tip">
                <p>List of committees at the University of Alberta.</p>
              </div>
              <b-form-group id="committee"
                          label="Committee"
                          label-for="exampleInput2">
                <b-form-select id="exampleInput2"
                            :options="committeeOptions"
                            required
                            v-model="form.committee">
                </b-form-select>
              </b-form-group>
              <b-form-group id="date">
                <b-row>
                  <b-col>
                    <p> Start: </p>
                    <date-picker v-model="date_start" :config="config_date_start"></date-picker>
                  </b-col>
                  <b-col>
                    <div id="time-help" class="help-tip">
                      <p>Date picker, allows searching in a range of dates.</p>
                    </div>
                    <p> End: </p>
                    <date-picker v-model="date_end" @change="change" :config="config_date_end"></date-picker>
                  </b-col>
                </b-row>
              </b-form-group>
              <div class="help-tip">
                <p>Various members that take part in Governance discussions.</p>
              </div>
              <b-form-group id="people"
                          label="People"
                          label-for="exampleInput5">
                <b-form-select id="exampleInput5"
                            :options="peopleOptions"
                            required
                            v-model="form.people">
                </b-form-select>
              </b-form-group>
            </b-card>
          </b-col>
          <b-col md=8 order="1" order-md="2">
          <!-- The explanation box -->
            <b-card header="Guide" class="mt-4 md-elevation-3" >
              <p class="card-text">This area will help you discover the more advanced search capabilities of the system. The "Search Options" card houses several selections of known topics, people, organizations, etc. that the system knows about. By selecting any one of these fields the "Query" box will update to include the query that will be needed to search for those specific items.</p>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import TopLeftSearch from './TopLeftSearch.vue'

export default {
  props: {
    inputField: {
      type: Object,
      default: () => ({})
    },
    query: {
      type: String
    },
    advanced: {
      type: String
    }
  },
  components: {
    TopLeftSearch,
  },
  created () {
    this.parseQuery()
  },
  methods: {
    // this method does not work, beause it grabs the result to quickly, debounce needed to delay the method
    // changedTopicInput () {
    //   console.log(this.form.topic)
    // }
    parseQuery () {
      var queryArray = this.query.split(':')
      this.inputField.search = queryArray[1]

      var advancedArray = this.advanced.split(':')
      if (advancedArray[1] !== 'false') {
        this.form.committee = advancedArray[2]
        if (this.form.committee === '') {
          this.form.committee = null
        }

        this.form.date = advancedArray[4]
        if (this.form.date === '') {
          this.form.date = null
        }

        this.form.people = advancedArray[6]
        if (this.form.people === '') {
          this.form.people = null
        }
      }
      // console.log(this.form)
      // console.log(this.inputField.search)
    },
    change () {
      console.log("change")
    }
  },
  data () {
    return {
      newSearchBoxText: '',
      advancedInputField: {
        search: ''
      },
      form: {
        committee: null,
        date: null,
        people: null
      },
      committeeOptions: [
        { value: null, text: '' },
        { value: '1 committee', text: '1 committee' },
        { value: '2 committee', text: '2 committee' },
        { value: '3 comimttee', text: '3 comimttee' }
      ],
      dateOptions: [
        { value: null, text: '' },
        { value: '1 idk', text: '1 idk' },
        { value: '2 what', text: '2 what' },
        { value: '3 we want for this', text: '3 we want for this' }
      ],
      peopleOptions: [
        { value: null, text: '' },
        { value: 'Eleni', text: 'Eleni' },
        { value: 'Barbosa', text: 'Barbosa' },
        { value: 'Diego', text: 'Diego' }
      ],
      date_start: null,
      config_date_start: {
        format: 'DD/MM/YYYY',
        useCurrent: false,
        showClear: true,
        showClose: true,
        maxDate: new Date()
      },
      date_end: new Date(),
      config_date_end: {
        format: 'DD/MM/YYYY',
        useCurrent: false,
        showClear: true,
        showClose: true,
        maxDate: new Date()
      }              
    }
  },

  // watch: {
  //   date_end: function(val, oldval){
  //     console.log(val)
  //   }
  // }
}
</script>

<style>
#end{
  z-index:-1;
}
.help-tip{
    position: absolute;
    /*top: 18px;*/
    /*right: 100px;*/
    text-align: center;
    background-color: #BCDBEA;
    border-radius: 50%;
    width: 23px;
    height: 23px;
    font-size: 14px;
    line-height: 26px;
    cursor: default;
    left: 92.5%;
}

#time-help{
    position: absolute;
    /*top: 18px;*/
    /*right: 100px;*/
    text-align: center;
    background-color: #BCDBEA;
    border-radius: 50%;
    width: 23px;
    height: 23px;
    font-size: 14px;
    line-height: 26px;
    cursor: default;
    left: 86.5%;
}

.help-tip:before{
    content:'?';
    font-weight: bold;
    color:#fff;
}

.help-tip:hover p{
    display:block;
    transform-origin: 100% 0%;

    -webkit-animation: fadeIn 0.3s ease-in-out;
    animation: fadeIn 0.3s ease-in-out;

}

.help-tip p{    /* The tooltip */
    display: none;
    text-align: left;
    background-color: #1E2021;
    padding: 10px;
    width: 300px;
    position: absolute;
    border-radius: 3px;
    box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
    /*right: -4px;*/
    left: -4px;
    color: #FFF;
    font-size: 13px;
    line-height: 1.4;
    z-index: 1;
}

.help-tip p:before{ /* The pointer of the tooltip */
    position: absolute;
    content: '';
    width:0;
    height: 0;
    border:6px solid transparent;
    border-bottom-color:#1E2021;
    /*right:10px;*/
    left:10px;
    top:-12px;
}

.help-tip p:after{ /* Prevents the tooltip from being hidden */
    width:100%;
    height:40px;
    content:'';
    position: absolute;
    top:-40px;
    left:0;
}

/* CSS animation */

@-webkit-keyframes fadeIn {
    0% { 
        opacity:0; 
        transform: scale(0.6);
    }

    100% {
        opacity:100%;
        transform: scale(1);
    }
}

@keyframes fadeIn {
    0% { opacity:0; }
    100% { opacity:100%; }
}
</style>
