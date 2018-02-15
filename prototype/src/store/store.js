import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex) // only required if you're using modules.

const store = new Vuex.Store({
  state: {
    searchresults: [
      { text: 'WOW.' },
      { text: 'SO.' },
      { text: 'MUCH.' },
      { text: 'FUN.' }
    ]
  }
  // mutations: {
  //   'ADD_TODO': function (state, result) {
  //     state.searchresults.push(result)
  //   },
  //   'CLEAR_TODOS': function (state) {
  //     const searchResults = state.searchresults
  //     searchResults.splice(0, searchResults.length)
  //   }
  // },
  // actions: {
  //   addResult (store, result) {
  //     store.commit('ADD_TODO', result)
  //   },
  //   clearResults (store) {
  //     store.commit('CLEAR_TODOS')
  //   }
  // }
})

export default store
