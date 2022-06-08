<template>
  <div id="matter" class="container">
    <div class="shadow p-3 mb-5 bg-body rounded">
      <h1>Add a New Conveyance Matter</h1>

      <form @submit.prevent="onSubmit">
        <div>
          <div class="mb-3 row">
            <label for="title" class="col-sm-4 col-form-label"
              >Conveyance Matter Title
            </label>
            <div class="col-sm-8">
              <textarea
                rows="3"
                v-model="title"
                class="form-control"
                placeholder="Enter Conveyance Matter Title"
              >
              </textarea>
            </div>
            <br />
          </div>
          <div class="mb-3 row">
            <label for="bank" class="col-sm-4 col-form-label">Bank</label>
            <div class="col-sm-8">
              <select
                v-model="selected_bank"
                class="form-select mb-3 col-sm-12"
                aria-label=".form-select-lg example"
              >
                <option
                  v-for="bank in banks"
                  :key="bank.id"
                  v-bind:value="{ id: bank.id, name: bank.name }"
                >
                  {{ bank.name }}
                </option>
              </select>
            </div>
          </div>
          <hr />

          <br />
          <h3>List of Matters</h3>
          <hr />
          <br />
          <div class="row">
            <div class="col-md-6"><h4>Name</h4></div>
            <div class="col-md-4"><h4>Type</h4></div>
            <div class="col-md-2"><h4>Select</h4></div>
          </div>
          <hr />
          <div class="row" v-for="matter in matters" :key="matter.pk">
            <div class="col-md-6">
              <input
                v-model="matter.name"
                :id="matter.name"
                :name="matter.name"
                class="form-control mb-3"
                placeholder="Enter Client's Name - Matter"
              />
            </div>
            <div class="col-md-4">{{ matter.name }}</div>
            <div class="col-md-2 text-center">
              <input
                v-model="selected"
                :value="matter"
                class="form-check-input"
                type="checkbox"
              />
            </div>
          </div>
          <br />
          <button type="submit" class="btn btn-primary">Add</button>
        </div>
      </form>

      <p v-if="error" class="text-danger mt-2">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { axios } from "../common/api.service.js";

export default {
  name: "MatterView",

  data() {
    return {
      banks: [],
      matters: [],
      selected: [],
      selected_bank: {},
      error: null,
      bank: null,
      title: null,
    };
  },
  methods: {
    async getBanksData() {
      let endpoint = "/api/banks/";
      try {
        const response = await axios.get(endpoint);
        this.banks.push(...response.data.results);
        console.log(this.banks);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
    async getMattersData() {
      let endpoint = "/api/base_matters/";
      try {
        const response = await axios.get(endpoint);
        this.matters = response.data;
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
    async performNetworkRequest() {
      let endpoint = "/api/conveyance_matters/";
      let method = "POST";
      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: {
            title: this.title,
            bank: this.selected_bank.name,
            matters: this.selected,
          },
        });
        this.$router.push({ name: "home" });
      } catch (error) {
        this.error = error.response.statusText;
      }
    },
    onSubmit() {
      this.matters.forEach((matter) => {
        if (matter.checkbox === true) {
          this.selected.push(matter);
        }
      });
      if (!this.title) {
        this.error = "The title field should not be empty!";
      } else if (this.title.length > 255) {
        this.error = "Ensure this field has no more than 255 characters!";
      } else {
        this.performNetworkRequest();
      }
    },
  },
  created() {
    this.getBanksData();
    this.getMattersData();
    document.title = "Add Matter - Conveyances Matters";
  },
};
</script>
