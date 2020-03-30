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
        lg="4"
      >
        <HomeWelcome/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import HomeWelcome from '@/components/HomeWelcome.vue';

export default {
  name: 'Home',
  components: {
    HomeWelcome,
  },
};
</script>
