<template>
  <div id="recent-projects">
    <h1 class="hide">Recent Projects</h1>
    <ul class="projects">
      <li :style="portfolioItemStyle" v-for="project in projects" :key="project._id" class="project" :class="`project-${project._id}`">
        <div class="project-details">
            <img style="max-width: 100%;" :src="project.imgMain" alt="" />
            <h2 class="hide">{{ project.name }}</h2>
            <p>{{ project.descShort}}</p>
        </div>
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
        height: 0,
        overflow: 'hidden'
      }
    }
  },
  computed: {
    ...mapGetters([
      'projects'
    ])
  },
  // mounted() {
  //   this.$nextTick(() => {
  //     window.addEventListener('resize', this.handleResize)
  //     this.handleResize()
  //   })
  // },
  // destroyed() {
  //   window.removeEventListener('resize', this.handleResize)
  // },
  // methods: {
  //   handleResize() {
  //     this.portfolioItemStyle.height = `${window.innerHeight}px`;
  //   }
  // }
}
</script>
