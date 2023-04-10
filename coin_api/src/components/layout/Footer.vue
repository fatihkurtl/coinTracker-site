<template>
  <footer class="bg-gray-800 mt-auto">
  <div class="max-w-6xl mx-auto flex flex-wrap justify-between">
    <div class="p-5 w-1/2 sm:w-4/12 md:w-3/12">
      <a class="text-white text-3xl font-bold leading-none" href="#">
        CoinTracker
      </a>
    </div>
    <div class="p-5 w-1/2 sm:w-4/12 md:w-3/12">
      <ul class="list-unstyled">
        <li>
          <router-link :to="{ name: 'Home' }" class="text-white hover:text-gray-300 font-medium block pb-2 text-sm">
            Anasayfa
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'Coins' }" class="text-white hover:text-gray-300 font-medium block pb-2 text-sm">
            Piyasalar
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'About' }" class="text-white hover:text-gray-300 font-medium block pb-2 text-sm">
            Hakkımızda
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'Contact' }" class="text-white hover:text-gray-300 font-medium block pb-2 text-sm">
            İletişim
          </router-link>
        </li>
      </ul>
    </div>
    <div class="p-5 w-1/2 sm:w-4/12 md:w-3/12">
      <ul class="list-unstyled">
        <li>
          <a href="#" class="text-white hover:text-gray-300 font-medium block pb-2 text-sm">
            Kullanım Şartları
          </a>
        </li>
        <li>
          <a href="#" class="text-white hover:text-gray-300 font-medium block pb-2 text-sm">
            Gizlilik Politikası
          </a>
        </li>
        <li>
          <a href="#" class="text-white hover:text-gray-300 font-medium block pb-2 text-sm">
            Sıkça Sorulan Sorular
          </a>
        </li>
      </ul>
    </div>
    <div class="p-5 w-1/2 sm:w-4/12 md:w-3/12">
      <div class="text-white mb-2 mt-4">Bizi Takip Edin</div>

      <div class="flex mb-4">
        <a href="https://github.com/fatihkurtl" target="_blank" class="no-underline hover:text-gray-300">
          <i class="fab fa-github fa-2x mr-3"></i>
        </a>
        <a href="https://www.linkedin.com/in/fatihkurtl/" target="_blank" class="no-underline hover:text-gray-300">
          <i class="fab fa-linkedin fa-2x"></i>
        </a>
      </div>
      <div class="text-white">&copy; CoinTracker.com. Tüm hakları saklıdır.</div>
    </div>
  </div>
</footer>

</template>

<style>
footer {
  bottom: 0;
  left: 0;
  right: 0;
}
</style>
