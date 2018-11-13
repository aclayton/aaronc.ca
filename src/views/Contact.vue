<template>
  <div class="contact">
    <header style="text-align: center; background-color: #007bff;">
      <logo color="#ffffff" style="max-width: 200px;" class="mt-4 mb-4" alt="" />
      <h1 style="color: #ffffff;"><strong>Contact Aaron</strong></h1>
      <h2 style="color: #ffffff;" class="pb-4">Front-end Developer</h2>
    </header>

    <b-form
      id="contactForm"
      @submit.prevent="handleSubmit"
      v-if="show"
      method="post"
      data-netlify="true"
      data-netlify-honeypot="bot-field"
      name="contact">

      <input type="hidden" name="contact" value="ask-team-vue" />

      <b-form-group label="Your Name" label-for="formName">
        <b-form-input id="formName"
                      type="text"
                      v-model="form.name"
                      required
                      placeholder="eg. Aaron Clayton (required)">
        </b-form-input>
      </b-form-group>

      <b-form-group label="Your Email" label-for="formMail">
        <b-form-input id="formMail"
                      type="email"
                      v-model="form.email"
                      required
                      placeholder="eg. aaronc@protonmail.ch (required)">
        </b-form-input>
      </b-form-group>

      <b-form-group label="Your Phone#" label-for="formPhone">
        <b-form-input id="formPhone"
                      type="text"
                      v-model="form.phone"
                      placeholder="eg. 289-213-3228 (optional)">
        </b-form-input>
      </b-form-group>

      <b-form-group label="Your Message" label-for="formMessage">
        <b-form-textarea id="formMessage"
                     v-model="form.message"
                     placeholder="The long and short of it..."
                     :rows="3"
                     :max-rows="6">
        </b-form-textarea>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>

    </b-form>

  </div>
</template>
<script>
import Logo from '@/components/logo.vue'
export default {
  name: 'contact',
  components: {
    Logo
  },
  data() {
    return {
      show: true,
      form: {}
    }
  },

  methods: {
    handleSubmit () {
      fetch('/', {
        method: 'POST',
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: this.encode({
          'form-name': 'contact',
          ...this.form
        })
      })
      .then(() => {
        this.$router.push('thanks')
      })
      .catch(() => {
        this.$router.push('fail')
      })
    }
  }
}
</script>
