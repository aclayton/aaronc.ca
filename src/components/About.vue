<template>
  <div id="about">
    <div class="container">

      <b-row>
        <b-col cols="12" class="col-sm-3">
          <b-img class="test" alt="Aaron's GitHub Avatar" fluid src="https://avatars.githubusercontent.com/aclayton" />
        </b-col>
        <b-col>
          <p>A self-motivated web development professional with in depth knowledge and proficiency in <strong>Vuejs/Vuex</strong>, <strong>Node</strong>, <strong>MongoDB</strong>. My varied work experience has provided me with the liberty to design and develop cutting edge websites that deliver on impact, functionality and accessibility.</p>


          <div class="text-right">
            <b-btn class="btn-github mr-2" variant="dark" size="sm" href="https://github.com/aclayton" target="_blank">
              <icon name="brands/github" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GitHub
            </b-btn>

            <b-btn variant="primary" size="sm" href="/doc/aaron-clayton.pdf" target="_blank">
              <icon name="file-download" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Resumé
            </b-btn>
          </div>

        </b-col>
      </b-row>

    </div>
  </div>

</template>
<script>
import 'vue-awesome/icons/file-download'
import 'vue-awesome/icons/brands/github'
export default {
  name: 'About'
}
</script>
