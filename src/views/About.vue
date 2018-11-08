<template>
  <div class="about">
    <header style="text-align: center; background-color: #007bff;">
      <img src="/img/ac-white.svg" style="max-width: 200px;" class="mt-4 mb-4" alt="" />
      <h1 style="color: #fff;"><strong>About Aaron</strong></h1>
      <h2 style="color: #fff;" class="pb-4">Front-end Developer</h2>
    </header>
    <div role="main">

      <b-row>
        <b-col cols="4" class="col-sm-3">
          <img style="max-width: 100%;" src="https://avatars.githubusercontent.com/aclayton" />
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
            <b-progress-bar :value="25" variant="success"><strong>HTML 5</strong></b-progress-bar>
            <b-progress-bar :value="25" variant="warning"><strong>WCAG / Section 508</strong></b-progress-bar>
            <b-progress-bar :value="25" variant="primary"><strong>Clean Semantics</strong></b-progress-bar>
            <b-progress-bar :value="25" variant="secondary"><strong>SEO</strong></b-progress-bar>
          </b-progress>
          <label>Javascript</label>
          <b-progress height="1.6rem" class="mb-3">
            <b-progress-bar :value="16.66" variant="info"><strong>Vue/Vuex</strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="danger"><strong>AngularJS</strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="dark"><strong>Node</strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="success"><strong>Webpack</strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="secondary"><strong>ES6</strong></b-progress-bar>
            <b-progress-bar :value="16.66" variant="primary"><strong>Babel</strong></b-progress-bar>
          </b-progress>
          <label>Styling</label>
          <b-progress height="1.6rem" class="mb-3">
            <b-progress-bar :value="20" variant="info"><strong>Custom</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="danger"><strong>Bootstrap (3/4)</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="dark"><strong>Material Design</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="success"><strong>SCSS</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="secondary"><strong>OOCSS</strong></b-progress-bar>
          </b-progress>
          <label>Other</label>
          <b-progress height="1.6rem" class="mb-3">
            <b-progress-bar :value="20" variant="info"><strong>MongoDB</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="danger"><strong>PWA</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="dark"><strong>Service Workers</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="success"><strong>Apache Cordova</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="secondary"><strong>Git</strong></b-progress-bar>
            <b-progress-bar :value="20" variant="secondary"><strong>OAuth</strong></b-progress-bar>
          </b-progress>

        </b-col>
      </b-row>
      <hr />
      <b-row>
        <b-col>
          <h2><strong>More...</strong></h2>
          <p>
            Phat ipsum dolor sit i'm in the shizzle, consectetuer adipiscing shut the shizzle up. Stuff shizzlin dizzle velizzle, things yippiyo, suscipit shiznit, crazy vizzle, for sure. Shizzle my nizzle crocodizzle own yo' tortizzle. Sizzle daahng dawg. Its fo rizzle izzle dolor dapibus sizzle tempizzle tempor. Maurizzle pellentesque nibh sizzle boom shackalack. I'm in the shizzle izzle tortor. Pellentesque check it out rhoncizzle nisi. In habitasse platea that's the shizzle. Get down get down dapibizzle. Fo tellus da bomb, pretizzle eu, mattizzle ac, eleifend vitae, nunc. Gangsta suscipizzle. Fizzle sempizzle shit sizzle we gonna chung.
          </p>
          <p>
            Phasellizzle its fo rizzle volutpat ma nizzle. Ut boom shackalack adipiscing the bizzle. Donizzle sizzle break yo neck, yall. Uhuh ... yih! sapizzle massa, ultrices nizzle, go to hizzle yo mamma, fermentum quis, pede. Ghetto da bomb hizzle. Etiam break yo neck, yall ornare ante. Mauris pimpin'. Vestibulizzle dope pede its fo rizzle nibh commodo commodo. Mammasay mammasa mamma oo sa ipsizzle dolor sizzle fo shizzle, consectetizzle nizzle brizzle. Sed izzle mi. Dope mi sizzle, check it out izzle, mammasay mammasa mamma oo sa a, eleifend gangster, shut the shizzle up.
          </p>
        </b-col>
      </b-row>

      <footer>

      </footer>

    </div>
  </div>
</template>
<script>

</script>
