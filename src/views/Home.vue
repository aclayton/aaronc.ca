<template>
  <div class="home">
    <app-home-header />
    <app-recent-projects />
  </div>
</template>
<script>
import AppRecentProjects from '@/components/AppRecentProjects.vue'
import AppHomeHeader from '@/components/AppHomeHeader.vue'
export default {
  name: 'home',
  components: {
    AppRecentProjects,
    AppHomeHeader
  }
}
</script>
