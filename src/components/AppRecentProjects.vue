<template>
  <div
    id="recent-projects"
    class="container-fluid no-pad"
  >
    <h1 class="hide">Recent Projects</h1>
    <ul class="projects row">
      <li  v-for="project in projects" :class="project.cardClass" :style="portfolioItemStyle" :key="project._id" class="project col-md" :id="`project-${project._id}`">
        <div class="project-details" @click="handleHover(project)">


          <div class="front" :style="portfolioItemStyle">
            <h2 class="hide">{{ project.name }}</h2>
            <img v-if="project.imgMain" :src="project.imgMain" alt="" />
          </div>

          <div class="back" :style="portfolioItemStyle">
            <div v-if="project.descShort">
              <p>{{ project.descShort }}</p>
            </div>
            <div v-if="project.projectLink || project.githubLink" class="button-row mt-4">
              <b-btn class="mr-4" v-if="project.projectLink" @click="handleNavigation(project._id)" target="_blank" variant="outline-secondary" size="sm">

                  <icon name="link" />&nbsp;&nbsp;&nbsp;View the Project

              </b-btn>
              <!-- <b-btn  class="btn-gh" v-if="project.githubLink" :href="project.githubLink" target="_blank" variant="outline-secondary" size="sm">
                <icon name="brands/github" /> View the Code
              </b-btn> -->
            </div>
          </div>


        </div>
        <b-btn variant="link" class="btn-scroll" v-if="project.scrollToId" v-scroll-to="project.scrollToId">
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
import 'vue-awesome/icons/link'

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
      this.calcSize()
    })
  },

  destroyed() {
    window.removeEventListener('resize', this.handleResize)
  },

  methods: {
    handleNavigation(id) {
      this.$router.push({
        name: 'PortfolioItem',
        params: { _id: id }
      })
    },

    handleHover(project) {
      if (project.cardClass === 'hover') {
        project.cardClass = ''
      } else {
        project.cardClass = 'hover'
      }
    },

    calcSize() {
      if (window.innerWidth < 768) {
          this.portfolioItemStyle.height = `${window.innerHeight / 2}px`
          window.removeEventListener('resize', this.handleResize)
      } else {
          this.portfolioItemStyle.height = `${window.innerWidth / 2.333}px`
          this.portfolioItemStyle.height = `${window.innerWidth / 3.333}px`
      }
    },

    handleResize() {
      this.calcSize()
    }
  }
}
</script>
