<template>
  <div id="app">
    <router-view></router-view>
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
</script>

<style>
</style>
