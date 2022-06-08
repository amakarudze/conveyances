<template>
  <div id="matters">
    <!-- Page Heading -->
    <h1 class="h3 mb-2 text-gray-800">Conveyances Matters</h1>

    <!-- DataTables Example -->
    <div class="card shadow mb-4">
      <div class="card-header py-3">
        <h6 class="m-0 font-weight-bold text-primary">
          List of Conveyances Matters
        </h6>
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <div id="dataTable_wrapper" class="dataTables_wrapper dt-bootstrap4">
            <div class="row">
              <div class="col-sm-12">
                <table
                  class="table table-bordered dataTable"
                  id="dataTable"
                  width="100%"
                  cellspacing="0"
                  role="grid"
                  aria-describedby="dataTable_info"
                  style="width: 100%"
                >
                  <thead class="bg-gradient-light">
                    <tr role="row">
                      <th
                        scope="col"
                        class="text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-sort="ascending text-primary"
                      >
                        Conveyance Matter
                      </th>
                      <th
                        scope="col"
                        class="text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                      >
                        Bank
                      </th>
                      <th
                        scope="col"
                        class="text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                      >
                        Created by
                      </th>
                      <th
                        scope="col"
                        class="text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                      >
                        Date Created
                      </th>
                      <th
                        scope="col"
                        class="text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                      >
                        Last Updated
                      </th>
                      <th
                        scope="col"
                        class="text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                      >
                        Complete
                      </th>
                    </tr>
                  </thead>
                  <tfoot class="bg-gradient-light">
                    <tr>
                      <th scope="col" class="text-primary">
                        Conveyance Matter
                      </th>
                      <th scope="col" class="text-primary">Bank</th>
                      <th scope="col" class="text-primary">Created by</th>
                      <th scope="col" class="text-primary">Date Created</th>
                      <th scope="col" class="text-primary">Last Updated</th>
                      <th scope="col" class="text-primary">Complete</th>
                    </tr>
                  </tfoot>
                  <tbody>
                    <tr v-for="conveyance in conveyances" :key="conveyance.pk">
                      <td>
                        <router-link
                          :to="{
                            name: 'conveyance',
                            params: { slug: conveyance.uuid },
                          }"
                          class="nav-link"
                        >
                          {{ conveyance.title }}</router-link
                        >
                      </td>
                      <td>{{ conveyance.bank }}</td>
                      <td>{{ conveyance.created_by }}</td>
                      <td>{{ conveyance.created_at }}</td>
                      <td>{{ conveyance.last_updated }}</td>
                      <td>
                        <i
                          v-if="conveyance.complete"
                          class="fa fa-check-square text-success"
                        ></i>
                        <i v-else class="fa fa-window-close text-danger"></i>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row justify-content-md-center">
        <div class="col col-lg-2"></div>
        <div class="col-md-auto">
          <nav aria-label="Page navigation">
            <ul class="pagination">
              <li v-show="previous" @click="getConveyances" class="page-item">
                <span class="page-link">&laquo;</span>
              </li>
              <li
                v-for="i in total_pages"
                :key="i"
                @click="getConveyances"
                class="page-item"
              >
                <span
                  v-if="i === current"
                  class="page-item active page-link"
                  aria-current="page"
                >
                  {{ i }}</span
                ><span v-else class="page-item page-link"> {{ i }}</span>
              </li>

              <li v-show="next" @click="getConveyances" class="page-item">
                <span class="page-link">&raquo;</span>
              </li>
            </ul>
          </nav>
        </div>
        <div class="col col-lg-2"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from "../common/api.service.js";
export default {
  name: "HomeView",
  data() {
    return {
      conveyances: [],
      count: null,
      current: null,
      next: null,
      previous: null,
      total_pages: null,
    };
  },
  methods: {
    async getConveyances() {
      let endpoint = "/api/conveyance_matters/";
      if (this.next) {
        endpoint = this.next;
      }
      if (this.previous) {
        endpoint = this.previous;
      }
      try {
        const response = await axios.get(endpoint);
        this.conveyances.push(...response.data.results);
        this.current = response.data.current;
        this.total_pages = response.data.total_pages;
        if (response.data.count) {
          this.count = response.data.count;
        }
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
        if (response.data.previous) {
          this.previous = response.data.previous;
        } else {
          this.previous = null;
        }
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
  },
  created() {
    this.getConveyances();
    document.title = "Home - Conveyances Matters";
  },
};
</script>
