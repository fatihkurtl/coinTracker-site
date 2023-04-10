import { createRouter, createWebHashHistory } from "vue-router";
import { useAuthStore } from "./store/auth";
import { useRoute, useRouter } from "vue-router";

const routes = [
  {
    name: "Home",
    path: "/",
    component: () => import("@/views/home.vue"),
  },
  {
    name: "Coins",
    path: "/coins",
    component: () => import("@/views/coins.vue"),
  },
  {
    name: 'Currency',
    path: '/currency',
    component: () => import('@/views/currency.vue')
  },
  {
    name: "About",
    path: "/about",
    component: () => import("@/views/about.vue"),
  },
  {
    name: "Contact",
    path: "/contact",
    component: () => import("@/views/contact.vue"),
  },
  {
    name: "PostDetail",
    path: "/post_detail/:id",
    component: () => import("@/views/postDetail.vue"),
  },
  {
    name: "Register",
    path: "/register",
    component: () => import("@/views/register.vue"),
  },
  {
    name: "Login",
    path: "/login",
    component: () => import("@/views/login.vue"),
  },
  {
    name: "Forgot Password",
    path: "/forgot_password",
    component: () => import("@/views/forgotPassword.vue"),
  },
  {
    name: "Admin Share Post",
    path: "/share_post/admin",
    component: () => import("@/views/admin/sharePost.vue"),
    meta: { requiresAuth: true, isAdmin: true }, // Meta verisi ile admin sayfalarını belirliyoruz
  },
  {
    name: "Member List",
    path: "/member_list/admin",
    component: () => import("@/views/admin/memberList.vue"),
    meta: { requiresAuth: true, isAdmin: true }, // Meta verisi ile admin sayfalarını belirliyoruz
  },
];

const router = createRouter({
  routes,
  history: createWebHashHistory(),
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  const isAuth = authStore.isAuth;

  const admin = authStore.admin;

  const authNotRequired = [
    "Login",
    "Register",
    "Home",
    "Coins",
    "Currency",
    "PostDetail",
    "About",
    "Contact",
  ];
  const authRequired = ["Admin Share Post", "Member List"];

  if (authRequired.indexOf(to.name) > -1 && !admin) next({ name: "Login" });
  else next();
  if (authNotRequired.indexOf(to.name) > -1 && isAuth) {
    return { name: "Home" };
  }
});

export default router;
