import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

export default new Vuex.Store({
  state: {
    projects: [
      {
        _id: 1,
        name: 'svg-machine.com',
        imgMain: '/img/svg-machine.png',
        descShort: 'A little app to help make libraries of svg files, and export definition files.',
        descLong: '',
        githubLink: 'https://github.com/aclayton/svg-machine',
        projectLink: 'https://www.svg-machine.com'
      },
      {
        _id: 2,
        name: 'The Logo'
      },
      {
        _id: 3,
        name: 'Nia Data Exchange'
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
    projectById: state => {
      return id => {
        return state.projects.find(project => project._id === id)
      }
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
