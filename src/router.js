import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Success from './views/Success.vue'
import Failure from './views/Failure.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import(/* webpackChunkName: "contact" */ './views/Contact.vue')
    },
    {
      path: '/thanks',
      name: 'success',
      component: Success
    },
    {
      path: '/fail',
      name: 'fail',
      component: Failure
    },
    {
      path: '/project/:_id',
      name: 'project',
      component: () => import(/* webpackChunkName: "project" */ './views/PortfolioItem.vue')
    }
  ]
})
