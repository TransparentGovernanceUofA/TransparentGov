<template>
<div class="badge align-middle align-text-top align-text-bottom" v-bind:class="[computedStyle,computedPills]">
  {{text}}
  <span class="clickable" v-on:click="emit">x</span>
</div>
</template>

<script>
export default {
  props: ['text', 'type', 'pillStyle', 'pillable'],
  computed: {
    computedStyle: function () {
      return 'badge-' + this.pillStyle
    },
    computedPills: function () {
      return (this.pillable === 'true') ? 'badge-pill' : ''
    }
  },
  methods: {
    emit: function () {
      this.$emit('pill_clicked', this.$el)
    }
  }
}
</script>

<style>
.badge{
  margin-right:5px;
  margin-left:5px;
}

.clickable{
  cursor:pointer;
}
</style>
