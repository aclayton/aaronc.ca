<template>
  <div id="recent-projects">
    <h1 class="hide">Recent Projects</h1>
    <ul class="projects">
      <li :style="portfolioItemStyle" v-for="project in projects" :key="project._id" class="project" :id="`project-${project._id}`">
        <div class="project-details">
          <!-- <router-link :to="{ name: 'project', params: { _id: project._id }}" class="img-wrap"> -->
          <h2 class="hide">{{ project.name }}</h2>
          <img v-if="project.imgMain" :src="project.imgMain" alt="" />
          <div v-if="project.descLong">
            <p>{{ project.descLong }}</p>
          </div>
          <div v-if="project.projectLink || project.githubLink" class="button-row mt-4">
            <b-btn class="mr-4" v-if="project.projectLink" :href="project.projectLink" target="_blank" variant="outline-secondary" size="sm">
              <icon name="external-link-alt" /> View the Project
            </b-btn>
            <b-btn  class="btn-gh" v-if="project.githubLink" :href="project.githubLink" target="_blank" variant="outline-secondary" size="sm">
              <icon name="brands/github" /> View the Code
            </b-btn>
          </div>
          <!-- </router-link> -->
        </div>
        <b-btn variant="link" class="btn-scroll" v-scroll-to="project.scrollToId">
          {{ project.scrollToText }}<br />
          <icon v-if="project.scrollToText != 'Top'" class="animated pulse infinite" name="chevron-down" />
        </b-btn>
      </li>
    </ul>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import 'vue-awesome/icons/brands/github'
import 'vue-awesome/icons/external-link-alt'
export default {
  name: 'RecentProjects',
  data() {
    return {
      portfolioItemStyle: {
        height: '100%',
        overflow: 'hidden'
      }
    }
  },
  computed: {
    ...mapGetters([
      'projects'
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
      this.portfolioItemStyle.height = `${window.innerHeight}px`;
    }
  }
}
</script>
