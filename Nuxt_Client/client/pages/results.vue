<template>
  <div>
    <h1>This is the results page</h1>
    <ul>
      <li v-for="survey in this.surveys" :key="survey.id">
        id:{{ survey[0] }} count:{{ survey[1] }} description:{{ survey[2] }}
      </li>
    </ul>
    <router-link to="/">Back to the main page</router-link>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      surveys: [],
    };
  },

  mounted() {
    this.surveys = this.asycSurveys();
  },
  
  methods: {
    async asycSurveys() {
      try {
        axios.get(`http://localhost:8000/survey/`).then((result) => {
          this.surveys = JSON.parse(result.data);
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