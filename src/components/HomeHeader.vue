<template>

  <header id="header-home" :style="homeHeaderStyle">
    <div class="logo">
      <img src="/img/ac-white.svg" />
    </div>
    <div class="main-msg">
      <h1><strong>Aaron Clayton</strong></h1>
      <h2>Front-end Developer</h2>
      <p>Producing high quality responsive websites and exceptional user experience</p>
    </div>
    <b-btn variant="link">
      view recent work<br />
      <icon class="animated pulse infinite" name="chevron-down" />
    </b-btn>
  </header>

</template>
<script>
import 'vue-awesome/icons/chevron-down'
export default {
  name: 'HomeHeader',

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
