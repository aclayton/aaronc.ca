<template>
  <footer id="footer">
    <div class="container">

      <div class="logo">
        <logo color="rgba(255, 255, 255, 0.7)"></logo>
        <!-- <logo color="#007bff"></logo> -->
      </div>

      <div class="numbers">
        <p>P: <a href="tel:289-213-3228">289-213-3228</a></p>
        <p>E: <a href="mailto:aaronc@protonmail.ch">aaronc@protonmail.ch</a></p>
      </div>

      <div class="socials">
        <a class="fb" href="https://facebook.com/profile.php?id=100000204910548">
          <icon name="brands/facebook-square" />
        </a>
        <a class="gh" href="https://github.com/aclayton">
          <icon name="brands/github" />
        </a>
      </div>

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
