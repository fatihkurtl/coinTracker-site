<template>
  <br />
  <!-- Contact page -->
  <div class="bg-gray-100 min-h-screen py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <h2
        class="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-4xl"
      >
        Bize Ulaşın
      </h2>
      <p class="mt-4 text-lg text-gray-500">
        Eğer herhangi bir sorunuz veya yorumunuz varsa, lütfen aşağıdaki formu
        doldurun ve en kısa sürede size dönüş yapacağız.
      </p>
      <div class="mt-9 grid grid-cols-1 gap-y-6 sm:grid-cols-2 sm:gap-x-8">
        <!-- Contact form -->
        <form class="space-y-6" @submit.prevent="sendContact">
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700">
              Ad Soyad
            </label>
            <div class="mt-1">
              <input
                v-model="contactData.name"
                id="name"
                name="name"
                type="text"
                autocomplete="name"
                required
                class="py-3 px-4 block w-full shadow-sm text-gray-900 focus:ring-blue-500 focus:border-blue-500 border-gray-300 rounded-md"
              />
            </div>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">
              Email
            </label>
            <div class="mt-1">
              <input
                v-model="contactData.email"
                id="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="py-3 px-4 block w-full shadow-sm text-gray-900 focus:ring-blue-500 focus:border-blue-500 border-gray-300 rounded-md"
              />
            </div>
          </div>
          <div>
            <label for="phone" class="block text-sm font-medium text-gray-700">
              Telefon Numarası
            </label>
            <div class="mt-1">
              <input
                v-model="contactData.phone"
                id="phone"
                name="phone"
                type="text"
                autocomplete="tel"
                class="py-3 px-4 block w-full shadow-sm text-gray-900 focus:ring-blue-500 focus:border-blue-500 border-gray-300 rounded-md"
              />
            </div>
          </div>
          <div>
            <label
              for="message"
              class="block text-sm font-medium text-gray-700"
            >
              Mesajınız
            </label>
            <div class="mt-1">
              <textarea
                v-model="contactData.message"
                id="message"
                name="message"
                rows="4"
                class="py-3 px-4 block w-full shadow-sm text-gray-900 focus:ring-blue-500 focus:border-blue-500 border-gray-300 rounded-md"
              ></textarea>
            </div>
          </div>
          <div>
            <button
              type="submit"
              class="py-3 px-4 bg-blue-500 hover:bg-blue-600 text-white font-bold rounded-md shadow-md transition duration-300"
            >
              Gönder
            </button>
          </div>
        </form>
        <!-- Contact alert -->
        <div class="space-y-4 mt-48 ml-16">
          <div>
            <Toast v-if="contactAlert" type="success">
              <span class="text-green-600"
                >Mesajınız Alındı. En kısa sürede size dönüş yapacağız.
                <i class="far fa-smile" style="font-size: 16px"></i
              ></span>
            </Toast>
            <Toast v-if="contactAlert == null" type="success">
              <span class="text-red-600"
                >Mesaj gönderilemedi. Lütfen daha sonra tekrar deneyin.
                <i class="far fa-frown" style="font-size: 16px"></i
              ></span>
            </Toast>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>  
import { appAxios } from "@/utils/appAxios";
import { ref, reactive } from "vue";
import { useAuthStore } from "@/store/auth";
import { Toast } from "flowbite-vue";

const authStore = useAuthStore();

const contactData = reactive({
  user: authStore.getCurrentUser ? authStore.getCurrentUser : null,
  name: null,
  email: null,
  phone: null,
  message: null,
});

const contactAlert = ref(false);

const sendContact = async () => {
  try {
    const response = await appAxios.post("/contact", contactData);
    contactData.name = null;
    contactData.email = null;
    contactData.phone = null;
    contactData.message = null;
    response.status === 201 ? (contactAlert.value = true) : null;
    setTimeout(() => {
      contactAlert.value = false;
    }, 5000);
  } catch (error) {
    console.log(error);
  }
};
</script>
