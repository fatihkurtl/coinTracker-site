<template>
  <div>
    <!-- Hero section.vue -->
    <HeroSection />

    <!-- Coin section.vue -->
    <CoinSection />

    <!-- Admin posts.vue -->
    <Posts />

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-3">
      <div class="flex flex-wrap -mx-4">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-3">
          <div class="flex flex-wrap -mx-4">
            <div class="w-full lg:w-2/3 px-4">
              <div class="flex flex-wrap -mx-4">
                <div class="w-full lg:w-2/3 px-4 text-center">
                  <Weather />
                </div>
                <div class="w-full lg:w-1/3 px-4 text-center">
                  <Visitors />
                </div>
              </div>
            </div>
            <div class="w-full lg:w-1/3 px-4">
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--news.vue -->
    <News />
  </div>
</template>

<script setup>
import HeroSection from "../components/home/heroSection.vue";
import CoinSection from "../components/home/coinSection.vue";
import Posts from "../components/home/posts.vue";
import News from "../components/home/news.vue";
import Weather from "../components/home/weather.vue";
import Visitors from "../components/home/visitors.vue";
</script>
