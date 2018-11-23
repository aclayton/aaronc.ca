<template>
  <b-btn
    class="btn-to-top"
    variant="link"
    size="lg"
    v-scroll-to="{
      el: '#header-home',
      easing: 'cubic-bezier(0.215, 0.61, 0.355, 1)',
      duration: 150
    }"
  >
    <icon name="chevron-up" class="animated pulse infinite" />
  </b-btn>
</template>
<script>
  import 'vue-awesome/icons/chevron-up'
  export default {
    name: 'scrollToTop'
  }
</script>
