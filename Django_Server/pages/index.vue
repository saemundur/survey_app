<template>
  <div>
    <h1>Survey</h1>
    <h2>
      How many employees in your organization have received training sessions
      last year?
    </h2>
    <input type="number" step="1" pattern="\d+" />
    <h2>Describe the Training that were happening.</h2>
    <input type="text" />
    <br />
    <button>Submit</button>
  </div>
</template>

<script>
// import axios form '@nuxtjs/axios'

export default {
  created() {
    // this.surveys = this.asycSurveys();
  },
  data() {
    return {
      surveys: [],
    };
  },
  methods: {
    async asycSurveys({ $axios, params }) {
      try {
        let surveys = await $axios.$get(`/http://localhost:8000/survey/`);
        return { surveys };
      } catch (e) {
        return { surveys: [] };
      }
    },
  },
};
</script>

<style>
</style>