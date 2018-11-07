<template>
  <div id="availability">

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
