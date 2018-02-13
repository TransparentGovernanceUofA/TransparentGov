<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <router-view/> -->
    <img src="./assets/transparentGovernance.png">
    <search-box></search-box>
    <search-result-list></search-result-list>
  </div>
</template>

<script>
import SearchResultList from './components/SearchResultList.vue'
import SearchBox from './components/SearchBox.vue'
export default {
  components: {
    SearchBox,
    SearchResultList
  }
}
// export default {
//   name: 'App'
// }
</script>

<style>
#app {
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;*/
  text-align: center;
  /*color: #2c3e50;
  margin-top: 60px;*/
}
</style>
