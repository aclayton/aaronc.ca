<template>
  <div id="project-page">
    <header>
      <div class="container">
        <h1>{{ activeProject.name }}</h1>
        <p>{{ activeProject.descShort }}</p>
      </div>
    </header>
    <div role="main" v-html="activeProject.descLong"></div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PortfolioItem',
  computed: {
    ...mapGetters([
      'activeProject'
    ])
  }
}
</script>
