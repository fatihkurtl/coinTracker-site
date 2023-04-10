<template>
  <div class="bg-blue-300 rounded-lg shadow-lg p-6 max-h-56 mr-56">
    <h3 class="text-xl font-medium mb-4">Hava Durumu</h3>
    <div v-if="loading" class="text-xl font-medium mb-4">Yükleniyor...</div>
    <div v-else class="flex items-center justify-center mb-6">
      <div class="text-5xl font-bold text-gray-800 mr-2">{{ temp }}°C</div>
      <div>
        <!-- <img
          src="https://www.weatherbit.io/static/img/icons/r01d.png"
          alt="hava durumu ikonu"
          class="w-16"
        /> -->
      </div>
    </div>
    <div class="text-lg text-gray-800 mb-4">{{ cityName }}</div>
    <div class="text-sm text-gray-600">{{ description }}</div>
  </div>
</template>

<script>
  import axios from "axios";

export default {
  data() {
    return {
      loading: true,
      cityName: "",
      temp: 0,
      humidity: 0,
      description: "",
    };
  },
  mounted() {
    this.getLocation();
  },
  methods: {
    async getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          this.getWeather,
          this.showError
        );
      } else {
        alert("Tarayıcınız konum paylaşımını desteklemiyor.");
      }
    },
    async getWeather(position) {
      const { latitude, longitude } = position.coords;
      const apiKey = "c20b811cd65bc004f2bde33a7097a756";
      const url = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${apiKey}&units=metric`;
      const response = await axios.get(url);
      this.cityName = response.data.name;
      this.temp = response.data.main.temp;
      this.humidity = response.data.main.humidity;
      this.description = response.data.weather[0].description;
      this.loading = false;
    },
    showError(error) {
      switch (error.code) {
        case error.PERMISSION_DENIED:
          alert("Konum paylaşımı engellendi.");
          break;
        case error.POSITION_UNAVAILABLE:
          alert("Konum bilgisi alınamadı.");
          break;
        case error.TIMEOUT:
          alert("İstek zaman aşımına uğradı.");
          break;
        default:
          alert("Bilinmeyen bir hata oluştu.");
          break;
      }
    },
  },
};
</script>
