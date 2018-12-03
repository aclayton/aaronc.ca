<template>

  <div id="skills">

    <div id='particles-js' ref="skillsParticles"></div>

  </div>

</template>

<script>
import { mapGetters } from 'vuex'
import particlesSettings from './../assets/particles'
export default {
  name: 'Skills',
  computed: {
    ...mapGetters([
      'skills'
    ])
  },
  created() {
    require('./../assets/p')
  },
  mounted() {
    this.initParticlesJS()
  },

  methods: {
    initParticlesJS () {
      // eslint-disable-next-line
      particlesJS('particles-js', particlesSettings)
    }
  }
}
</script>
