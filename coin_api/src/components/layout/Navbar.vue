<template>
  <nav class="bg-gray-800">
    <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <div class="flex-shrink-0 flex items-center">
          <a
            href="#"
            @click="scrollToTop"
            class="font-bold text-white text-2xl"
          >
            CoinTracker
          </a>
        </div>
        <div class="absolute inset-y-0 right-0 flex items-center sm:hidden">
          <button
            type="button"
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
            aria-controls="mobile-menu"
            aria-expanded="false"
          >
            <span class="sr-only">Open main menu</span>
            <svg
              class="block h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
            <svg
              class="hidden h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <div class="hidden sm:block sm:ml-6">
          <div class="flex space-x-4">
            <router-link
              @click="scrollToTop"
              :to="{ name: 'Home' }"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
              >Anasayfa</router-link
            >
            <!---->
            <div class="relative inline-block text-left">
              <button
                @click="dropdownFunc"
                type="button"
                class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium focus:outline-none"
                id="dropdown-menu"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Piyasalar
              </button>
              <div
                v-if="dropdown == true"
                class="absolute right-0 z-50 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
                role="menu"
                aria-orientation="vertical"
                aria-labelledby="dropdown-menu"
              >
                <router-link
                  :to="{ name: 'Coins' }"
                  href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  role="menuitem"
                  >Kripto</router-link
                >
                <router-link
                  :to="{ name: 'Currency' }"
                  href="#"
                  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  role="menuitem"
                  >Döviz Kurları</router-link
                >
              </div>
            </div>

            <!---->
            <router-link
              @click="scrollToTop"
              :to="{ name: 'About' }"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
              >Hakkımızda</router-link
            >
            <router-link
              @click="scrollToTop"
              :to="{ name: 'Contact' }"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
              >İletişim</router-link
            >
            <router-link
              v-if="!currentUser"
              :to="{ name: 'Login' }"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
              >Giriş yap</router-link
            >
            <router-link
              v-if="!currentUser"
              :to="{ name: 'Register' }"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
              >Kayıt ol</router-link
            >
            <router-link
              v-if="currentUser"
              @click="authStore.handleLogout"
              :to="{ name: 'Login' }"
              class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
              >Çıkış yap</router-link
            >
            <div
              v-if="authStore.admin == true && authStore.token"
              class="relative inline-block text-left"
            >
              <div>
                <button
                  @click="adminNav"
                  type="button"
                  class="bg-gray-900 rounded-md w-full px-3 py-2 text-sm font-medium text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white"
                  id="menu-button"
                  aria-expanded="true"
                  aria-haspopup="true"
                >
                  <span class="material-symbols-outlined">
                    admin_panel_settings
                  </span>
                  <svg
                    class="text-gray-400 group-hover:text-gray-500 transition ease-in-out duration-150 h-5 w-5 group-hover:-rotate-180"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 011.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </button>
              </div>

              <div
                v-if="isOpen == true"
                class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5"
              >
                <div
                  class="py-1"
                  role="menu"
                  aria-orientation="vertical"
                  aria-labelledby="menu-button"
                  tabindex="-1"
                >
                  <router-link
                    :to="{ name: 'Admin Share Post' }"
                    class="text-black hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
                    >Share Post</router-link
                  >
                  <router-link
                    :to="{ name: 'Member List' }"
                    class="text-black hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
                    >Member List</router-link
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="sm:hidden" id="mobile-menu">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <router-link
          :to="{ name: 'Home' }"
          class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
          >Home</router-link
        >
        <router-link
          :to="{ name: 'Coins' }"
          class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
          >Coins</router-link
        >
        <router-link
          :to="{ name: 'About' }"
          class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
          >About</router-link
        >
        <router-link
          :to="{ name: 'Contact' }"
          class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
          >Contact</router-link
        >
        <a
          href="#"
          class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium"
          >Contact</a
        >
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "@/store/auth";
import { ref } from "vue";

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();
const currentUser = authStore.getCurrentUser;

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
};
const isOpen = ref(false);

const adminNav = () => {
  isOpen.value == false ? (isOpen.value = true) : (isOpen.value = false);
};

const dropdown = ref(false);

const dropdownFunc = () => {
  dropdown.value == false ? (dropdown.value = true) : (dropdown.value = false);
};
</script>

<style>
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 9999;
}
</style>
