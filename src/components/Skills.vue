<template>

  <div id="skills">
    <div class="container">

      <b-row>
        <b-col>
          <h2><strong>Skills</strong></h2>

          <label>Markup</label>
          <b-progress height="1.6rem" class="mb-3">
            <b-progress-bar :value="20" variant="success"><strong>
              <icon name="brands/html5" /> HTML 5
            </strong></b-progress-bar>
            <b-progress-bar :value="35" variant="warning"><strong>WCAG / Section 508</strong></b-progress-bar>
            <b-progress-bar :value="30" variant="primary"><strong>Clean Semantics</strong></b-progress-bar>
            <b-progress-bar :value="15" variant="secondary"><strong>SEO</strong></b-progress-bar>
          </b-progress>
          <label>Javascript</label>
          <b-progress height="1.6rem" class="mb-3">
            <b-progress-bar :value="16.66" variant="info"><strong>
              <icon name="brands/vuejs" /> Vue/Vuex
            </strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="danger"><strong>
              <icon name="brands/angular" /> AngularJS
            </strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="dark"><strong>
              <icon name="brands/node-js" /> Node
            </strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="secondary"><strong>Webpack</strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="success"><strong>ES6</strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="warning"><strong>Babel</strong></b-progress-bar>
          </b-progress>
          <label>Styling</label>
          <b-progress height="1.6rem" class="mb-3">
            <b-progress-bar :value="20" variant="dark"><strong>Custom</strong></b-progress-bar>
            <b-progress-bar :value="25" variant="primary"><strong>Bootstrap (3/4)</strong></b-progress-bar>
            <b-progress-bar :value="25" variant="danger"><strong>Material Design</strong></b-progress-bar>
            <b-progress-bar :value="15" variant="warning"><strong>
              <icon name="brands/sass" /> SCSS
            </strong></b-progress-bar>
            <b-progress-bar :value="15" variant="info"><strong>OOCSS</strong></b-progress-bar>
          </b-progress>
          <label>Other</label>
          <b-progress height="1.6rem" class="mb-3">
            <b-progress-bar :value="20" variant="success"><strong>MongoDB</strong></b-progress-bar>
            <b-progress-bar :value="13" variant="dark"><strong>PWA</strong></b-progress-bar>
            <b-progress-bar :value="32" variant="danger"><strong>Service Workers</strong></b-progress-bar>
            <b-progress-bar :value="29" variant="primary"><strong>Apache Cordova</strong></b-progress-bar>
            <b-progress-bar :value="9" variant="info"><strong>Git</strong></b-progress-bar>
            <b-progress-bar :value="17" variant="secondary"><strong>OAuth</strong></b-progress-bar>
          </b-progress>

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
  name: 'Skills'
}
</script>
