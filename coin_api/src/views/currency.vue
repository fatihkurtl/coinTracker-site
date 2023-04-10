<template>
  <div class="max-w-xl mx-auto py-10 mt-16">
    <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-2xl font-bold">Döviz Kurları</h2>
        <div>
          <span v-if="loading" class="mr-2">Yükleniyor...</span>
          <button
            @click="refreshData"
            :disabled="loading"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            <i class="fa fa-refresh mr-2"></i> Yenile
          </button>
        </div>
      </div>
      <div class="overflow-x-auto">
        <table class="table-auto w-full">
          <thead>
            <tr>
              <th class="px-4 py-2">Para Birimi</th>
              <th class="px-4 py-2">Alış</th>
              <th class="px-4 py-2">Satış</th>
              <th class="px-4 py-2">Değişim</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(currency, index) in currencies" :key="index">
              <td class="border px-4 py-2">{{ currency.Isim }}</td>
              <td class="border px-4 py-2">{{ currency.ForexBuying }}</td>
              <td class="border px-4 py-2">{{ currency.ForexSelling }}</td>
              <td
                class="border px-4 py-2"
                :class="getChangeClass(currency.CrossRateUSD)"
              >
                {{ '%' + currency.CrossRateUSD }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>

import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  name: "DovizKurlari",
  setup() {
    const loading = ref(false);
    const currencies = ref([]);
    const refreshData = async () => {
        loading.value = true;
        try {
        const response = await axios.get(
          "http://hasanadiguzel.com.tr/api/kurgetir"
        );
        currencies.value = response.data.TCMB_AnlikKurBilgileri
      } catch (error) {
        console.error(error);
      }
      loading.value = false;
    };

    const getChangeClass = (change) => {
      return {
        "text-green-600": change > 0,
        "text-red-600": change < 0,
      };
    };

    onMounted(() => {
      refreshData();
    });

    return {
      loading,
      currencies,
      refreshData,
      getChangeClass,
    };
  },
};
</script>
