<template>
  <div class="top-left">
    <router-link to="/">
      <img src="./../assets/transparentGovernance2.png" id = "logo">
    </router-link>
    <input id="input-box">
    <div id = "results">
      <search-result-list id="result-view"></search-result-list>
    </div>
  </div>
</template>

<script>
import SearchResultList from './SearchResultList.vue'

export default{
  components: {
    SearchResultList
  }
}

</script>

<style>
#input-box{
  width: 300px;
}

#result-view{
  position: absolute;
  top: 10%;
  left: 15%;
}
</style>
