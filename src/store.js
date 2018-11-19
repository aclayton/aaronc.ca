import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    projects: [
      {
        _id: 1,
        name: 'svg-machine.com',
        imgMain: '/img/svg-machine.png',
        descShort: 'A little app to help make libraries of svgs, and export definition files.',
        descLong: '',
        githubLink: 'https://github.com/aclayton/svg-machine',
        projectLink: 'https://www.svg-machine.com',
        scrollToId: '#project-2',
        scrollToText: 'Next',
        cardClass: ''
      },
      {
        _id: 2,
        name: 'More to come',
        imgMain: '/img/Octocat.png',
        githubLink: 'https://github.com/aclayton',
        // scrollToId: '#header-home',
        // scrollToText: 'Next',
        descShort: `There's more to come, but in the mean time check out my GitHub.`,
        cardClass: ''
      },
      // {
      //   _id: 3,
      //   name: 'Nia Data Exchange',
      //   scrollToId: '#header-home',
      //   scrollToText: 'Top'
      // }
    ],
    ui: {
      menuActive: true
    },
    availability: {
      msg: 'Aaron is a self-motivated web development professional, available for hire, or projects large and small.'
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
        return ['col-10', 'col-md-4', 'col-lg-3', 'animated', 'slideInLeft']
      }
    },
    availability: state => {
      return state.availability
    }
  }
})
