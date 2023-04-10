import { defineStore } from "pinia";
import router from "../router";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    user: null,
    token: null,
    admin: null,
    post_id: null,
  }),

  actions: {
    handleLogin(data) {
      console.log(data);
      this.user = data;
    },
    saveToken(e) {
      console.log(e);
      this.token = e;
    },
    handleLogout() {
      this.user = null;
      this.token = null;
      this.admin = null;
      router.push({ name: "Login" });
    },
    isAdmin(e) {
      this.admin = e;
    },
    postDetail(e) {
      this.post_id = e;
    }
  },
  getters: {
    isAuth: (state) => state.user != null,
    getCurrentUser(state) {
      return state.user;
    },
    getUserToken(state) {
      return state.token;
    },
    getAdmin(state) {
      return state.admin;
    },
  },

  // localStorage
  persist: true,
});
