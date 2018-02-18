<template>
  <p>
    {{ searchresult.id }}
    <br>
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
  font-size: 20 px;
  border-bottom: 1px solid black;
}
</style>
