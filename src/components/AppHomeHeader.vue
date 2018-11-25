<template>

  <header
    id="header-home"
    :style="homeHeaderStyle"
    class="container-fluid"
  >
    <div class="logo">
      <logo class="home bounceInDown" color="#ffffff" alt="" />
    </div>
    <div class="main-msg">
      <div class="main-msg-inner">
        <h1><strong>Aaron Clayton</strong></h1>
        <h2>Front-end Developer</h2>
        <p>Producing high quality responsive websites and exceptional user experience</p>
      </div>
    </div>
    <b-btn variant="link" v-scroll-to="{
        el: '#recent-projects',
        easing: 'cubic-bezier(0.215, 0.61, 0.355, 1)',
        duration: 150
      }">
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
      if (window.innerWidth > 600) {
        this.homeHeaderStyle.height = `${window.innerHeight}px`;
      } else {
        this.homeHeaderStyle.height = `${window.innerHeight}px`;
        window.removeEventListener('resize', this.handleResize)
      }
    }
  }
}
</script>
