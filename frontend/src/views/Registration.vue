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
                autocomplete="username"
                prepend-icon="person"
                type="text"
              />
              <v-text-field
                label="First Name"
                autocomplete="given-name"
                v-model="firstname"
                type="text"
              />
              <v-text-field
                label="Last Name"
                autocomplete="family-name"
                v-model="lastname"
                type="text"
              />
              <v-text-field
                label="Email"
                autocomplete="email"
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
                v-model="confirmation"
                prepend-icon="lock"
                type="password"
              />
            </v-card-text>
            <v-card-actions>
              <v-btn class="link" to="/signin">Already have an account?</v-btn>
              <v-spacer />
              <v-btn type="submit" color=primary>Register</v-btn>
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
  data: () => ({
    username: '',
    firstname: '',
    lastname: '',
    email: '',
    password: '',
    confirmation: '',
  }),
  methods: {
    postRegistration(event) {
      event.preventDefault();
      axios.post('http://localhost:8000/api/v1/registration/', {
        username: this.username,
        first_name: this.firstname,
        last_name: this.lastname,
        email: this.email,
        password: this.password,
      })
        .then(() => window.location.replace('/signin'))
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
