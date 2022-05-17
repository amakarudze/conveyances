<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="d-flex" id="wrapper">
    <!-- Sidebar-->
    <div class="border-end bg-white" id="sidebar-wrapper">
      <div class="sidebar-heading border-bottom bg-light">
        <span class="navbar-brand mb-0 h1">Conveyances</span>
      </div>
      <div class="list-group list-group-flush">
        <RouterLink class="nav-link" to="/">Home</RouterLink>
        <RouterLink class="nav-link" to="/matter">Add New Matter</RouterLink>
        <RouterLink class="nav-link" to="/edit-matter">Edit Matter</RouterLink>
      </div>
    </div>

    <!-- Page content wrapper-->
    <div id="page-content-wrapper">
      <!-- Top navigation-->
      <nav
        class="navbar navbar-expand-lg navbar-light bg-light border-bottom ms-auto"
      >
        <div class="container-fluid">
          <button class="btn btn-primary" id="sidebarToggle">
            Toggle Menu
          </button>
          <button
            class="navbar-toggler"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
            <RouterLink class="nav-link" to="/matter"
              >Add New Matter</RouterLink
            >
            <RouterLink class="nav-link" to="/edit-matter"
              >Edit Matter</RouterLink
            >
          </div>
        </div>
      </nav>
      <!-- Page content-->
      <div class="container-fluid">
        <RouterView />
      </div>
    </div>
  </div>
</template>
