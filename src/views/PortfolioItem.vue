<template>
  <div v-if="projects.length" id="project">
    PROJECT ID: {{ $route.params._id }}<br />
    PROJECT NAME: {{ currentProject.name }}
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PortfolioItem',
  computed: {
    currentProject: function() {
      return this.projectById(this.$route.params._id)
    },
    ...mapGetters([
      'projectById',
      'projects'
    ])
  }
}
</script>
