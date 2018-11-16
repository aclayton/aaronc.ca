<template>
  <footer id="footer">
    <div class="container">

      <b-row>
        <b-col>
          <logo color="#ffffff"></logo>
        </b-col>
        <b-col>
          <p>Phone: <a href="tel:289-213-3228">289-213-3228</a></p>
          <p>Email: <a href="mailto:aaronc@protonmail.ch">aaronc@protonmail.ch</a></p>
        </b-col>
        <b-col>
          <a href="">Facebook</a>
          <a href="">GitHub</a>
          <a href="">Twitter</a>
        </b-col>
      </b-row>

    </div>
  </footer>
</template>
<script>
import Logo from '@/components/Logo.vue'
export default {
  name: 'Footer',
  components: {
    Logo
  }
}
</script>
