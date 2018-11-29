<template>

  <div id="skills">

    <ul :style="ulStyle">
      <li v-for="skill in skills" :key="skill._id" :class="skill.name" class="skill">
        {{ skill.name }}
      </li>
    </ul>

  </div>

</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Skills',
  data() {
    return {
      ulStyle: {
        height: 0
      }
    }
  },
  computed: {
    ...mapGetters([
      'skills'
    ])
  },
  mounted() {
    this.$nextTick(() => {
      if (window.innerWidth > 600) {
        window.addEventListener('resize', this.handleResize)
      }
      this.handleResize()
    })
  },

  destroyed() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize () {
      this.ulStyle.height = `${window.innerHeight*.3}px`
    }
  }
}
</script>
