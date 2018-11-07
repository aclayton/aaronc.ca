import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  supportCircular: true,
  storage: window.localStorage
})

export default new Vuex.Store({
  state: {
    projects: [
      {
        _id: 1,
        name: 'logo',
        imgMain: '/img/ac.svg',
        descShort: 'More to come...',
        descLong: '',
        githubLink: '',
        projectLink: '',
        insideLink: 'projects/ac-logo'
      }
    ],
    ui: {
      menuActive: true
    },
    availability: {
      msg: 'Aaron is currently available for hire.'
    }
  },
  mutations: {
    UPDATE_UI_MENU (state, value) {
      state.ui.menuActive = value
    }
  },
  getters: {
    projects: state => {
      return state.projects
    },
    ui: state => {
      return state.ui
    },
    navClasses: state => {
      if (!state.ui.menuActive) {
        return ['animated', 'slideOutLeft']
      } else {
        return ['col-10', 'col-md-4', 'col-lg-4', 'animated', 'slideInLeft']
      }
    },
    availability: state => {
      return state.availability
    }
  },
  plugins: [vuexLocal.plugin]
})
