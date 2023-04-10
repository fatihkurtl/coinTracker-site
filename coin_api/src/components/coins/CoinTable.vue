<template>
  <br /><br />
  <div class="flex flex-col mt-6">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div
          class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg"
        >
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-2xl font-medium text-gray-500 uppercase tracking-wider"
                >
                  Koin
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-2xl font-medium text-gray-500 uppercase tracking-wider"
                >
                  Fiyat
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-2xl font-medium text-gray-500 uppercase tracking-wider"
                >
                  Değişim
                </th>

                <th
                  scope="col"
                  class="px-6 py-3 text-left text-2xl font-medium text-gray-500 uppercase tracking-wider"
                >
                  Piyasa Değeri
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <div class="flex justify-end mb-4">
                    <button
                      @click="changeCurrency"
                      class="flex items-center text-white bg-indigo-500 hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 px-4 py-2 rounded-3xl shadow-sm"
                    >
                      <span v-if="currency == 'try'" class="material-symbols-outlined">
                        currency_exchange
                      </span>
                      <span v-if="currency == 'usd'" class="material-symbols-outlined">
                        currency_lira
                      </span>
                    </button>
                  </div>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="coin in coins" :key="coin.id">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                      <img
                        class="h-10 w-10 rounded-full"
                        :src="coin.image"
                        alt=""
                      />
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">
                        {{ coin.name }}
                      </div>
                      <div class="text-sm text-gray-500">
                        {{ coin.symbol.toUpperCase() }}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">
                    <div v-if="currency == 'try'">₺ {{ coin.current_price }}</div><div v-else>$ {{ coin.current_price }}</div>
                  </div>
                  <div class="text-sm text-gray-500">
                    {{
                      (
                        (coin.price_change_24h / coin.current_price) *
                        100
                      ).toFixed(2)
                    }}%
                  </div>
                </td>
                <td class="px-6 py-4 flex flex-end whitespace-nowrap">
                  <span
                    v-if="coin.price_change_percentage_24h.toFixed(2) < 0"
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800"
                  >
                    {{ coin.price_change_percentage_24h.toFixed(2) }}%
                  </span>
                  <span
                    v-else
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"
                  >
                    {{ coin.price_change_percentage_24h.toFixed(2) }}%
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                 <div v-if="currency == 'try'">₺ {{ coin.market_cap }}</div><div v-else>$ {{ coin.market_cap }}</div> 
                </td>
              </tr>
            </tbody>
          </table>
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
    const currency = ref("usd");

    const getCoinsData = async () => {
      try {
        const response = await axios.get(
          `https://api.coingecko.com/api/v3/coins/markets?vs_currency=${currency.value}&order=market_cap_desc&page=1&sparkline=false`
        );
        coins.value = response.data;
      } catch (error) {
        console.log(error);
      }
    };

    const changeCurrency = () => {
      currency.value = currency.value === "usd" ? "try" : "usd";
      getCoinsData();
    };

    onMounted(() => {
      getCoinsData();
    });

    return {
      coins,
      currency,
      changeCurrency,
    };
  },
};
</script>