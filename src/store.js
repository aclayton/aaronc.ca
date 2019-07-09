import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'
import * as fireBase from './fireBase'
import axios from 'axios'

import svgMachine from './html/svg-machine.html'

const vuexLocal = new VuexPersistence({
  supportCircular: true,
  storage: window.localStorage
})

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [vuexLocal.plugin],
  state: {
    contactForm: {
      name: '', email: '', phone: '', message: '', date: new Date
    },
    alerts: [
      {
        type: 'messageError',
        variant: 'danger',
        message: 'Sorry, there was an error sending your message.',
        active: false
      },
      {
        type: 'messageSuccess',
        variant: 'success',
        message: 'Your message has been sent!',
        active: true
      }
    ],
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
        active: false,
        slides: [
          {
            _id: 1,
            caption: '',
            text: '',
            src: '/img/projects/svg-machine-start.png'
          }, {
            _id: 2,
            caption: '',
            text: '',
            src: '/img/projects/svg-machine-check.png'
          }
        ],
        color: {'background-color': '#181d23'}
      },
      {
        _id: 2,
        name: 'AC Logo',
        imgMain: '/img/ac-white.png',
        descShort: 'A logo of divine proportion',
        descLong: '',
        githubLink: '',
        projectLink: 'https://www.aaronc.ca',
        scrollToId: '',
        scrollToText: '',
        cardClass: '',
        active: false,
        slides: [
          {
            _id: 1,
            src: '/img/projects/logo-1.png',
            caption: '',
            text: ''
          }, {
            _id: 2,
            src: '/img/projects/logo-2.png',
            caption: '',
            text: ''
          }, {
            _id: 3,
            src: '/img/projects/logo-3.png',
            caption: '',
            text: ''
          }
        ],
        color: {'background-color': '#007bff'}
      },
      {
        _id: 3,
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
    },
    SET_INACTIVE_PROJECT (state, id) {
      state.projects.find(project => project._id === id ).active = false
    },
    SET_ACTIVE_PROJECT (state, id) {
      state.projects.find(project => project._id === id ).active = true
    },
    SET_ALERT (state, type) {
      state.alerts.find(alert => alert.type === type).active = true
    },
    CLEAR_ALERTS (state) {
      state.alerts.forEach(alert => alert.active = false)
    },
    CLEAR_CONTACT_FORM (state) {
      state.contactForm = { name: '', email: '', phone: '', message: '' }
    }
  },
  actions: {
    sendMessage (state) {
      this.state.contactForm.date = new Date
      const replyUrl = `https://us-central1-aaroncca-form-processor.cloudfunctions.net/responseMessage`
      const forwardUrl = `https://us-central1-aaroncca-form-processor.cloudfunctions.net/forwardMessage`
      const forwardAndReply = [
          axios.post(replyUrl, this.state.contactForm),
          axios.post(forwardUrl, this.state.contactForm)
      ]
      fireBase.messagesCollection.add(this.state.contactForm)
        .then(() => {
          Promise.all(forwardAndReply)
            .then(state.commit('SET_ALERT', 'messageSuccess'))
        })
        .catch(err => {
          state.commit('SET_ALERT', 'messageError')
          console.warn(err)
        })
    }
  },
  getters: {
    ui: state => state.ui,
    skills: state => state.skills,
    projects: state => state.projects,
    contactFormData: state => state.contactForm,
    activeAlerts: state => {
      return state.alerts.find(alert => alert.active === true)
    },
    projectById: state => {
      return id => {
        return state.projects.find(project => project._id === id)
      }
    },
    activeProject: state => {
      return state.projects.find(project => project.active === true)
    }
  }
})
