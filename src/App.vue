<template>
  <b-container fluid id="app">
    <b-row>

      <div :class="navSideClass" id="nav-side-blocker"></div>
      <div :class="navSideClass" id="nav-side">
        <navigation></navigation>
        <b-btn variant="primary" href="/doc/aaron-clayton.pdf" target="_blank">
          <icon name="file-download" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Resumé
        </b-btn>
      </div>
      <div @click="toggleNav" v-if="menuActive" id="nav-side-shade"></div>

      <b-col id="page-side">
        <div class="mobile-toggle" style="text-align: right;">
          <b-btn @click="toggleNav" variant="link">
            <icon name="ellipsis-v"/>
          </b-btn>
        </div>
        <router-view/>
      </b-col>

    </b-row>
  </b-container>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
import 'vue-awesome/icons/ellipsis-v'
import 'vue-awesome/icons/file-download'
export default {
  components: {
    Navigation
  },
  data() {
    return {
      menuActive: true
    }
  },
  computed: {
    navSideClass: function() {
      if (!this.menuActive) {
        //hide
        return ['animated', 'slideOutLeft']
      } else {
        //show
        return ['col-10', 'col-md-4', 'col-lg-4', 'animated', 'slideInLeft']
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
      if (window.innerWidth < 768) {
        this.menuActive = false
      } else {
        this.menuActive = true
      }
    },
    toggleNav() {
      if (this.menuActive == true) {
        this.menuActive = false
      } else {
        this.menuActive = true
      }
    }
  }
}
</script>

<style lang="scss">
@import 'styles/index.scss';
</style>
