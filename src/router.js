import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import PortfolioItem from './views/PortfolioItem.vue'

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
      path: '/portfolio/:_id',
      name: 'PortfolioItem',
      component: PortfolioItem
    }
  ]
})
