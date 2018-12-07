<template>
  <div id="project-page" :style="activeProject.color">
    <header>
      <div class="container">
        <h1>{{ activeProject.name }}</h1>
        <p>{{ activeProject.descShort }}</p>
        <hr />
        <span class="btn-special btn-special-project">
          <b-btn :href="activeProject.projectLink">
            <icon name="external-link-alt" />&nbsp;&nbsp;&nbsp;view the project
          </b-btn>
        </span>
        <span class="btn-special btn-special-gh">
          <b-btn :href="activeProject.githubLink">
            <icon name="brands/github" />
          </b-btn>
        </span>
      </div>
    </header>
    <div role="main">
      <div class="container">

      <b-carousel
        id="carousel1"
        controls
        indicators
        :interval="12000"
      >

          <b-carousel-slide
            v-for="slide in activeProject.slides"
            :caption="slide.caption"
            :text="slide.text"
            :img-src="slide.src"
            :key="slide._id"
          ></b-carousel-slide>

      </b-carousel>
      </div>

      <div v-html="activeProject.descLong"></div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import 'vue-awesome/icons/external-link-alt'
import 'vue-awesome/icons/brands/github'
export default {
  name: 'PortfolioItem',
  computed: {
    ...mapGetters([
      'activeProject'
    ])
  },
  methods: {}
}
</script>
