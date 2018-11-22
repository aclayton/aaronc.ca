<template>

  <div id="skills">
    <div class="container">

      <b-row>
        <b-col>
          <h2><strong>Skills</strong></h2>

          <label>Markup</label>
            <div class="skill">HTML 5</div>
            <div class="skill">WCAG / Section 508</div>
            <div class="skill">Clean Semantics</div>
            <div class="skill">SEO</div>
          <label>Javascript</label>
            <div class="skill">Vue/Vuex</div>
            <div class="skill">AngularJS</div>
            <div class="skill">Node</div>
            <div class="skill">Webpack</div>
            <div class="skill">ES6</div>
            <div class="skill">Babel</div>
          <label>Styling</label>
            <div class="skill">Custom</div>
            <div class="skill">Bootstrap (3/4)</div>
            <div class="skill">Material Design</div>
            <div class="skill">SCSS</div>
            <div class="skill">OOCSS</div>
          <label>Other</label>
            <div class="skill">MongoDB</div>
            <div class="skill">PWA</div>
            <div class="skill">Service Workers</div>
            <div class="skill">Apache Cordova</div>
            <div class="skill">Git</div>
            <div class="skill">OAuth</div>

        </b-col>
      </b-row>

    </div>
  </div>

</template>

<script>
import 'vue-awesome/icons/brands/html5'
import 'vue-awesome/icons/brands/vuejs'
import 'vue-awesome/icons/brands/angular'
import 'vue-awesome/icons/brands/node-js'
import 'vue-awesome/icons/brands/sass'
import 'vue-awesome/icons/mobile-alt'
import 'vue-awesome/icons/brands/github'

export default {
  name: 'Skills',
  methods: {
    
  }
}
</script>
