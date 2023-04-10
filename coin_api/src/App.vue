<template>
  <Navbar />
  <router-view></router-view>
  <Footer />
</template>

<script setup>
import Navbar from "@/components/layout/Navbar.vue";
import Footer from "@/components/layout/Footer.vue";
</script>
