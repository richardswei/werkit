import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    count: 0,
    token: null,
    drawer: false,
    // profile: null,
  },
  getters: {
    drawerState: (state) => state.drawer,
  },
  mutations: {
    INCREMENT(state) {
      state.count += 1;
    },
    SET_TOKEN(state, token) {
      state.token = token;
    },
    UNSET_TOKEN(state) {
      state.token = null;
    },
    TOGGLE_DRAWER(state) {
      state.drawer = !state.drawer;
    },
  },
  actions: {
    signin({ commit }, account) {
      commit('SET_TOKEN', account);
    },
    signout({ commit }) {
      commit('UNSET_TOKEN');
    },
    togglemenu({ commit }) {
      commit('TOGGLE_DRAWER');
    },
  },
  modules: {
  },
  strict: process.env.NODE_ENV !== 'production',
});
