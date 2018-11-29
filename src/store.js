import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

import svgMachine from './html/svg-machine.html'

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [vuexLocal.plugin],
  state: {
    projects: [
      {
        _id: 1,
        name: 'svg-machine.com',
        url: 'svg-machine',
        imgMain: '/img/svg-machine.png',
        descShort: 'A little app to help make libraries of svgs, and export definition files.',
        descLong: svgMachine,
        githubLink: 'https://github.com/aclayton/svg-machine',
        projectLink: 'https://www.svg-machine.com',
        scrollToId: '#project-2',
        scrollToText: 'Next',
        cardClass: '',
        active: false
      },
      {
        _id: 2,
        name: 'More to come',
        imgMain: '/img/Octocat.png',
        githubLink: 'https://github.com/aclayton',
        descShort: `There's more to come, but in the meantime check out my GitHub.`,
        cardClass: '',
        active: false
      }
    ],
    ui: {
      menuActive: false
    },
    skills: [
      { _id: 1,   name: 'git' },
      { _id: 2,   name: 'babel' },
      { _id: 3,   name: 'node' },
      { _id: 4,   name: 'javascript' },
      { _id: 5,   name: 'cordova' },
      { _id: 6,   name: 'oauth' },
      { _id: 7,   name: 'mongo' },
      { _id: 8,   name: 'material' },
      { _id: 9,   name: 'angular' },
      { _id: 10,  name: 'express' },
      { _id: 11,  name: 'bootstrap' },
      { _id: 12,  name: 'sass' },
      { _id: 13,  name: 'vuejs' },
      { _id: 14,  name: 'ubuntu' },
      { _id: 15,  name: 'webpack' },
      { _id: 16,  name: 'html5' }
    ]
  },
  mutations: {
    UPDATE_UI_MENU (state, value) {
      state.ui.menuActive = value
    },
    SET_INACTIVE_PROJECT (state, id) {
      state.projects.find(project => project._id === id ).active = false
    },
    SET_ACTIVE_PROJECT (state, id) {
      state.projects.find(project => project._id === id ).active = true
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
    activeProject: state => {
      return state.projects.find(project => project.active === true)
    },
    ui: state => {
      return state.ui
    },
    skills: state => {
      return state.skills
    }
  }
})
