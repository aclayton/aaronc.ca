<template>
  <div id="about" :style="aboutStyle">
    <div class="container">
      <div class="about-header">
        <div class="about-header-inner">
          <b-img class="test" alt="Aaron's GitHub Avatar" fluid src="https://avatars.githubusercontent.com/aclayton" />
          <h2>Aaron is ...</h2>
        </div>
      </div>

        <div class="details">
          <p>A self-motivated web development professional with in depth knowledge and proficiency in <strong>Vuejs/Vuex</strong>, <strong>Node</strong>, <strong>MongoDB</strong>. My varied work experience has provided me with the liberty to design and develop cutting edge websites that deliver on impact, functionality and accessibility.</p>


          <div class="text-right">
            <b-btn class="btn-github mr-2" variant="dark" size="sm" href="https://github.com/aclayton" target="_blank">
              <icon name="brands/github" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GitHub
            </b-btn>

            <b-btn class="btn-action" size="sm" href="/doc/aaron-clayton.pdf" target="_blank">
              <icon name="file-download" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Resumé
            </b-btn>
          </div>
        </div>

    </div>
  </div>

</template>
<script>
import 'vue-awesome/icons/file-download'
import 'vue-awesome/icons/brands/github'
export default {
  name: 'About',
  data() {
    return {
      aboutStyle: {
        height: 0
      }
    }
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
      let height = document.getElementById('particles-js').clientHeight;
      this.aboutStyle.height = `${height}px`
    },
  }
}
</script>
