<template>
  <div
    class="overflow-hidden"
    style="position: relative;"
  >
    <v-container class="fill-height">
      <v-row
        align="center"
        justify="center"
      >
      </v-row>
    </v-container>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Dashboard',
  created() {
    this.getTodos();
  },
  methods: {
    getTodos() {
      axios.get('http://localhost:8000/api/v1/todoitems/', {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
