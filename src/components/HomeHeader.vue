<template>

  <header id="header-home" :style="homeHeaderStyle">
    <div class="logo">
      <logo color="#ffffff" style="max-width: 50%" alt="" />
    </div>
    <div class="main-msg">
      <h1><strong>Aaron Clayton</strong></h1>
      <h2>Front-end Developer</h2>
      <p>Producing high quality responsive websites and exceptional user experience</p>
    </div>
    <b-btn variant="link" v-scroll-to="'#recent-projects'">
      view recent work<br />
      <icon class="animated pulse infinite" name="chevron-down" />
    </b-btn>
  </header>

</template>
<script>
import 'vue-awesome/icons/chevron-down'
import Logo from '@/components/logo.vue'
export default {
  name: 'HomeHeader',

  components: {
    Logo
  },

  data() {
    return {
      homeHeaderStyle: {
        height: 0,
        overflow: 'hidden'
      }
    }
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
      this.homeHeaderStyle.height = `${window.innerHeight}px`;
    }
  }
}
</script>
