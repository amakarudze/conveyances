<template>
  <div id="bank" class="container">
    <div class="shadow p-3 mb-5 bg-body rounded">
      <h1 class="mb-3">Add Bank</h1>
      <form @submit.prevent="onSubmit">
        <input
          v-model="bankName"
          class="form-control"
          placeholder="Enter Bank Name"
        />
        <br />
        <button type="submit" class="btn btn-primary">Add</button>
      </form>

      <p v-if="error" class="text-danger mt-2">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { axios } from "../common/api.service.js";

export default {
  name: "BankView",
  data() {
    return {
      bankName: null,
      error: null,
    };
  },
  methods: {
    async performNetworkRequest() {
      let endpoint = "/api/banks/";
      let method = "POST";
      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: { name: this.bankName },
        });
        alert(response.statusText);
        this.$router.push({ name: "banks" });
      } catch (error) {
        this.error = error.response.statusText;
      }
    },
    onSubmit() {
      if (!this.bankName) {
        this.error = "Bank field should not be empty!";
      } else if (this.bankName.length > 255) {
        this.error = "Ensure this field has no more than 255 characters!";
      } else {
        this.performNetworkRequest();
      }
    },
  },
  created() {
    document.title = "Add Bank - Conveyances Matters";
  },
};
</script>
