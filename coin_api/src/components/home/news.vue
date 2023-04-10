<template>
  <div class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="lg:text-center">
        <h2
          class="text-base text-indigo-600 font-semibold tracking-wide uppercase"
        >
          Haberler
        </h2>
        <p
          class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl"
        >
          En Son Haberler
        </p>
        <p class="mt-4 max-w-2xl text-xl text-gray-500 lg:mx-auto">
          Yeni haberleri, gelişmeleri ve analizleri buradan takip edebilirsiniz.
        </p>
      </div>
      <div class="mt-20">
        <div class="sm:flex sm:flex-wrap">
          <div v-for="i in news" :key="i.id" class="sm:w-1/3 mb-4 px-2">
            <div
              class="h-full border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden"
            >
              <img
                class="lg:h-48 md:h-36 w-full object-cover object-center"
                :src="i.imageurl"
                alt=""
              />
              <div class="p-6">
                <h2 class="text-2xl font-bold leading-8 tracking-tight mb-3">
                  <a :href="i.guid" target="_blank" class="hover:underline">{{ i.title }}</a>
                </h2>
                <p class="leading-relaxed mb-3">{{ i.body }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "news",
  data: () => ({
    news: [],
    errors: [],
  }),
  created() {
    axios
      .get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
      .then((response) => {
        this.news = response.data.Data.slice(0, 9);
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>
