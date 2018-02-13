<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <router-view/> -->
    <img src="./assets/transparentGovernance.png">
    <search-box @toggleList="toggleList"></search-box>
    <search-result-list v-if='isShown'></search-result-list>
  </div>
</template>

<script>
import SearchResultList from './components/SearchResultList.vue'
import SearchBox from './components/SearchBox.vue'
export default {
  components: {
    SearchBox,
    SearchResultList
  },
  methods: {
    toggleList () {
      this.isShown = !this.isShown
    }
  },
  data: function () {
    return { isShown: false }
  }
}
// export default {
//   name: 'App'
// }
</script>

<style>
#app {
  text-align: center;
  margin-top: 150px;
}
</style>
