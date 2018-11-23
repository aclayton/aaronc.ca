<template>
    <div id="app">
      <app-home-header
        v-waypoint="{ active: true, callback: onWaypoint, options: waypointOptions }"
      ></app-home-header>
      <app-recent-projects></app-recent-projects>
      <app-about></app-about>
      <app-contact></app-contact>
      <app-footer></app-footer>
      <app-scroll-to-top :class="show ? 'active' : ''"></app-scroll-to-top>
    </div>
</template>

<script>
import AppHomeHeader from '@/components/HomeHeader.vue'
import AppRecentProjects from '@/components/RecentProjects.vue'
import AppAbout from '@/components/About.vue'
import AppContact from '@/components/ContactComponent.vue'
import AppFooter from '@/components/Footer.vue'
import AppScrollToTop from '@/components/scrollToTop.vue'

export default {
  data() {
    return {
      show: false,
      waypointOptions: {
        rootMargin: '-10px'
      }
    }
  },
  components: {
    AppHomeHeader,
    AppRecentProjects,
    AppAbout,
    AppContact,
    AppFooter,
    AppScrollToTop
  },
  methods: {
    onWaypoint({ going, direction }) {
      console.log('going', going, 'direction', direction)
      if (going === this.$waypointMap.GOING_OUT) {
        this.show = true
      } else if (going === this.$waypointMap.GOING_IN && direction) {
        this.show = false
      }
    }
  }
}
</script>

<style lang="scss">
@import 'styles/index.scss';
</style>
