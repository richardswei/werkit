<template>
  <div
    class="overflow-hidden"
    style="position: relative;"
  >
    <v-container class="fill-height">
      <v-row
        align="center"
        justify="center"
      >
        <v-card
          class="mx-auto"
          max-width="434"
          tile
        >
          <v-img
            height="100%"
            src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
          >
            <v-row
              align="end"
              class="fill-height"
            >
              <v-col
                align-self="start"
                class="pa-0"
                cols="12"
              >
                <v-avatar
                  class="profile"
                  color="grey"
                  size="164"
                  tile
                >
                  <v-img src="/apple-icon-152x152.png"></v-img>
                </v-avatar>
              </v-col>
              <v-col class="py-0">
                <v-list-item
                  color="rgba(0, 0, 0, .4)"
                  dark
                >
                  <v-list-item-content>
                    <v-list-item-title class="title">
                      {{user.first_name}} {{user.last_name}}
                    </v-list-item-title>
                    <v-list-item-subtitle>{{user.username}}</v-list-item-subtitle>
                    <v-list-item-subtitle>{{user.email}}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-col>
            </v-row>
          </v-img>
        </v-card>
      </v-row>
    </v-container>
  </div>
</template>
<script>
export default {
  name: 'Profile',
  computed: {
    user: {
      get() {
        return this.$store.getters.user;
      },
      set() {

      },
    },
  },
};
</script>
