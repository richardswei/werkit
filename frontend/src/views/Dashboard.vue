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
      <v-card
        outlined
        dense
        v-for="(item, index) in todoItems"
        :key="index"
      >
        <v-row no-gutters>
          <v-col cols="11">
            <v-list-item>
              <v-list-item-avatar
                :color="getPriorityColor(item.priority)"
              ></v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title>{{item.title}}</v-list-item-title>
                <v-list-item-subtitle>
                  Due: {{item.dueDate}} - {{item.dueTime}}
                </v-list-item-subtitle>
                <v-list-item-subtitle>
                  {{item.description}}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
          <v-col
            cols="auto"
            class="ml-auto mr-1"
          >
            <v-btn small icon color="teal">
              <v-icon>mdi-check</v-icon>
            </v-btn>
            <br>
            <v-btn small icon color="grey">
              <v-icon>mdi-square-edit-outline</v-icon>
            </v-btn>
            <br>
            <v-btn small icon color="red">
              <v-icon>mdi-close</v-icon>
            </v-btn>

          </v-col>
        </v-row>
      </v-card>

      <v-dialog
        class="editDialog"
        ref="editDialog"
        v-model="editDialog.show"
        max-width="600px"
      >
        <v-card>
          <v-container>
            <v-text-field
              v-model="editDialog.data.title"
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
                    @click.stop="toggleDatePicker(editDialog.data.dueDate)"
                  >
                    <v-icon>event</v-icon>
                  </v-btn>
                  <v-text-field
                    v-model="editDialog.data.dueDate"
                    label="Due Date"
                  ></v-text-field>
                </div>
              </v-col>
              <v-col cols="6">
                <div class="d-flex align-center">
                  <v-btn
                    text
                    depressed
                    @click.stop="toggleTimePicker(editDialog.data.id, editDialog.data.dueTime)"
                  >
                    <v-icon>access_time</v-icon>
                  </v-btn>
                  <v-text-field
                    v-model="editDialog.data.dueTime"
                    label="Due Time"
                  ></v-text-field>
                </div>
              </v-col>
            </v-row>
            <v-textarea
              v-model="editDialog.data.description"
              label="Description"
              filled
              dense
              auto-grow
              rows="3"
            ></v-textarea>
            <p>
              <span class="text--secondary">Priority: </span>
              <v-btn-toggle
                v-model="editDialog.data.priority"
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
                Last modified: {{editDialog.data.updated
                  ? (new Date(editDialog.data.updated)).toLocaleString()
                  : 'Never'}}
              </div>
              <v-spacer></v-spacer>
              <v-btn
                @click.stop="saveTodo(editDialog.data)"
              >Save</v-btn>
              <v-btn
                color="blue darken-1"
                @click.stop="editDialog.show=false"
              >Close</v-btn>
            </div>
          </v-container>
        </v-card>
      </v-dialog>

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
    editDialog: {
      data: {},
      show: false,
    },
    datePicker: {
      due: null,
      show: false,
    },
    timePicker: {
      due: null,
      show: false,
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
    toggleDatePicker(due) {
      // format for picker needs to be YYYY-MM-DD
      const formattedDate = moment(due).format('YYYY-MM-DD');
      this.datePicker = {
        due: formattedDate,
        show: true,
      };
    },
    toggleTimePicker(due) {
      // using fake date as placeholder
      // format for picker needs to be HH:MM
      const formattedTime = moment(`1/1/11 ${due}`).format('HH:mm');
      this.timePicker = {
        due: formattedTime,
        show: true,
      };
    },
    setDate() {
      this.editDialog.data.dueDate = moment(this.datePicker.due).format('L');
      this.datePicker.show = false;
    },
    setTime() {
      this.$refs.timeDialog.save(this.timePicker.due);
      this.timePicker.show = false;
      const momentObj = moment(`1/1/11 ${this.timePicker.due}`);
      // reformat to ui's display format
      this.editDialog.data.dueTime = momentObj.format('LT');
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
      };
      console.log(todo);
      this.editDialog.data = todo;
      this.editDialog.show = true;
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
          if (item.id) {
            this.todoItems[index].id = response.data.id;
          } else {
            const todoItem = {
              id: response.data.id,
              created: response.data.created,
              updated: response.data.updated,
              title: response.data.title,
              description: response.data.description,
              user_id: response.data.user_id,
              priority: Object.keys(this.priorities)[response.data.priority],
              dueDate: moment(response.data.due).format('L'),
              dueTime: moment(response.data.due).format('LT'),
            };
            this.todoItems.unshift(todoItem);
            this.editDialog.show = false;
          }
        }, (error) => {
          console.log(error);
        });
    },
    deleteTodo(item, index) {
      const config = {
        method: 'delete',
        url: `http://localhost:8000/api/v1/todoitems/${item.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      };
      axios(config)
        .then((response) => {
          console.log(response);
          // close todo after successful deletion
          this.todoItems.splice(index, 1);
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
