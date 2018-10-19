<template>
  <div id="app">
    <my-Header></my-Header>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'


export default {
  name: 'App',
  data () {
    return {
      msg: '这是一个内容组件'
    }
  },
  components: {
    'my-Header': Header
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 16px;
}
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body{
  min-width: 1650px;
}
ul,ol{
  list-style: none;
}
a{
  color: #fff;
  text-decoration: none;
}
img{
  width: 100%;
  height: 100%;
}
input{
  border: none;
  outline: none;
}
</style>
