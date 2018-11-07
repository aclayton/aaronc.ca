<template>
  <div id="project">
    PROJECT ITEM {{ $route.params._id }}

    Project Name: {{ currentProject.name }}
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'PortfolioItem',
  data() {
    return {
      currentProject: {}
    }
  },
  computed: {
    ...mapGetters([
      'projectById'
    ])
  },
  mounted() {
    this.currentProject = this.projectById(this.$route.params._id)
  }
}
</script>
