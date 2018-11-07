<template>
  <div id="availability">
    {{ availability.msg }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Availability',
  computed: {
    ...mapGetters([
      'availability'
    ])
  }
}
</script>
