<template>
  <div class="alerts" v-if="activeAlerts">

      <b-alert
        :variant="activeAlerts.variant"
        :show="activeAlerts.active"
        dismissible
        @dismissed="clearForm"
        class="animated slideInUp"
      >
        <div>
          <h2>{{ activeAlerts.message }}</h2>
        </div>
      </b-alert>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'AlertComponent',
  computed: {
      ...mapGetters([ 'activeAlerts' ])
  },
  mounted() {
    this.clearForm()
  },
  methods: {
    clearForm() {
      this.$store.commit('CLEAR_CONTACT_FORM')
      this.$store.commit('CLEAR_ALERTS')
    }
  }
}
</script>
<style lang="scss">
  .alerts {
    height: 100%;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1000;
    background: rgba(0,0,0,.65);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
  }
</style>
