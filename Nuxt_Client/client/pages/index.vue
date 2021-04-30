<template>
  <div>
    <h2>
      {{ this.statisticsLable }}
    </h2>
    <input v-model="count" type="number" step="1" pattern="\d+" min="0" />
    <h2>
      {{this.describtionLable}}  
    </h2>
    <input v-model="describtion" type="text" />
    <br />
    <br />
    <button @click="submit">Submit</button>
    <br />
    <br />
    <router-link to="/results">Go to results</router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: function () {
    return {
      count: 0,
      describtion: "",
      statisticsLable: "How many employees in your organization have received training sessions last year?",
      describtionLable: "Describe the Training that were happening.",
    };
  },

  mounted() {
    this.getLables();
  },

  methods: {
    submit() {
      axios
        .post("http://localhost:8000/survey/submit/", {
          count: this.count,
          describtion: this.describtion,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.error(error);
        });
    },
    async getLables() {
      try {
        axios.get(`http://localhost:8000/survey/lables/`).then((result) => {
          let lables = JSON.parse(result.data);
          this.statisticsLable = lables[0];
          this.describtionLable = lables[1];
        });
      } catch (e) {
        console.error(e);
      }
    },
  },
};
</script>

<style>
</style>