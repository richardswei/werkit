<template>
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          cols="12"
          sm="8"
          md="4"
        >
          <v-card class="elevation-12">
            <v-toolbar
              color="primary"
              dark
              flat
            >
              <v-toolbar-title>New Account</v-toolbar-title>
              <v-spacer />
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field
                  label="Username"
                  name="login"
                  prepend-icon="person"
                  type="text"
                />
                <v-text-field
                  label="First Name"
                  name="firstname"
                  type="text"
                />
                <v-text-field
                  label="Last Name"
                  name="lastname"
                  type="text"
                />
                <v-text-field
                  label="Email"
                  name="login"
                  prepend-icon="mail"
                  type="text"
                />
                <v-text-field
                  id="password"
                  label="Password"
                  name="password"
                  prepend-icon="lock"
                  type="password"
                />
                <v-text-field
                  id="password-verification"
                  label="Confirm Password"
                  name="password"
                  prepend-icon="lock"
                  type="password"
                />
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-btn class="link" to="/authentication">Already have an account?</v-btn>
              <v-spacer />
              <v-btn color="primary">Register</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>
