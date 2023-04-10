<template>
    <div class="flex flex-col items-center justify-center ml-60">
      <div class="bg-indigo-200 shadow-lg rounded-lg p-8">
        <div class="text-4xl font-bold mb-4">Ziyaretçi Sayısı</div>
        <div class="text-6xl font-bold">{{ pageViews }}</div>
      </div>
    </div>
</template>
  
<script>
  import { ref, onMounted } from 'vue';
  
  export default {
    name: 'VisitorCount',
    setup() {
    const pageViews = ref(0);

    onMounted(() => {
      pageViews.value++;
    });

    return { pageViews }
  },
  };
  </script>
  