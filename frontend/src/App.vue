<template>
  <div id="app">
    <Header />
    <ProductList />
  </div>
</template>

<script>
import Header from './components/Header.vue';
import ProductList from './components/ProductList.vue';

export default {
  name: 'App',
  components: {
    Header,
    ProductList
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
