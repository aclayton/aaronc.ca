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
        descShort: `There's more to come, but in the mean time check out my GitHub.`,
        cardClass: ''
      }
    ],
    ui: {
      menuActive: false
    },
    skills: [
      { _id: 1,   name: 'git',        img_src: '/img/logos/git.png' },
      { _id: 2,   name: 'babel',      img_src: '/img/logos/babel.png' },
      { _id: 3,   name: 'node',       img_src: '/img/logos/nodejs.png' },
      { _id: 4,   name: 'javascript', img_src: '/img/logos/js.jpg' },
      { _id: 5,   name: 'cordova',    img_src: '/img/logos/cordova.png' },
      { _id: 6,   name: 'oauth',      img_src: '/img/logos/oauth.png' },
      { _id: 7,   name: 'mongo',      img_src: '/img/logos/mongodb.jpg' },
      { _id: 8,   name: 'material',   img_src: '/img/logos/materialdesign.png' },
      { _id: 9,   name: 'angular',    img_src: '/img/logos/angularjs.png' },
      { _id: 10,  name: 'express',    img_src: '/img/logos/express.png' },
      { _id: 11,  name: 'bootstrap',  img_src: '/img/logos/bootstrap.png' },
      { _id: 12,  name: 'sass',       img_src: '/img/logos/sass.png' },
      { _id: 13,  name: 'vuejs',      img_src: '/img/logos/vuejs.png' },
      { _id: 14,  name: 'ubuntu',     img_src: '/img/logos/ubuntu.png' },
      { _id: 15,  name: 'webpack',    img_src: '/img/logos/webpack.png' },
      { _id: 16,  name: 'html5',      img_src: '/img/logos/html5.png' }
    ]
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
    skills: state => {
      return state.skills
    }
  }
})
