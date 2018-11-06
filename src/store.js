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
    ]
  },
  getters: {
    projects: state => {
      return state.projects
    }
  },
  plugins: [vuexLocal.plugin]
})
