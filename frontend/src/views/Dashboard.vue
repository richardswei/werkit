<template>
  <div
    class="overflow-hidden"
    style="position: relative;"
  >
    <v-container fluid>
      <v-toolbar
        dense
        dark
        class="primary"
      >
        <v-app-bar-nav-icon>
          <v-icon>dashboard</v-icon>
        </v-app-bar-nav-icon>
        <v-toolbar-title>Todo Dashboard</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>
        <v-btn
          icon
          @click.stop="addTodo()"
        ><v-icon>mdi-plus</v-icon></v-btn>
      </v-toolbar>
      <v-expansion-panels
        v-model="expanded"
      >
        <v-expansion-panel
          v-for="(item, index) in todoitems"
          :key="index"
        >
          <v-expansion-panel-header>
            <template v-slot:default="{ open }">
              <v-fade-transition leave-absolute>
                <v-row no-gutters>
                  <v-col cols="3" class="text--secondary">
                    <span v-if="open" key="0" >
                      Edit Mode
                    </span>
                    <span v-else key="1" >
                      Due: {{item.dueDate}} @ {{item.dueTime}}
                    </span>
                  </v-col>
                  <v-col cols="8" class="text--secondary">
                    <span v-if="open" key="0" >
                    </span>
                    <span v-else key="1" >
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
            <v-row>
              <v-col cols="6">
                <div class="d-flex align-center">
                  <v-btn
                    text
                    depressed
                    @click.stop="toggleDatePicker(item.id, item.dueDate)"
                  >
                    <v-icon>event</v-icon>
                  </v-btn>
                  <v-text-field
                    v-model="item.dueDate"
                    label="Due Date"
                  ></v-text-field>
                </div>
              </v-col>
              <v-col cols="6">
                <div class="d-flex align-center">
                  <v-btn
                    text
                    depressed
                    @click.stop="toggleTimePicker(item.id, item.dueTime)"
                  >
                    <v-icon>access_time</v-icon>
                  </v-btn>
                  <v-text-field
                    v-model="item.dueTime"
                    label="Due Time"
                  ></v-text-field>
                </div>
              </v-col>
            </v-row>
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
                mandatory
                dense
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
            <div>
              <div class="text--secondary">
                Last modified: {{(new Date(item.updated)).toLocaleString()}}
              </div>
              <v-spacer></v-spacer>
              <v-btn
                @click.stop="saveTodo(item)"
              >Save</v-btn>
            </div>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
      <v-dialog
        ref="dateDialog"
        v-model="datePicker.show"
        :return-value.sync="datePicker.due"
        width="290px"
      >
        <v-date-picker v-model="datePicker.due" scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="datePicker.show=false">Cancel</v-btn>
          <v-btn text color="primary" @click="setDate()">OK</v-btn>
        </v-date-picker>
      </v-dialog>
      <v-dialog
        ref="timeDialog"
        v-model="timePicker.show"
        :return-value.sync="timePicker.due"
        width="290px"
      >
        <v-time-picker
          v-model="timePicker.due"
          v-if="timePicker.show"
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="timePicker.show=false">Cancel</v-btn>
          <v-btn text color="primary" @click="setTime()">OK</v-btn>
        </v-time-picker>
      </v-dialog>
    </v-container>
  </div>
</template>
<script>
import axios from 'axios';
import moment from 'moment';

export default {
  name: 'Dashboard',
  created() {
    this.getTodos();
  },
  data: () => ({
    expanded: null,
    datePicker: {
      due: null,
      show: false,
      itemId: null,
    },
    timePicker: {
      due: null,
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
      // format for picker needs to be YYYY-MM-DD
      const formattedDate = moment(due).format('YYYY-MM-DD');
      this.datePicker = {
        due: formattedDate,
        show: true,
        itemId,
      };
    },
    toggleTimePicker(itemId, due) {
      // using fake date as placeholder
      // format for picker needs to be HH:MM
      const formattedTime = moment(`1/1/11 ${due}`).format('HH:mm');
      this.timePicker = {
        due: formattedTime,
        show: true,
        itemId,
      };
    },
    setDate() {
      const index = this.todoitems.findIndex((element) => element.id
        === this.datePicker.itemId);
      // reformat to ui's display format
      this.todoitems[index].dueDate = moment(this.datePicker.due).format('L');
      this.datePicker.show = false;
    },
    setTime() {
      const index = this.todoitems.findIndex((element) => element.id
        === this.timePicker.itemId);
      // using fake date as placeholder
      this.$refs.timeDialog.save(this.timePicker.due);
      this.timePicker.show = false;
      const momentObj = moment(`1/1/11 ${this.timePicker.due}`);
      // reformat to ui's display format
      this.todoitems[index].dueTime = momentObj.format('LT');
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
          const todoitems = response.data.map((item) => ({
            id: item.id,
            created: item.created,
            updated: item.updated,
            title: item.title,
            description: item.description,
            user_id: item.user_id,
            priority: Object.keys(this.priorities)[item.priority],
            dueDate: moment(item.due).format('L'),
            dueTime: moment(item.due).format('LT'),
          }));
          this.todoitems = todoitems;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    addTodo() {
      const todo = {
        title: '',
        description: '',
        priority: Object.keys(this.priorities)[0],
        dueDate: moment().add(1, 'day').format('L'),
        dueTime: moment().add(1, 'hour').format('LT'),
      };
      this.todoitems.unshift(todo);
      console.log(this.todoitems.map((item) => item.title));
      this.expanded = 0;
      console.log(this.expanded);
    },
    saveTodo(item) {
      const payloadKeys = [
        'due',
        'title',
        'description',
        'priority',
      ];
      const payload = Object.fromEntries(
        Object.entries(item)
          .filter(([key]) => payloadKeys.includes(key)),
      );
      payload.priority = Object.keys(this.priorities).indexOf(item.priority);
      payload.due = moment(`${item.dueDate} ${item.dueTime}`).toJSON();
      // if item doesnt have an id it's new.
      const config = {
        method: item.id ? 'put' : 'post',
        url: item.id
          ? `http://localhost:8000/api/v1/todoitems/${item.id}/`
          : 'http://localhost:8000/api/v1/todoitems/',
        data: payload,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      };
      axios(config)
        .then((response) => {
          console.log(response);
        }, (error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style>
.v-btn--active .v-btn__content {
  font-weight: bolder;
  font-style: italic;
}
</style>
