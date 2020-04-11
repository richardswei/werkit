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
                    cols="3"
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
                    cols="8"
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
                      <div text-truncate>
                        <strong>{{item.title}}</strong> - {{item.description}}
                      </div>
                    </span>
                  </v-col>
                  <v-col cols="1" >
                    <v-chip
                      x-small
                      :color="getPriorityColor(item.priority)"
                    >
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
            <v-text-field
              v-model="item.due"
              label="Picker in menu"
              prepend-icon="event"
              readonly
              @click.stop="toggleDatePicker(item.id, item.due)"
            ></v-text-field>
            <v-textarea
              v-model="item.description"
              label="Description"
              filled
              dense
              auto-grow
              rows="3"
            ></v-textarea>
            <p>
              <span class="text--secondary">Priority: </span>
              <v-btn-toggle
                v-model="item.priority"
                active-class
                mandatory
                dense
                light
              >
                <v-btn
                  v-for="(value, name) in priorities"
                  small
                  :key="name"
                  :value="name"
                  :color="value"
                >
                  <div>{{name}}</div>
                </v-btn>
              </v-btn-toggle>
            </p>
            <div class="text--secondary">Last modified: {{item.updated}}</div>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
      <v-dialog
        ref="dialog"
        v-model="datePicker.show"
        :return-value.sync="datePicker.date"
        width="290px"
      >
        <v-date-picker v-model="datePicker.date" scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="datePicker.show = false">Cancel</v-btn>
          <v-btn text color="primary" @click="setDate()">OK</v-btn>
        </v-date-picker>
      </v-dialog>
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
    datePicker: {
      date: null,
      show: false,
      itemId: null,
    },
    todoitems: [],
    priorities: {
      normal: 'green',
      priority: 'yellow',
      urgent: 'orange',
      critical: 'red',
    },
  }),
  methods: {
    toggleDatePicker(itemId, due) {
      this.datePicker = {
        date: due,
        show: true,
        itemId,
      };
    },
    setDate() {
      const index = this.todoitems.findIndex((element) => element.id === this.datePicker.itemId);
      this.todoitems[index].due = this.datePicker.date;
      this.datePicker = {
        due: null,
        show: false,
        itemId: null,
      };
    },
    getPriorityColor(priority) {
      return this.priorities[priority];
    },
    getTodos() {
      axios.get('http://localhost:8000/api/v1/todoitems/', {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          const todoitems = response.data.map((item) => ({ ...item, due: '2020-04-02' }));
          console.log(response.data);
          this.todoitems = todoitems;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
