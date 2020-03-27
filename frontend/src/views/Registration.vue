<template>
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" lg="4">
          <v-form @submit='postRegistration'>
            <v-card class="elevation-12">
              <v-toolbar color="primary" dark flat>
              <v-toolbar-title>New Account</v-toolbar-title>
              <v-spacer />
            </v-toolbar>
            <v-card-text>
              <v-text-field
                label="Username"
                v-model="username"
                prepend-icon="person"
                type="text"
              />
              <v-text-field
                label="First Name"
                v-model="firstname"
                type="text"
              />
              <v-text-field
                label="Last Name"
                v-model="lastname"
                type="text"
              />
              <v-text-field
                label="Email"
                v-model="email"
                prepend-icon="mail"
                type="text"
              />
              <v-text-field
                id="password"
                label="Password"
                v-model="password"
                prepend-icon="lock"
                type="password"
              />
              <v-text-field
                id="password-verification"
                label="Confirm Password"
                v-model="password"
                prepend-icon="lock"
                type="password"
              />
            </v-card-text>
            <v-card-actions>
              <v-btn @click='increment'>increment</v-btn>
              <v-btn class="link" to="/authentication">Already have an account?</v-btn>
              <v-spacer />
              <v-btn type="submit">Register</v-btn>
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
  name: 'Registration',
  components: {
  },
  computed: {
    count() {
      return this.$store.state.count;
    },
  },
  data: () => ({
    username: '',
    firstname: '',
    lastname: '',
    email: '',
    password: '',
  }),
  methods: {
    increment() {
      console.log('starting increment');
      this.$store.commit('INCREMENT');
    },
    postRegistration(event) {
      event.preventDefault();
      const account = {
        username: this.username,
        first_name: this.firstname,
        last_name: this.lastname,
        email: this.email,
        password: this.password,
        todoitems: [],
        notes: [],
      };
      console.log(account);
      axios.post('http://localhost:8000/api/v1/registration/', {
        username: this.username,
        first_name: this.firstname,
        last_name: this.lastname,
        email: this.email,
        password: this.password,
        todoitems: [],
        notes: [],
      })
        .then((response) => {
          console.log(response);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
