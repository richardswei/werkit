<template>
  <v-app id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/dashboard">Dashboard</router-link> |
      <router-link to="/authentication">Sign In</router-link> |
      <router-link to="/registration">New Account</router-link>
    </div> -->
    <v-app-bar
      app
      class="primary"
    >
      <router-link to="/">
        <img
          src="@/assets/logos/vector/default-monochrome-white.svg"
          alt="Logo"
          height="40"/>
      </router-link>
      <v-spacer/>
      <v-btn
        v-if="this.$store.state.token"
        color="teal"
        dark
        @click="toggleMenu"
      >
        <v-icon>menu</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content>
      <router-view class="pt-12 pb-12 background"/>
      <NavDrawer/>
    </v-content>
  </v-app>
</template>

<script>
import NavDrawer from '@/components/NavDrawer.vue';

export default {
  name: 'Home',
  components: {
    NavDrawer,
  },
  methods: {
    toggleMenu() {
      this.$store.dispatch('togglemenu');
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: var(--v-primary-base);
}

.background {
  background: url(./assets/background.png) no-repeat center center fixed;
  background-size: cover;
  height: 100%;
}

.text-white {
  color: white
}

</style>
