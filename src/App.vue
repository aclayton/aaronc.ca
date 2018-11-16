<template>
  <!-- <b-container fluid id="app" class="no-pad"> -->
    <div id="app">
      <app-home-header></app-home-header>
      <app-recent-projects></app-recent-projects>
      <app-about></app-about>
      <app-skills></app-skills>
      <app-learn-more></app-learn-more>
      <app-footer></app-footer>
    </div>
  <!-- </b-container> -->
</template>

<script>
import AppHomeHeader from '@/components/HomeHeader.vue'
import AppRecentProjects from '@/components/RecentProjects.vue'
import AppAbout from '@/components/About.vue'
import AppSkills from '@/components/Skills.vue'
import AppLearnMore from '@/components/LearnMore.vue'
import AppFooter from '@/components/Footer.vue'
import { mapGetters } from 'vuex'

export default {
  components: {
    AppHomeHeader,
    AppRecentProjects,
    AppAbout,
    AppSkills,
    AppLearnMore,
    AppFooter
  },
  computed: {
    ...mapGetters([
      'ui',
      'navClasses'
    ])
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener('resize', this.handleResize)
      this.handleResize()
    })
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize() {
      if (window.innerWidth < 768) {
        this.$store.commit('UPDATE_UI_MENU', false)
      } else {
        this.$store.commit('UPDATE_UI_MENU', true)
      }
    },
    toggleNav() {
      if (this.ui.menuActive == true) {
        this.$store.commit('UPDATE_UI_MENU', false)
      } else {
        this.$store.commit('UPDATE_UI_MENU', true)
      }
    }
  }
}
</script>

<style lang="scss">
@import 'styles/index.scss';
</style>
