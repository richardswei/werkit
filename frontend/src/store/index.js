import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersist from 'vuex-persist';
// import axios from 'axios';

Vue.use(Vuex);

const vuexLocalStorage = new VuexPersist({
  key: 'vuex', // The key to store the state on in the storage provider.
  storage: window.localStorage, // or window.sessionStorage or localForage
  // Function that passes the state and returns the state with only the objects you want to store.
  // reducer: state => state,
  reducer: (state) => ({
    token: state.token,
    user: state.user,
  }),
  // Function that passes a mutation and
  // lets you decide if it should update the state in localStorage.
  // filter: mutation => (true)
});

export default new Vuex.Store({
  state: {
    token: null,
    drawer: false,
    user: {
      username: 'Username',
      first_name: 'First Name',
      last_name: 'Last Name',
      email: 'user@email.com',
    },
  },
  getters: {
    drawerState: (state) => state.drawer,
    token: (state) => state.token,
    user: (state) => state.user,
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token;
    },
    SET_USER(state, user) {
      state.user = user;
    },
    UNSET_TOKEN(state) {
      state.token = null;
    },
    TOGGLE_DRAWER(state) {
      state.drawer = !state.drawer;
    },
    CLOSE_DRAWER(state) {
      state.drawer = false;
    },
  },
  actions: {
    setsession({ commit }, authPayload) {
      commit('SET_TOKEN', authPayload.token);
      commit('SET_USER', authPayload.user);
    },
    signout({ commit }) {
      commit('UNSET_TOKEN');
    },
    togglemenu({ commit }) {
      commit('TOGGLE_DRAWER');
    },
    close_menu({ commit }) {
      commit('CLOSE_DRAWER');
    },
  },
  modules: {
  },
  plugins: [vuexLocalStorage.plugin],
  strict: process.env.NODE_ENV !== 'production',
});
