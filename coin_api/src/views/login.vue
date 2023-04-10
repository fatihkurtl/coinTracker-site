<template>
  <div
    class="min-h-screen bg-gray-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
        Hesabınıza giriş yapın
      </h2>
      <p class="mt-2 text-center text-sm text-gray-600">
        Veya 
        <router-link
          :to="{ name: 'Register' }"
          class="font-medium text-indigo-600 hover:text-indigo-500"
        >
        yeni bir hesap oluşturun
        </router-link>
      </p>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <Toast v-if="warning == true" type="warning">
          <span class="text-red-700">{{ msg }}!!!</span>
        </Toast>
        <Toast v-if="warning == false" type="success">
          <span class="text-green-600">{{ msg }}</span>
        </Toast>
        <Toast v-if="warning == 'admin'" type="success">
          <span class="text-green-600"
            >Hoş geldin admin
            <span class="material-symbols-outlined">
              admin_panel_settings
            </span></span
          >
        </Toast>
        <form class="space-y-6" @submit.prevent="doLogin">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">
              E-posta adresi
            </label>
            <div class="mt-1">
              <input
                v-model="userData.email"
                id="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <label
              for="password"
              class="block text-sm font-medium text-gray-700"
            >
              Parola
            </label>
            <div class="mt-1">
              <input
                v-model="userData.password"
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center">
              <input
                id="remember_me"
                name="remember_me"
                type="checkbox"
                class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
              />
              <label for="beni_hatırla" class="ml-2 block text-sm text-gray-900">
                Beni hatırla
              </label>
            </div>

            <div class="text-sm">
              <router-link  :to="{ name: 'Forgot Password' }"
                href="#"
                class="font-medium text-indigo-600 hover:text-indigo-500"
              >
              Parolanızı mı unuttunuz?
              </router-link>
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Giriş yap
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>   
  import { ref, reactive } from "vue";
  import { appAxios } from "@/utils/appAxios.js";
  import { useRoute, useRouter } from "vue-router";
  import { useAuthStore } from "../store/auth";
  import { Toast } from "flowbite-vue";

const authStore = useAuthStore();

const router = useRouter();

const userData = reactive({
  email: null,
  password: null,
});

const warning = ref();
const msg = ref();

const doLogin = () => {
  appAxios.post("/login", userData).then((get_response) => {
    console.log(get_response.status);
    if (get_response.status == 202) {
      if (get_response.data.admin == true) {
        console.log("get_response.data.admin :>> ", get_response.data.admin);
        authStore.isAdmin(get_response.data.admin);
        authStore.saveToken(get_response.data.token);
        authStore.handleLogin(userData.email);
        warning.value = "admin";
      } else if (!get_response.data.admin) {
        authStore.handleLogin(userData.email);
        authStore.saveToken(get_response.data.token);
        warning.value = false;
        msg.value = get_response.data.msg;
      }
    } else if (get_response.status == 204) {
      warning.value = true;
      msg.value = "User Not Found";
    } else if (get_response.status == 203) {
      warning.value = true;
      msg.value = get_response.data.msg;
    }
  });

  setTimeout(() => {
    if (warning.value == false || warning.value == "admin") {
      router.push({ name: "Home" });
    } else {
      warning.value = true;
    }
  }, 3000);
};
</script>
