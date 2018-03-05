<template>
  <div class="top-left">
    <router-link to="/">
      <img src="./../assets/transparentGovernance2.png" id = "logo">
    </router-link>
    <input id="input-box" v-model="searchBoxText">
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      searchBoxText: ''
    }
  },

  created () {
    this.searchBoxText = this.$parent.inputField.search
  }
}

</script>

<style>
#input-box{
  position:absolute;
  width: 500px;
  border-radius: 3px;
  top: 30px;
  height: 35px;
}
</style>
