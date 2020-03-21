<template>
  <div>
    <v-content>
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
              <v-card-text>
                <h1 class="display-4">WerkIt</h1>
              </v-card-text>
              <v-card-text>
                <p class="display-1">WerkIt is a lightweight task management application</p>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn class="primary" to="/authentication">Sign In</v-btn>
                <v-btn class="primary" to="/registration">Get Started</v-btn>
                <v-spacer />
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </div>
</template>

<script>

</script>

<style>

</style>
