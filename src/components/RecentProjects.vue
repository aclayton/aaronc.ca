<template>
  <div id="recent-projects">
    <h1 class="hide">Recent Projects</h1>
    <ul class="projects">
      <li :style="portfolioItemStyle" v-for="project in projects" :key="project._id" class="project" :id="`project-${project._id}`">
        <div class="project-details">
          <!-- <router-link :to="{ name: 'project', params: { _id: project._id }}" class="img-wrap"> -->
            <img :src="project.imgMain" alt="" />
          <!-- </router-link> -->
          <h2 class="hide">{{ project.name }}</h2>
        </div>
        <b-btn variant="link" v-scroll-to="project.scrollToId">
          {{ project.scrollToText }}<br />
          <icon v-if="project.scrollToText != 'Top'" class="animated pulse infinite" name="chevron-down" />
        </b-btn>
      </li>
    </ul>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
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
