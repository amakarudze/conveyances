<template>
  <div id="conveyance-details">
    <h1>{{ conveyance.title }}</h1>
    <div class="shadow p-3 mb-5 bg-body rounded">
      <form @submit.prevent="onSubmit">
        <div class="row">
          <div class="col-sm-4">
            <p><strong> Created by:</strong></p>
          </div>
          <div class="col-sm-8">
            <p>{{ conveyance.created_by }}</p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4">
            <p><strong> Created at:</strong></p>
          </div>
          <div class="col-sm-8">
            <p>{{ conveyance.created_at }}</p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4">
            <p><strong> Bank:</strong></p>
          </div>
          <div class="col-sm-8">
            <p>{{ conveyance.bank }}</p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4">
            <p><strong> Complete:</strong></p>
          </div>
          <div class="col-sm-8">
            <i
              v-if="conveyance.complete === true"
              class="fa fa-check-square text-success"
            ></i>
            <input
              v-else
              v-model="conveyance.complete"
              :value="conveyance.complete"
              class="form-check-input ml-2"
              type="checkbox"
            />
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4">
            <p><strong> Comments:</strong></p>
          </div>
          <div class="col-sm-8">
            <textarea
              rows="3"
              v-model="conveyance.comment"
              class="form-control mb-3"
            ></textarea>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4">
            <p><strong> Last updated:</strong></p>
          </div>
          <div class="col-sm-8">
            <p>{{ conveyance.last_updated }}</p>
          </div>
        </div>
        <hr />
        <div>
          <h3>Matters:</h3>
          <div
            :span="8"
            v-for="matter in conveyance.matters"
            :key="matter.index"
            class="card mb-3"
          >
            <div class="card-body">
              <div class="card-title">
                <h4>{{ matter.name }} # Matter No. {{ matter.pk }}</h4>
                <hr />
              </div>
              <div class="row">
                <div class="col-sm-3"><h5>Stage</h5></div>
                <div class="col-sm-4"><h5>Comment</h5></div>
                <div class="col-sm-2 offset-1"><h5>Done</h5></div>
              </div>
              <div
                v-for="stage in matter.stages"
                :key="stage.index"
                class="card-text"
              >
                <hr />
                <div class="row">
                  <div class="col-sm-3">{{ stage.stage }}</div>
                  <div class="col-sm-6">
                    <textarea
                      rows="3"
                      v-model="stage.comment"
                      class="form-control mb-3"
                    ></textarea>
                  </div>
                  <div class="col-sm-2 offset-1">
                    <i
                      v-if="stage.done === true"
                      class="fa fa-check-square text-success"
                    ></i>
                    <input
                      v-else
                      v-model="stage.done"
                      :value="stage.done"
                      class="form-check-input ml-2"
                      type="checkbox"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4"></div>
          <div class="col-sm-4"></div>
          <div class="col-sm-4">
            <button type="submit" class="btn btn-primary">Update</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { axios } from "../common/api.service.js";

export default {
  name: "ConveyanceMatterView",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      conveyance: {},
    };
  },
  methods: {
    async getConveyanceData() {
      let endpoint = `/api/conveyance_matters/${this.slug}/`;
      try {
        const response = await axios.get(endpoint);
        this.conveyance = response.data;
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
    async performNetworkRequest() {
      let endpoint = `/api/conveyance_matters/${this.slug}/`;
      let method = "PATCH";
      try {
        const response = await axios({
          url: endpoint,
          method: method,
          data: {
            complete: this.conveyance.complete,
            comment: this.conveyance.comment,
            matters: this.conveyance.matters,
          },
        });
        this.$router.push({ name: "home" });
      } catch (error) {
        this.error = error.response.statusText;
      }
    },
    onSubmit() {
      this.performNetworkRequest();
    },
  },
  created() {
    this.getConveyanceData();
    document.title = "Matter Details - Conveyances Matters";
  },
};
</script>
