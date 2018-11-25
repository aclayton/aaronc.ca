<template>
  <div class="home">
    <app-home-header
      v-waypoint="{ active: true, callback: toggleShow, options: waypointOptions }"
    ></app-home-header>
    <app-recent-projects></app-recent-projects>
    <app-about></app-about>
    <app-contact></app-contact>
    <app-footer></app-footer>
    <app-scroll-to-top
      :class="ui.menuActive ? 'active' : ''"
    ></app-scroll-to-top>
  </div>
</template>
<script>
import AppHomeHeader from '@/components/AppHomeHeader.vue'
import AppRecentProjects from '@/components/AppRecentProjects.vue'
import AppAbout from '@/components/AppAbout.vue'
import AppContact from '@/components/AppContact.vue'
import AppFooter from '@/components/AppFooter.vue'
import AppScrollToTop from '@/components/AppScrollToTop.vue'
import { mapGetters } from 'vuex'

export default {
  components: {
    AppHomeHeader,
    AppRecentProjects,
    AppAbout,
    AppContact,
    AppFooter,
    AppScrollToTop
  },
  data() {
    return {
      waypointOptions: {
        rootMargin: '-10px'
      }
    }
  },
  computed: {
    ...mapGetters([
      'ui'
    ])
  },
  methods: {
    toggleShow({ going, direction }) {
      if (going === this.$waypointMap.GOING_OUT) {
        this.$store.commit('UPDATE_UI_MENU', true)
      } else if (going === this.$waypointMap.GOING_IN && direction) {
        this.$store.commit('UPDATE_UI_MENU', false)
      }
    }
  }
}
</script>
