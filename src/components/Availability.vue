<template>
  <div id="availability">
    <b-row>
      <b-col cols="3" class="no-pad-right">
        <b-img alt="Aaron's GitHub Avatar" fluid src="https://avatars.githubusercontent.com/aclayton" />
      </b-col>
      <b-col>
        <p><small>{{ availability.msg }}</small></p>
      </b-col>
    </b-row>

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
