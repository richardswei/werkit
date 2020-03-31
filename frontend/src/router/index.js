import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import store from '../store';

Vue.use(VueRouter);

function guard(to, from, next) {
  if (store.state.token) {
    // or however you store your logged in state
    next(); // allow to enter route
  } else {
    next('/signin'); // go to '/signin';
  }
}

function alreadyLoggedIn(to, from, next) {
  if (store.state.token) {
    next('/app/dashboard');
  } else {
    next();
  }
}

const routes = [
  {
    path: '/',
    beforeEnter: alreadyLoggedIn,
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/app',
    name: 'MainApp',
    beforeEnter: guard,
    component: () => import('../views/EmptyRouterView.vue'),
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () => import('../views/Dashboard.vue'),
      },
      {
        path: 'profile',
        name: 'Profile',
        component: () => import('../views/Profile.vue'),

      },
    ],
  },
  {
    path: '/signin',
    name: 'Sign In',
    component: () => import('../views/Authentication.vue'),
  },
  {
    path: '/registration',
    name: 'New Account',
    component: () => import('../views/Registration.vue'),
  },
  {
    path: '/404',
    component: () => import('../views/NotFound.vue'),
  },
  { path: '*', redirect: '/404' },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
