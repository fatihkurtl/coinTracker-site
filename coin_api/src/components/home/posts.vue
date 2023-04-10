<template>
  <div class="bg-gray-100">
    <div class="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8">
      <div class="sm:text-center lg:text-left">
        <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
          En Son Gönderiler
        </h2>
        <p class="mt-4 text-lg text-gray-500">
          İşte topluluğumuzdan en son gönderiler.
        </p>
        <div class="mt-10 grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          <!-- Post 1 -->
          <div
            v-for="post in posts"
            :key="post.id"
            class="bg-white overflow-hidden shadow rounded-lg"
          >
            <img class="w-full" :src="`${post.image}`" alt="" />
            <div class="p-5">
              <h3 class="text-lg font-medium text-gray-900">
                {{ post.title }}
              </h3>
              <p class="mt-2 text-gray-500">
                {{ post.content }}
              </p>
              <div class="mt-4">
                <button
                  type="submit"
                  @click="goDetail(post.id)"
                  class="text-base font-medium text-indigo-500 hover:text-indigo-400"
                >
                  Read more →
                </button>
              </div>

              <div class="mt-4" v-if="admin.getAdmin">
                <button
                  type="submit"
                  @click="deletePost(post.id)"
                  class="text-base font-medium text-red-500 hover:text-red-900"
                >
                  Postu Sil
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { appAxios } from "../../utils/appAxios";
import { ref, reactive, onMounted } from "vue";
import { useAuthStore } from "@/store/auth";
import { useRouter, useRoute } from "vue-router";

const route = useRoute();
const router = useRouter();
const goDetail = (id) => {
  router.push({ name: "PostDetail", params: { id } });
};

const admin = useAuthStore();

const posts = ref([]);

onMounted(async () => {
  appAxios
    .get(`/get_post/${admin.getAdmin}`)
    .then((response) => {
      posts.value = response.data.posts;
    })
    .catch((error) => {
      console.log("error :>> ", error);
    });
});

const deletePost = (id) => {
  appAxios
    .post(`delete_post/${id}`, {})
    .then((response) => {
      if (response.status === 201) {
        alert("Post Silindi");
        window.location.reload();
      } else {
        alert("Post Silinemedi");
      }
    })
    .catch((error) => {
      console.log("error :>> ", error);
    });
};
</script>
