<template>
  <div class="top-left">
    <router-link to="/">
      <img src="./../assets/transparentGovernance2.png" id = "logo">
    </router-link>
    <input id="input-box" v-model="searchBoxText" v-on:keyup.enter="goToResults()">
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      searchBoxText: '',
      inputField: {
        search: ''
      }
    }
  },

  created () {
    this.searchBoxText = this.$parent.inputField.search
  },
  methods: {
    goToResults () {
      // console.log('TESTING')
      // this.inputField.search = this.searchBoxText
      // let inputField = this.inputField
      // console.log(inputField)

      // router.push to a different path works but pushing to the same path wont work for some reason, i know it has some thing to do with how it reuses the components and that it wont reload them
      // this.$router.push({name: 'SearchBox'})
      // this.$router.push({name: 'Result', params: { inputField }})

      this.$parent.inputField.search = this.searchBoxText
      this.$parent.fetchData()
    }
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
