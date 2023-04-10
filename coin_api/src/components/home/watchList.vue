<template>
    <div
          class="max-w-md mx-auto bg-white shadow-lg rounded-lg overflow-hidden w-96 h-full"
        >
          <div class="flex items-center px-6 py-3 bg-gray-900">
            <h2 class="text-lg text-white font-semibold">İzleme Listesi</h2>
          </div>
          <div class="px-6 py-4">
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-semibold">Bitcoin</h3>
              <p class="text-gray-600">$61,345.00</p>
            </div>
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-semibold">Ethereum</h3>
              <p class="text-gray-600">$2,338.22</p>
            </div>
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-semibold">Binance Coin</h3>
              <p class="text-gray-600">$321.23</p>
            </div>
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-semibold">Cardano</h3>
              <p class="text-gray-600">$1.20</p>
            </div>
            <div class="flex justify-between items-center mb-4">
              <h3 class="text-lg font-semibold">XRP</h3>
              <p class="text-gray-600">$0.60</p>
            </div>
          </div>
        </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import axios from 'axios';
</script>