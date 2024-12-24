<template>
    <div>
        <h1>Products</h1>
        <div v-for="product in products" :key="product.id">
            <p>{{ product.name }}</p>
            <p>{{ product.price }} USD</p>
        </div>
    </div>
</template>

<script>
    import { fetchProducts } from '../utils/api';

    export default {
        data() {
        return {
            products: [],
        };
        },
            async created() {
            this.products = await fetchProducts();
        },
    };
</script>
