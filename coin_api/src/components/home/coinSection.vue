<template>
  <div class="bg-white">
    <div class="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8">
      <div class="sm:text-center lg:text-left">
        <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
          En İyi Kripto Paralar
        </h2>
        <p class="mt-4 text-lg text-gray-500">
          Şu anda piyasada en iyi coinlerden bazıları şunlardır.
        </p>
        <div class="mt-10">
          <div class="flex justify-center">
          <div
            v-for="coin in coins"
            :key="coin.id"
            class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3"
          >
            <div class="bg-gray-100 overflow-hidden shadow rounded-lg w-96">
              <div class="p-5">
                <div class="flex items-center">
                  <div class="flex-shrink-0">
                    <img
                      class="h-12 w-12"
                      :src="coin.image"
                      alt="Bitcoin"
                    />
                  </div>
                  <div class="ml-5 w-0 flex-1 items">
                    <dl>
                      <dt class="text-sm font-medium text-gray-500 truncate">
                        {{ coin.name }} ({{ coin.symbol.toUpperCase() }})
                      </dt>
                      <dd>
                        <div class="text-lg font-medium text-gray-900">
                          ${{ coin.current_price }}
                        </div>
                      </dd>
                      <dd class="mt-2">
                        <div v-if="coin.price_change_24h.toFixed(2) < 0" class="text-sm font-medium text-red-600">
                          <span class="sr-only">Increased by</span>
                          {{
                            (
                              (coin.price_change_24h / coin.current_price) *
                              100
                            ).toFixed(2)
                          }}%
                        </div>
                        <div v-else class="text-sm font-medium text-green-600">
                          <span class="sr-only">Increased by</span>
                          {{
                            (
                              (coin.price_change_24h / coin.current_price) *
                              100
                            ).toFixed(2)
                          }}%
                        </div>
                      </dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { ref, onMounted } from "vue";
  import axios from "axios";

export default {
  setup() {
    const coins = ref([]);

    const getCoinsData = async () => {
      try {
        const response = await axios.get(
          "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&page=1&sparkline=false"
        );
        coins.value = response.data.slice(0, 3);
      } catch (error) {
        console.log(error);
      }
    };

    onMounted(() => {
      getCoinsData();
    });

    return {
      coins,
      getCoinsData,
    };
  },
};
</script>
