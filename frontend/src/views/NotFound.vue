<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" lg="4">
        <v-card
          class="mx-auto"
          outlined
        >
          <v-card-title class="text-center display-3">
            <v-spacer/>
              404 Not Found
            <v-spacer/>
          </v-card-title>
          <v-card-text>Oops, that page couldn't be found</v-card-text>
          <v-card-actions>
            <v-spacer/>
            <v-btn class="link" to="/">Get back to Werk</v-btn>
            <v-spacer/>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
