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
      path: "/edit-matter",
      name: "edit-matter",
      // route level code-splitting
      // this generates a separate chunk (MatterEditor.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/MatterEditorView.vue"),
    },
    {
      path: "/matter",
      name: "matter",
      // route level code-splitting
      // this generates a separate chunk (Matter.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/MatterView.vue"),
    },
  ],
});

export default router;
