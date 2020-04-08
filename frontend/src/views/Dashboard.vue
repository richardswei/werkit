<template>
  <div
    class="overflow-hidden"
    style="position: relative;"
  >
    <v-container fluid>
      <v-list
      flat
      subheader
      three-line
    >
      <v-subheader>General</v-subheader>

      <v-list-item-group
        multiple
        active-class=""
      >
        <v-list-item
          v-for="item in todoitems"
          :key="item.id"
        >
          <v-list-item-content>
            <v-list-item-title>{{item.title}}</v-list-item-title>
            <v-list-item-subtitle>{{item.description}}</v-list-item-subtitle>
            <v-list-item-subtitle>{{item.due}}</v-list-item-subtitle>
            <v-list-item-subtitle>{{item.updated}}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
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
  data: () => ({
    todoitems: [],
  }),
  methods: {
    getTodos() {
      axios.get('http://localhost:8000/api/v1/todoitems/', {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          console.log(response.data);
          this.todoitems = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
