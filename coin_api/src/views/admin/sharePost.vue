<template>
  <div
    class="flex flex-col items-center justify-center h-auto bg-gray-700 mt-16"
  >
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg p-6">
      <h2 class="text-xl font-bold mb-4">New Post</h2>
      <form @submit.prevent="sharePost">
        <div class="mb-4">
          <label for="title" class="block text-gray-700 font-bold mb-2"
            >Title:</label
          >
          <input
            v-model="postData.title"
            type="text"
            name="title"
            id="title"
            class="w-full border border-gray-400 p-2 rounded-md"
            required
          />
        </div>
        <div class="mb-4">
          <label for="content" class="block text-gray-700 font-bold mb-2"
            >Content:</label
          >
          <textarea
            v-model="postData.content"
            name="content"
            id="content"
            rows="5"
            class="w-full border border-gray-400 p-2 rounded-md"
            required
          ></textarea>
        </div>
        <div class="mb-4">
          <label for="image" class="block text-gray-700 font-bold mb-2"
            >Image:</label
          >
          <input
            @change="uploadPhoto"
            type="file"
            name="image"
            id="image"
            class="w-full border border-gray-400 p-2 rounded-md"
          />
        </div>
        <div class="flex justify-end">
          <button
            type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Create
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { appAxios } from "../../utils/appAxios";
import { useAuthStore } from "@/store/auth";


const admin = useAuthStore();

const postData = ref({
  admin: admin.getAdmin,
  title: null,
  content: null,
  file: null,
});
const maxFileSize = 3;
const uploadPhoto = (e) => {
  const files = e.target.files;
  let errors = [],
    allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;

  /* file validations */
  if (!files.length) return false;
  if (!allowedExtensions.exec(e.target.value))
    errors.push("Please upload file having extensions .jpeg/.jpg/.png/ only.");
  if (files[0].size / (1024 * 1024) > maxFileSize)
    errors.push("File size is too large (max 3 MB)");
  if (errors.length) {
    alert(errors.join("\n"));
    return (e.target.value = "");
  }
  postData.value.file = files[0];
};

const sharePost = () => {
  const formData = new FormData();
  formData.append("title", postData.value.title);
  formData.append("content", postData.value.content);
  formData.append("file", postData.value.file);
  appAxios.post(`/share_post/${admin.getAdmin}`, formData).then((response) => {
    postData.value.title = null;
    postData.value.content = null;
    postData.value.file = null;
    console.log("response :>> ", response);
    window.location.reload();
  });
};
</script>
