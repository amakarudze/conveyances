<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<script>
import { axios } from "./common/api.service.js";

export default {
  data() {
    return {
      user: {},
    };
  },
  methods: {
    async getCurrentUser() {
      let endpoint = "/api/current_user/";
      try {
        const response = await axios.get(endpoint);
        this.user = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
    },
  },
  created() {
    this.getCurrentUser();
  },
};
</script>

<template>
  <!-- Page Wrapper -->
  <div id="wrapper">
    <!-- Sidebar -->
    <ul
      class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion"
      id="accordionSidebar"
    >
      <!-- Sidebar - Brand -->
      <RouterLink
        class="sidebar-brand d-flex align-items-center justify-content-center"
        to="/"
      >
        <div class="sidebar-brand-icon rotate-n-15">
          <i class="fas fa-laugh-wink"></i>
        </div>
        <div class="sidebar-brand-text mx-3">Conveyance Matters</div>
      </RouterLink>

      <!-- Divider -->
      <hr class="sidebar-divider my-0" />

      <!-- Nav Item - Dashboard -->
      <li class="nav-item">
        <RouterLink class="nav-link" to="/"
          ><i class="fas fa-fw fa-tachometer-alt"></i
          ><span>Dashboard</span></RouterLink
        >
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider" />

      <!-- Heading -->
      <div class="sidebar-heading">Interface</div>

      <!-- Nav Item - Pages Collapse Menu -->
      <li class="nav-item">
        <RouterLink class="nav-link" to="/add-matter"
          ><i class="fas fa-fw fa-cog"></i
          ><span>Add New Matter</span></RouterLink
        >
      </li>

      <!-- Nav Item - Utilities Collapse Menu -->
      <li class="nav-item">
        <RouterLink class="nav-link" to="/add-bank"
          ><i class="fas fa-fw fa-wrench"></i><span>Add Bank</span></RouterLink
        >
      </li>

      <!-- Nav Item - Utilities Collapse Menu -->
      <li class="nav-item">
        <RouterLink class="nav-link" to="/banks"
          ><i class="fas fa-fw fa-building"></i
          ><span>View All Banks</span></RouterLink
        >
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider d-none d-md-block" />

      <!-- Sidebar Toggler (Sidebar) -->
      <div class="text-center d-none d-md-inline">
        <button class="rounded-circle border-0" id="sidebarToggle"></button>
      </div>
    </ul>
    <!-- End of Sidebar -->

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">
      <!-- Main Content -->
      <div id="content">
        <!-- Topbar -->
        <nav
          class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow"
        >
          <!-- Sidebar Toggle (Topbar) -->
          <button
            id="sidebarToggleTop"
            class="btn btn-link d-md-none rounded-circle mr-3"
          >
            <i class="fa fa-bars"></i>
          </button>

          <!-- Topbar Navbar -->
          <ul class="navbar-nav ml-auto">
            <div class="topbar-divider d-none d-sm-block"></div>

            <!-- Nav Item - User Information -->
            <li class="nav-item dropdown no-arrow">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                id="userDropdown"
                role="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                <span class="mr-2 d-none d-lg-inline text-gray-600 small"
                  >Hello, {{ user.username }}</span
                >
                <img
                  class="img-profile rounded-circle"
                  src="/src/img/undraw_profile.svg"
                />
              </a>
              <!-- Dropdown - User Information -->
              <div
                class="dropdown-menu dropdown-menu-right shadow animated--grow-in"
                aria-labelledby="userDropdown"
              >
                <RouterLink
                  class="dropdown-item"
                  data-toggle="modal"
                  data-target="#logoutModal"
                  to="/logout"
                >
                  <i
                    class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"
                  ></i>
                  Logout
                </RouterLink>
              </div>
            </li>
          </ul>
        </nav>
        <!-- End of Topbar -->

        <!-- Begin Page Content -->
        <div class="container-fluid">
          <RouterView />
        </div>
        <!-- /.container-fluid -->
      </div>
      <!-- End of Main Content -->

      <!-- Footer -->
      <footer class="sticky-footer bg-white">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <span>Copyright &copy; Anna Makarudze 2022</span>
          </div>
        </div>
      </footer>
      <!-- End of Footer -->
    </div>
    <!-- End of Content Wrapper -->
  </div>
  <!-- End of Page Wrapper -->
</template>
