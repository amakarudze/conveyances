import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory("/"),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/add-bank/",
      name: "add-bank",
      // route level code-splitting
      // this generates a separate chunk (MatterEditor.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/BankView.vue"),
    },
    {
      path: "/add-matter/",
      name: "add-matter",
      // route level code-splitting
      // this generates a separate chunk (Matter.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/MatterView.vue"),
    },
    {
      path: "/conveyance/:slug/",
      name: "conveyance",
      component: () => import("../views/ConveyanceMatterView.vue"),
      props: true,
    },
    {
      path: "/logout/",
      name: "logout",
      component: () => import("../views/LogoutView.vue"),
    },
    {
      path: "/banks/",
      name: "bank",
      component: () => import("../views/BanksView.vue"),
    },
  ],
});

export default router;
