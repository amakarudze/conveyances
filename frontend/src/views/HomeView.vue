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
                        class="sorting_asc text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-sort="ascending text-primary"
                        aria-label="Full Name: activate to sort column descending"
                      >
                        Matter
                      </th>
                      <th
                        scope="col"
                        class="sorting text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-label="Email: activate to sort column ascending"
                      >
                        Current Stage
                      </th>
                      <th
                        scope="col"
                        class="sorting text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-label="Is Active: activate to sort column ascending"
                      >
                        Bank
                      </th>
                      <th
                        scope="col"
                        class="sorting text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-label="Is Staff: activate to sort column ascending"
                      >
                        Created by
                      </th>
                      <th
                        scope="col"
                        class="sorting text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-label="Is Admin: activate to sort column ascending"
                      >
                        Date Created
                      </th>
                      <th
                        scope="col"
                        class="sorting text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-label="Date Joined: activate to sort column ascending"
                      >
                        Last Updated
                      </th>
                      <th
                        scope="col"
                        class="sorting text-primary"
                        tabindex="0"
                        aria-controls="dataTable"
                        rowspan="1"
                        colspan="1"
                        aria-label="Date Joined: activate to sort column ascending"
                      >
                        Complete
                      </th>
                    </tr>
                  </thead>
                  <tfoot class="bg-gradient-light">
                    <tr>
                      <th scope="col" class="text-primary">Matter</th>
                      <th scope="col" class="text-primary">Current Stage</th>
                      <th scope="col" class="text-primary">Bank</th>
                      <th scope="col" class="text-primary">Created by</th>
                      <th scope="col" class="text-primary">Date Created</th>
                      <th scope="col" class="text-primary">Last Updated</th>
                      <th scope="col" class="text-primary">Complete</th>
                    </tr>
                  </tfoot>
                  <tbody>
                    <tr>
                      <td><a href="#"></a></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td>
                        <i class="fa fa-check-square text-success"></i>
                        <i class="fa fa-window-close text-danger"></i>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
