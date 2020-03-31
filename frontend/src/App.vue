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
      <div class="text-white display-3">Werkit</div>
      <v-spacer/>
      <v-btn
        v-if="this.$store.state.token"
        color="pink"
        dark
        @click="itemClick"
      >
        Menu
      </v-btn>
    </v-app-bar>
    <v-content>
      <!-- <v-container> -->
      <router-view class="background"/>
      <!-- </v-container> -->
      <NavDrawer/>
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>
import Footer from '@/components/Footer.vue';
import NavDrawer from '@/components/NavDrawer.vue';

export default {
  name: 'Home',
  components: {
    Footer,
    NavDrawer,
  },
  methods: {
    itemClick() {
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
  text-align: center;
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
