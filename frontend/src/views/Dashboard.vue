<template>
  <div
    class="overflow-hidden"
    style="position: relative;"
  >
    <v-container fluid>
      <v-expansion-panels>
        <v-expansion-panel
          v-for="item in todoitems"
          :key="item.id"
        >
          <v-expansion-panel-header>
            <template v-slot:default="{ open }">
              <v-fade-transition leave-absolute>
                <v-row no-gutters>
                  <v-col
                    cols="2"
                    class="text--secondary"
                  >
                    <span
                      v-if="open"
                      key="0"
                    >
                      Edit Mode
                    </span>
                    <span
                      v-else
                      key="1"
                    >
                      Due: {{item.due}}
                    </span>
                  </v-col>
                  <v-col
                    cols="9"
                    class="text--secondary"
                  >
                    <span
                      v-if="open"
                      key="0"
                    >
                    </span>
                    <span
                      v-else
                      key="1"
                    >
                      <v-header><strong>{{item.title}}</strong> - {{item.description}}</v-header>
                    </span>
                  </v-col>
                  <v-col cols="1" >
                    <v-chip small>
                      {{item.priority}}
                    </v-chip>
                  </v-col>
                </v-row>
              </v-fade-transition>
            </template>
            <template v-slot:actions>
              <v-icon color="primary">expand_more</v-icon>
            </template>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-text-field
              v-model="item.title"
              label="Title"
              filled
              dense
            ></v-text-field>
            <v-select
              v-model="item.priority"
              :items="priorities"
              label="Priority"
              filled
              dense
              chips
              flat
            ></v-select>
            <v-btn-toggle
              v-model="item.priority"
              mandatory
              dense
            >
              <v-btn
                v-for="choice in color"
                :key="choice"
                :value="choice"
                :color="choice"
              >
                <v-text>{{choice}}</v-text>
              </v-btn>
            </v-btn-toggle>
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="date"
                  label="Picker without buttons"
                  prepend-icon="event"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
            </v-menu>
            <v-textarea
              v-model="item.description"
              label="Description"
              filled
              dense
              auto-grow
              rows="3"
            ></v-textarea>
            <div>Last modified: {{item.updated}}</div>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Dashboard',
  created() {
    this.getTodos();
  },
  data: () => ({
    date: null,
    todoitems: [],
    priorities: ['normal', 'urgent', 'critical'],
    color: ['success', 'purple', 'yellow'],
  }),
  methods: {
    getTodos() {
      axios.get('http://localhost:8000/api/v1/todoitems/', {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          console.log(response.data);
          this.todoitems = response.data;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
