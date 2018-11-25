<template>
  <footer id="footer">
    <div class="container">

      <b-row>
        <b-col>
          <logo color="rgba(255, 255, 255, 0.3)"></logo>
        </b-col>
        <b-col class="numbers">
          <p>P: <a href="tel:289-213-3228">289-213-3228</a></p>
          <p>E: <a href="mailto:aaronc@protonmail.ch">aaronc@protonmail.ch</a></p>
        </b-col>
        <b-col>
          <div class="socials">
            <a class="fb" href="https://facebook.com/profile.php?id=100000204910548"><icon name="brands/facebook-square" /></a>
            <a class="gh" href="https://github.com/aclayton"><icon name="brands/github" /></a>
            <!-- <a class="tw" href=""><icon name="brands/twitter-square" /></a> -->
          </div>
        </b-col>
      </b-row>

    </div>
  </footer>
</template>
<script>
import Logo from '@/components/logo.vue'
import 'vue-awesome/icons/brands/facebook-square'
import 'vue-awesome/icons/brands/github'
import 'vue-awesome/icons/brands/twitter-square'
export default {
  name: 'Footer',
  components: {
    Logo
  }
}
</script>
