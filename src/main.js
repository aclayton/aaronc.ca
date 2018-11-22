import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Icon from 'vue-awesome/components/Icon.vue'
import VueScrollTo from 'vue-scrollto'
import VueAnime from './anime'

Vue.use(VueAnime)
Vue.use(BootstrapVue)
Vue.use(VueScrollTo)
Vue.component('icon', Icon)

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {

  if (window.innerWidth < 768) {
    store.commit('UPDATE_UI_MENU', false)
  } else {
    store.commit('UPDATE_UI_MENU', true)
  }

  next()
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
