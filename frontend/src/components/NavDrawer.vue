<template>
  <v-navigation-drawer
    v-model="drawerState"
    right
    absolute
    stateless
  >
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="/blank_avatar.svg"></v-img>
      </v-list-item-avatar>

      <v-list-item-content>
          <v-list-item-title class="title">
            {{user.username}}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{user.first_name}}
          </v-list-item-subtitle>
        </v-list-item-content>
    </v-list-item>
    <v-list-item
      @click="deleteAuth"
      dark
      class="teal"
    >
      Sign Out
      <v-spacer></v-spacer>
      <v-icon>exit_to_app</v-icon>
    </v-list-item>

    <v-divider></v-divider>

    <v-list dense>

      <v-list-item
        v-for="item in items"
        :key="item.title"
        :to="item.link"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title link>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import axios from 'axios';

export default {
  // beforeCreate() {
  //   console.log('Nothing gets called before me!')
  // },
  data: () => ({
    items: [
      { title: 'Profile', icon: 'person', link: '/app/profile' },
      { title: 'Dashboard', icon: 'dashboard', link: '/app/dashboard' },
      { title: 'Notes', icon: 'notes', link: '/app/notes' },
    ],
  }),
  computed: {
    drawerState: {
      get() {
        return this.$store.getters.drawerState;
      },
      set() {
        // this.$store.commit('TOGGLE_DRAWER');
      },
    },
    user: {
      get() {
        return this.$store.getters.user;
      },
      set() {

      },
    },
  },
  methods: {
    deleteAuth(event) {
      event.preventDefault();
      axios.delete('http://localhost:8000/api/v1/signout/', {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$store.dispatch('signout');
        })
        .then(() => window.location.replace('/'))
        .catch((e) => {
          this.$store.dispatch('signout');
          console.log(e);
        });
    },
  },
};
</script>
<style>
  .flipped {
    transform: rotateY(180deg);
  }
</style>
