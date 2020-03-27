import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    count: 0,
    token: null,
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
  },
  actions: {
    signin({ commit }, account) {
      commit('SET_TOKEN', account);
    },
    signout({ commit }) {
      commit('UNSET_TOKEN');
    },
  },
  modules: {
  },
  strict: process.env.NODE_ENV !== 'production',
});
