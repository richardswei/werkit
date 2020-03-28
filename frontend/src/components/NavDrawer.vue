<template>
  <v-navigation-drawer
    v-model="drawerState"
    absolute
  >
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="/blank_avatar.svg"></v-img>
      </v-list-item-avatar>

      <v-list-item-content>
        <v-list-item-title>First_Name Last_Name</v-list-item-title>
      </v-list-item-content>
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
export default {
  // beforeCreate() {
  //   console.log('Nothing gets called before me!')
  // },
  data: () => ({
    items: [
      { title: 'Home', icon: 'dashboard', link: '/' },
      { title: 'About', icon: 'question_answer', link: '/' },
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
  },
};
</script>
