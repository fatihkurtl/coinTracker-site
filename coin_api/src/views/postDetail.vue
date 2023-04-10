<template>
  <div
    v-for="post in post_detail"
    :key="post.id"
    class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8 mt-12"
  >
    <div class="bg-white overflow-hidden shadow-xl sm:rounded-lg">
      <div class="bg-white shadow overflow-hidden sm:rounded-lg">
        <img class="w-full h-fit object-cover" :src="`${post.image}`" alt="" />
        <div class="px-4 py-5 sm:p-6">
          <div class="flex items-center mb-4">
            <div
              class="bg-gray-300 w-10 h-10 rounded-full flex-shrink-0 mr-4"
            ></div>
            <div>
              <p class="text-gray-900 leading-none font-medium">
                {{ post.author }}
              </p>
              <p class="text-gray-600 text-sm">{{ post.created_at }}</p>
            </div>
          </div>
          <h1 class="text-2xl leading-7 font-bold text-gray-900">
            {{ post.title }}
          </h1>
          <div class="mt-4 prose prose-sm max-w-none text-gray-800">
            {{ post.content }}
          </div>
        </div>
      </div>
      <div class="bg-gray-200 px-4 py-4 sm:px-6">
        <h3 class="text-lg leading-6 font-medium text-gray-900">Yorumlar</h3>
        <div class="mt-4">
          <div v-if="post_comments" class="mt-4 space-y-4">
            <div v-for="comment in post_comments" :key="comment.id">
              <div class="flex items-center space-x-2">
                <div class="w-10 h-10 rounded-full bg-gray-400"></div>
                <div class="flex-1">
                  <div class="flex items-center justify-between">
                    <h3 class="text-sm font-medium">
                      {{ comment.user.userName }}
                      <button
                        v-if="admin.getAdmin"
                        class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded focus:outline-none focus:shadow-outline"
                        @click="deleteComment(comment.id)"
                        style="font-size: 0.75rem"
                      >
                        Delete
                      </button>
                    </h3>
                    <p class="text-sm text-gray-500">
                      {{ comment.created_at }}
                    </p>
                  </div>
                  <p class="text-sm text-gray-800">{{ comment.content }}</p>
                </div>
              </div>
            </div>
          </div>
          <p v-else class="mt-4 text-sm text-gray-500">Henüz bir yorum yok.</p>
        </div>

        <br /><br />
        <hr />
        <div class="mt-4">
          <form @submit.prevent="addComment">
            <div class="mt-4">
              <label
                for="author"
                class="block text-sm font-medium text-gray-700"
                >Kullanıcı Adı</label
              >
              <input
                v-model="commentData.name"
                type="text"
                name="author"
                id="author"
                autocomplete="given-name"
                required
                class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
              />
            </div>
            <div class="mt-4">
              <label
                for="content"
                class="block text-sm font-medium text-gray-700"
                >Yorum</label
              >
              <textarea
                v-model="commentData.comment"
                name="content"
                id="content"
                rows="3"
                class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                required
              ></textarea>
            </div>
            <div class="mt-4">
              <button
                type="submit"
                class="inline-flex items-center px-4 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Yorum ekle
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";
import { appAxios } from "../utils/appAxios";
import { useRoute } from "vue-router";
import { useAuthStore } from "@/store/auth";

const admin = useAuthStore();

const route = useRoute();
const post = route.params.id;
// console.log("post :>> ", post);

const post_detail = ref(null);
const getPost = async () => {
  const response = await appAxios.get(`/post_detail/${post}`);
  post_detail.value = response.data;
};
getPost();

const commentData = reactive({
  name: null,
  comment: null,
});

const addComment = async () => {
  if (commentData.name && commentData.comment) {
    const response = await appAxios
      .post(`/save_comment/${post}/${user.getCurrentUser}`, commentData)
      .then((response) => {
        console.log(response);
        window.location.reload();
      });
  } else {
    alert("Lütfen tüm alanları doldurunuz.");
  }
};

const post_comments = ref(null);
const getPostComments = async () => {
  const response = await appAxios
    .get(`/get_comments/${post}`)
    .then((response_comment) => {
      post_comments.value = response_comment.data.comments;
    });
};
getPostComments();

const deleteComment = async (id) => {
  const response = await appAxios
    .post(`/delete_comment/${id}`, {})
    .then((response) => {
      if (response.status == 201) {
        alert("Yorum silindi.");
        window.location.reload();
      } else {
        alert("Yorum silinemedi.");
      }
    });
};
</script>
