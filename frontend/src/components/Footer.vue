<template>
  <v-footer
    padless
    dark
    class="primary"
  >
    <v-col
      class="text-left"
      cols="6"
    >
      <img
        src="@/assets/logos/vector/default-monochrome-white.svg"
        alt="Logo"
        height="30"
      />
      <v-row>
        <v-btn x-small text link>Terms</v-btn>
      </v-row>
      <v-row>
        <v-btn x-small text link>Privacy policy</v-btn>
      </v-row>
      <v-row>
        <v-btn x-small text link>Cookies</v-btn>
      </v-row>
      <v-row>
        <v-btn x-small text link>Ads info</v-btn>
      </v-row>
    </v-col>
    <v-col
      class="text-right"
      cols="6"
    >
      <v-spacer/>
      <v-btn text link href="http://weirichard.com" target="_blank">
        {{ new Date().getFullYear() }} - Richard Wei
      </v-btn>
    </v-col>
  </v-footer>
</template>

<style>

</style>
