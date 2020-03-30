<template>
  <v-sheet
    class="overflow-hidden"
    style="position: relative;"
  >
    <v-container class="fill-height">
      <v-row
        align="center"
        justify="center"
      >
      </v-row>
    </v-container>
    <NavDrawer/>
  </v-sheet>
</template>
<script>
import NavDrawer from '@/components/NavDrawer.vue';

export default {
  name: 'Dashboard',
  components: {
    NavDrawer,
  },
  methods: {
    itemClick() {
      this.$store.dispatch('togglemenu');
    },
  },
};
</script>
