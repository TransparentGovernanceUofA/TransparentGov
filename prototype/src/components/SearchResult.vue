<template>
  <p>
    {{ searchresult.text }}
  </p>
</template>

<script>
export default {
  props: ['searchresult']
}
</script>

<style>
p{
  font-size: 30px;
  border-bottom: 1px solid black;
}
</style>
