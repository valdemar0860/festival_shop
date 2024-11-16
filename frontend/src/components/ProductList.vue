<template>
    <div>
      <h2>Product List</h2>
      <ul>
        <li v-for="product in products" :key="product.id">
          <h3>{{ product.name }}</h3>
          <p>{{ product.description }}</p>
          <p>Price: {{ product.price }}</p>
          <img :src="product.image_url" alt="Product Image" />
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { fetchProducts } from '../utils/api';
  
  export default {
    name: 'ProductList',
    data() {
      return {
        products: []
      };
    },
    async mounted() {
      try {
        this.products = await fetchProducts();
      } catch (error) {
        console.error("Error loading products:", error);
      }
    }
  };
  </script>
  
  <style scoped>
  h2 {
    color: #333;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
  }
  img {
    max-width: 100px;
    height: auto;
  }
  </style>
  