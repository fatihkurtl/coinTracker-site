<template>
  <div class="flex flex-col mt-24 mb-6">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div
          class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg"
        >
          <table class="min-w-full divide-y divide-gray-900">
            <thead class="bg-gray-200">
              <tr>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  ID
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Ad Soyad
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Kullanıcı Adı
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  E-posta
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Kayıt Tarihi
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Delete</span>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="user in users" :key="user.id">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ user.id }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ user.fullName }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ user.userName }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ user.email }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ user.registerTime }}
                </td>
                <td
                  class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                >
                  <button
                    @click="deleteUser(user.id)"
                    class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  >
                    Sil
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { appAxios } from "@/utils/appAxios";
import { ref, onMounted } from "vue";
import { useAuthStore } from "@/store/auth";

const users = ref();

const admin = useAuthStore();

const warning = ref();

onMounted(() => {
  appAxios
    .get(`/get_users/${admin.isAdmin}`)
    .then((response) => {
      users.value = response.data.users;
    })
    .catch((error) => {
      console.log(error);
    });
});

const deleteUser = (id) => {
  if (admin.isAdmin) {
    appAxios
      .delete(`/delete_user/${id}`)
      .then((response) => {
        console.log(response.status);
        if (response.status == 201) {
          alert("Kullanıcı silindi!");
          window.location.reload();
        }
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    alert("Bu işlemi yapmaya yetkiniz yok!");
  }
};
</script>
