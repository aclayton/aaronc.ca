<template>
  <div class="home">
    <home-header />
    <recent-projects />
  </div>
</template>
<script>
import RecentProjects from '@/components/RecentProjects.vue'
import HomeHeader from '@/components/HomeHeader.vue'
export default {
  name: 'home',
  components: {
    RecentProjects,
    HomeHeader
  }
}
</script>
