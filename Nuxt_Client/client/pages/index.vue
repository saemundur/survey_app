<template>
  <div class="page">
    <h1>Thank you for participating in our survey!</h1>
    <div class="question">
      <h2>
        {{ this.statisticsLable }}
      </h2>
      <input v-model="count" type="number"/>
    </div>
    <div class="question">
      <h2>
        {{ this.describtionLable }}
      </h2>
      <input v-model="describtion" type="text" />
    </div>
    <button @click="submit">Submit</button>
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
      statisticsLable:
        "How many employees in your organization have received training sessions last year?",
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
.question {
  align-content: center;

  margin-bottom: 50px;
}

.page {
  margin-top: 20px;
  margin-left: 50px;
}

h1 {
  margin-bottom: 15px;
}
button {
  margin-right: 50px;
}
</style>