<template>
  <div class="about">
    <header style="text-align: center; background-color: #007bff;">
      <logo color="#ffffff" style="max-width: 200px;" class="mt-4 mb-4" alt="" />
      <h1 style="color: #ffffff;"><strong>About Aaron</strong></h1>
      <h2 style="color: #ffffff;" class="pb-4">Front-end Developer</h2>
    </header>
    <div role="main">

      <b-row>
        <b-col cols="4" class="col-sm-3">
          <b-img alt="Aaron's GitHub Avatar" thumbnail fluid src="https://avatars.githubusercontent.com/aclayton" />
        </b-col>
        <b-col>
          <p>A self-motivated web development professional with in depth knowledge and proficiency in <strong>Vuejs/Vuex</strong>, <strong>Node</strong>, <strong>MongoDB</strong>. My varied work experience has provided me with the liberty to design and develop cutting edge websites that deliver on impact, functionality and accessibility.</p>
          <div class="text-right">
            <b-btn variant="primary" href="/doc/aaron-clayton.pdf" target="_blank">
              <icon name="file-download" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Resumé
            </b-btn>
          </div>
        </b-col>
      </b-row>

      <hr />

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
      <hr />
      <b-row>
        <b-col>
          <h2><strong>Learn More...</strong></h2>
          <p>
            If you’d like to find out more about how I work and my process of working with clients, please visit the contact page and give a little information about the project you have in mind.
          </p>
          <div style="text-align: right; margin-bottom: 60px;">
            <b-btn to="contact" variant="primary">
              <icon name="mobile-alt" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contact
            </b-btn>
          </div>
        </b-col>
      </b-row>

      <footer>

      </footer>

    </div>
  </div>
</template>
<script>
import Logo from '@/components/logo.vue'
import 'vue-awesome/icons/brands/html5'
import 'vue-awesome/icons/brands/vuejs'
import 'vue-awesome/icons/brands/angular'
import 'vue-awesome/icons/brands/node-js'
import 'vue-awesome/icons/brands/sass'
import 'vue-awesome/icons/mobile-alt'
export default {
  name: 'about',
  components: {
    Logo
  }
}
</script>
