import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Icon from 'vue-awesome/components/Icon.vue'
import VueScrollTo from 'vue-scrollto'
import VueWaypoint from 'vue-waypoint'

Vue.use(BootstrapVue)
Vue.use(VueScrollTo)
Vue.use(VueWaypoint)
Vue.component('icon', Icon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
