<template>

  <header id="header-home" :style="homeHeaderStyle">
    <img src="/img/ac-white.svg" />
    <h1><strong>Aaron Clayton</strong></h1>
    <h2>Front-end Developer</h2>
    <p>Producing high quality responsive websites and exceptional user experience</p>
  </header>

</template>
<script>
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
<style scoped lang="scss">
  #header-home {
    background-color: #007bff;
    padding: 0 15px;
    color: #fff;
  }
</style>
