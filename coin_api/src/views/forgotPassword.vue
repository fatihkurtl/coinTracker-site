<template>
  <div
    class="bg-gray-50 min-h-screen flex flex-col justify-center py-12 sm:px-6 lg:px-8 mt-2"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
        Şifrenizi Sıfırlayın
      </h2>
      <p class="mt-2 text-center text-sm text-gray-600">
        Kendi e-posta adresinize şifre sıfırlama talimatları almak için aşağıya
        bilgilerinizi girin.
      </p>
    </div>

    <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <div class="text-center">
          <Toast v-if="warning == false" type="warning">
            <span class="text-red-600">Şifreler uyuşmuyor</span>
          </Toast>
          <Toast v-if="warning == true" type="success">
            <span class="text-green-600">Şifreniz başarıyla değiştirildi</span>
          </Toast>
        </div>
        <form class="space-y-6" @submit.prevent="forgotPassword">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">
              E-posta adresi
            </label>
            <div class="mt-1">
              <input
                v-model="state.email"
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
              Yeni şifre
            </label>
            <div class="mt-1">
              <input
                v-model="state.password"
                id="password"
                name="password"
                type="password"
                autocomplete="new-password"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <label
              for="password_confirm"
              class="block text-sm font-medium text-gray-700"
            >
              Yeni şifreyi doğrula
            </label>
            <div class="mt-1">
              <input
                v-model="state.password_confirm"
                id="password_confirm"
                name="password_confirm"
                type="password"
                autocomplete="new-password"
                required
                class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                <!-- Heroicon name: solid/lock-closed -->
                <svg
                  class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                  aria-hidden="true"
                >
                  <path
                    fill-rule="evenodd"
                    d="M3.293 14.707a1 1 0 010-1.414L8.586 8 3.293 2.707a1 1 0 111.414-1.414l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414 0z"
                    clip-rule="evenodd"
                  />
                </svg>
              </span>
              Şifremi sıfırla
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, reactive } from "vue";
import { appAxios } from "../utils/appAxios";
import { Toast } from "flowbite-vue";

const state = reactive({
  email: "",
  password: "",
  password_confirm: "",
});

const warning = ref();

const forgotPassword = async () => {
  if (state.password == state.password_confirm) {
    warning.value = true;
    try {
      const response = await appAxios.post("/forgot_password", {
        email: state.email,
        password: state.password,
        password_confirm: state.password_confirm,
      });
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  } else {
    warning.value = false;
  }
};
</script>
