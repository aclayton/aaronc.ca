<template>
  <b-container fluid id="app">
    <b-row>

      <div :class="navClasses" id="nav-side-blocker"></div>
      <div :class="navClasses" id="nav-side">
        <navigation></navigation>
        <availability />
      </div>
      <div @click="toggleNav" v-if="ui.menuActive" id="nav-side-shade"></div>

      <b-col id="page-side">
        <div class="mobile-toggle" style="text-align: right;">
          <b-btn @click="toggleNav" variant="link">
            <icon name="ellipsis-v"/>
          </b-btn>
        </div>
        <router-view/>
      </b-col>

    </b-row>
  </b-container>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
import Availability from '@/components/Availability'
import 'vue-awesome/icons/ellipsis-v'
import 'vue-awesome/icons/file-download'
import { mapGetters } from 'vuex'

export default {
  components: {
    Navigation,
    Availability
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
