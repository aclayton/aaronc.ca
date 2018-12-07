<template>
    <div id="app">
      <router-view></router-view>
      <app-footer></app-footer>
      <app-outro></app-outro>
    </div>
</template>

<script>
import AppFooter from '@/components/AppFooter.vue'
import AppOutro from '@/components/AppOutro.vue'
export default {
  components: {
    AppFooter,
    AppOutro
  }
}
</script>

<style lang="scss">
@import 'styles/index.scss';
</style>
