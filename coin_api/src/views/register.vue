<template>
  <div class="bg-white rounded-lg shadow-lg p-8 max-w-sm mx-auto mt-24">
    <Toast v-if="warning == true" type="warning">
      <span class="text-red-700"
        >Bu kullanıcı adı ya da email zaten kullanılıyor!!!</span
      >
    </Toast>
    <Toast v-if="warning == false" type="success">
      <span class="text-green-600">Başarıyla kayıt oldunuz</span>
    </Toast>
    <h2 class="text-2xl font-bold mb-6 text-gray-900">Kayıt ol</h2>
    <form @submit.prevent="doRegister">
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="name">
          Ad Soyad
        </label>
        <input
          v-model="userData.fullName"
          class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="name"
          type="text"
          placeholder="Örnek Örnekoğlu"
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="email">
          E-posta adresi
        </label>
        <input
          v-model="userData.email"
          class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="email"
          type="email"
          placeholder="örnek@example.com"
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="username">
          Kullanıcı Adı
        </label>
        <input
          v-model="userData.userName"
          class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="username"
          type="text"
          placeholder="kullanıcıAdı"
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="password">
          Parola
        </label>
        <input
          v-model="userData.password"
          class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="password"
          type="password"
          placeholder="********"
        />
      </div>
      <div class="flex items-center justify-between">
        <button
          class="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
        >
          Kayıt Ol
        </button>
        <router-link  :to="{ name: 'Forgot Password'}"
          class="inline-block align-baseline font-bold text-sm text-indigo-500 hover:text-indigo-800"
        >
        Parolanızı mı unuttunuz?"
        </router-link>
      </div>
    </form>
  </div>
  <br />
</template>

<script setup>  
import { ref, reactive } from "vue";
import { appAxios } from "@/utils/appAxios.js";
import { useRoute, useRouter } from "vue-router";
import { Toast } from "flowbite-vue";

const router = useRouter();

const userData = reactive({
  fullName: null,
  email: null,
  userName: null,
  password: null,
});

const warning = ref();

const doRegister = () => {
  appAxios.post("/register", userData).then((save_response) => {
    console.log(save_response.data.info);
    save_response.status == 203
      ? (warning.value = true)
      : (warning.value = false);
  });
  setTimeout(() => {
    warning.value == false
      ? router.push({ name: "Login" })
      : (warning.value = true);
    warning.value = null;
  }, 4000);
};
</script>
