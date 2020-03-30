<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" lg="4">
        <v-form @submit='postAuth'>
          <v-card class="elevation-12">
            <v-toolbar color="primary" dark flat>
              <v-toolbar-title>Sign In</v-toolbar-title>
              <v-spacer />
            </v-toolbar>
            <v-card-text>
                <v-text-field
                  label="Username"
                  name="username"
                  v-model='username'
                  autocomplete="username"
                  prepend-icon="person"
                  type="text"
                />
                <v-text-field
                  id="password"
                  label="Password"
                  name="password"
                  v-model='password'
                  autocomplete="current-password"
                  prepend-icon="lock"
                  type="password"
                />
            </v-card-text>
            <v-card-actions>
              <v-btn @click="showToken">Token</v-btn>

              <v-btn class="link" to="/registration">Don't have an account?</v-btn>
              <v-spacer />
              <v-btn type="submit" color="primary">Login</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Authentication',
  data: () => ({
    username: '',
    password: '',
  }),
  methods: {
    showToken() {
      console.log(this.$store.state.token);
    },
    postAuth(event) {
      event.preventDefault();
      axios.post('http://localhost:8000/api/v1/signin/', {
        username: this.username,
        password: this.password,
      })
        .then((response) => {
          this.$store.dispatch('signin', response.data.token);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
