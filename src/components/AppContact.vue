<template>
  <div id="contact">
    <b-container>
      <p>If you’d like to find out more about how I work and my process, please fill out the form and say hi!</p>

      <b-form
        id="contactForm"
        @submit.prevent="submit"
      >

        <b-form-group label="Your Name" label-for="formName">
          <b-form-input id="formName"
                        type="text"
                        :value="contactFormData.name"
                        @input="$event => contactFormData.name = $event"
                        required
                        placeholder="eg. Aaron Clayton (required)">
          </b-form-input>
        </b-form-group>

        <b-form-group label="Your Email" label-for="formMail">
          <b-form-input id="formMail"
                        type="email"
                        :value="contactFormData.email"
                        @input="$event => contactFormData.email = $event"
                        required
                        placeholder="eg. aaronc@protonmail.ch (required)">
          </b-form-input>
        </b-form-group>

        <b-form-group label="Your Phone#" label-for="formPhone">
          <b-form-input id="formPhone"
                        type="text"
                        :value="contactFormData.phone"
                        @input="$event => contactFormData.phone = $event"
                        placeholder="eg. 289-213-3228 (optional)">
          </b-form-input>
        </b-form-group>

        <b-form-group label="Your Message" label-for="formMessage">
          <b-form-textarea id="formMessage"
                       required
                       :value="contactFormData.message"
                       @input="$event => contactFormData.message = $event"
                       placeholder="The long and short of it..."
                       :rows="6"
                       :max-rows="12">
          </b-form-textarea>
        </b-form-group>
        <div class="text-right">

          <span class="btn-special-action">

            <b-button type="submit">
              <icon name="paper-plane" />&nbsp;&nbsp;&nbsp;Submit
            </b-button>

          </span>

        </div>

      </b-form>
    </b-container>

  </div>
</template>

<script>
import 'vue-awesome/icons/paper-plane'
import { mapGetters } from 'vuex'
export default {
  name: 'ContactComponent',
  computed: {
    ...mapGetters([ 'contactFormData' ])
  },
  methods: {
    submit () {
      this.$store.dispatch('sendMessage')
    }
  }
}
</script>
