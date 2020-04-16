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
        accordion
        v-model="expanded"
      >
        <v-expansion-panel
          v-for="(item, index) in todoItems"
          :key="index"
        >
          <v-expansion-panel-header>
            <template v-slot:default="{ open }">
              <v-fade-transition leave-absolute>
                <v-row dense >
                  <v-col
                    cols="auto"
                    class="text--primary"
                  >
                    <span
                      v-if="open"
                      key="0"
                    >
                      Edit Mode
                    </span>
                    <span v-else key="1" >
                      Due: {{item.dueDate}}
                      <br>
                      {{item.dueTime}}
                    </span>
                  </v-col>
                  <v-col v-if="open" key="0">
                  </v-col>
                  <v-col v-else key="1" cols="9" class="text--secondary">
                    <strong class="text--primary">{{item.title}}</strong>
                    - {{item.description}}
                  </v-col>
                  <v-col
                    cols="auto"
                    class="ml-auto mt-0"
                  >
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
          <v-expansion-panel-content
            class="editMode"
          >
            <v-text-field
              v-model="item.title"
              label="Title"
              filled
              dense
              class="pt-3"
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
                @click.stop="saveTodo(item, index)"
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
    todoItems: [],
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
      const index = this.todoItems.findIndex((element) => element.id
        === this.datePicker.itemId);
      // reformat to ui's display format
      this.todoItems[index].dueDate = moment(this.datePicker.due).format('L');
      this.datePicker.show = false;
    },
    setTime() {
      const index = this.todoItems.findIndex((element) => element.id
        === this.timePicker.itemId);
      // using fake date as placeholder
      this.$refs.timeDialog.save(this.timePicker.due);
      this.timePicker.show = false;
      const momentObj = moment(`1/1/11 ${this.timePicker.due}`);
      // reformat to ui's display format
      this.todoItems[index].dueTime = momentObj.format('LT');
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
          const todoItems = response.data.map((item) => ({
            id: item.id,
            created: item.created,
            updated: item.updated,
            title: item.title,
            description: item.description,
            user_id: item.user_id,
            priority: Object.keys(this.priorities)[item.priority],
            dueDate: moment(item.due).format('L'),
            dueTime: moment(item.due).format('LT'),
            unsaved: false,
          }));
          this.todoItems = todoItems;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    addTodo() {
      const todo = {
        id: null,
        created: null,
        updated: null,
        title: '',
        description: '',
        priority: Object.keys(this.priorities)[0],
        dueDate: moment().add(1, 'day').format('L'),
        dueTime: moment().add(1, 'hour').format('LT'),
        unsaved: true,
      };
      // add empty todo to top of list
      this.todoItems.unshift(todo);
      // open the most recently added item
      this.expanded = 0;
    },
    saveTodo(item, index) {
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
          // close todo after successfully saving
          this.todoItems[index].unsaved = false;
          this.todoItems[index].id = response.data.id;
          this.expanded = null;
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
.editMode {
  background-color: rgba(226,220,205,0.2);
}
</style>
