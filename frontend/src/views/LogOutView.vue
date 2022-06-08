<script>
import { axios } from "../common/api.service.js";

export default {
  name: "LogoutView",
  methods: {
    async logoutUser() {
      let endpoint = "/accounts/logout/";
      try {
        const response = await axios.get(endpoint);
        alert(response.statusText);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
  },
  created() {
    this.logoutUser();
  },
};
</script>
