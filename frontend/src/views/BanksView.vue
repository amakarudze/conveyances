<template>
  <div id="banks">
    <!-- Page Heading -->
    <h1 class="h3 mb-2 text-gray-800">Banks</h1>

    <!-- DataTables Example -->
    <div class="card shadow mb-4">
      <div class="card-header py-3">
        <h6 class="m-0 font-weight-bold text-primary">List of Banks</h6>
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
                        Bank Name
                      </th>
                    </tr>
                  </thead>
                  <tfoot class="bg-gradient-light">
                    <tr>
                      <th scope="col" class="text-primary">Bank</th>
                    </tr>
                  </tfoot>
                  <tbody>
                    <tr v-for="bank in banks" :key="bank.pk">
                      <td>{{ bank.name }}</td>
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
              <li v-show="previous" @click="getBanksData" class="page-item">
                <span class="page-link">&laquo;</span>
              </li>
              <li
                v-for="i in total_pages"
                :key="i"
                @click="getBanksData"
                class="page-item"
              >
                <span
                  v-if="i === current"
                  class="page-item active page-link"
                  aria-current="page"
                >
                  {{ i }}</span
                >
                <span v-else class="page-item page-link"> {{ i }}</span>
              </li>

              <li v-show="next" @click="getBanksData" class="page-item">
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
  name: "BanksView",
  data() {
    return {
      banks: [],
      count: null,
      current: null,
      next: null,
      previous: null,
      total_pages: null,
    };
  },
  methods: {
    async getBanksData() {
      let endpoint = "/api/banks/";
      if (this.next) {
        endpoint = this.next;
      }
      if (this.previous) {
        endpoint = this.previous;
      }
      try {
        const response = await axios.get(endpoint);
        this.banks.push(...response.data.results);
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
    this.getBanksData();
    document.title = "View Banks - Conveyances Matters";
  },
};
</script>
