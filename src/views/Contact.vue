<template>
  <div class="contact">

    <header style="text-align: center; background-color: #007bff;">
      <logo color="#ffffff" style="max-width: 200px;" class="mt-4 mb-4" alt="" />
      <h1 style="color: #ffffff;"><strong>Contact Aaron</strong></h1>
      <h2 style="color: #ffffff;" class="pb-4">Front-end Developer</h2>
    </header>

    <b-alert variant="danger"
             dismissible
             :show="showError"
             @dismissed="clearForm">
      We are sorry, but there seems to be an error getting this form sent...
    </b-alert>

    <b-alert variant="success"
             dismissible
             :show="showSuccess"
             @dismissed="clearForm">
      Your message has been sent!
    </b-alert>

    <b-form
      id="contactForm"
      method="post"
      data-netlify="true"
      data-netlify-honeypot="bot-field"
      @submit.prevent="handleSubmit">

      <input type="hidden" name="form-name" value="contact" />

      <p class="hidden">
        <label>Don’t fill this out if you're human: <input name="bot-field" /></label>
      </p>

      <b-form-group label="Your Name" label-for="formName">
        <b-form-input id="formName"
                      type="text"
                      :value="form.name"
                      @input="$event => form.name = $event"
                      required
                      placeholder="eg. Aaron Clayton (required)">
        </b-form-input>
      </b-form-group>

      <b-form-group label="Your Email" label-for="formMail">
        <b-form-input id="formMail"
                      type="email"
                      :value="form.email"
                      @input="$event => form.email = $event"
                      required
                      placeholder="eg. aaronc@protonmail.ch (required)">
        </b-form-input>
      </b-form-group>

      <b-form-group label="Your Phone#" label-for="formPhone">
        <b-form-input id="formPhone"
                      type="text"
                      :value="form.phone"
                      @input="$event => form.phone = $event"
                      placeholder="eg. 289-213-3228 (optional)">
        </b-form-input>
      </b-form-group>

      <b-form-group label="Your Message" label-for="formMessage">
        <b-form-textarea id="formMessage"
                     :value="form.message"
                     @input="$event => form.message = $event"
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
      status: '',
      form: {
        name: '',
        email: '',
        phone: '',
        message: ''
      }
    }
  },

  computed: {
    showError: function() {
      if ( this.status === 'error' ) { return true
      } else { return false }
    },
    showSuccess: function() {
      if ( this.status === 'success' ) { return true
      } else { return false }
    }
  },

  mounted() {
    this.status = 'ready'
  },

  methods: {
    log(e) {
      console.log(e)
    },
    clearForm() {
      this.form = {
        name: '',
        email: '',
        phone: '',
        message: ''
      }
      this.status = 'ready'
    },
    encode(data) {
      return Object.keys(data)
        .map(
          key => `${encodeURIComponent(key)}=${encodeURIComponent(data[key])}`
        )
        .join('&');
    },
    handleSubmit () {
      fetch('/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: this.encode({
          'form-name': 'contact',
          ...this.form
        })
      })
      .then(() => { this.status = 'success' })
      .catch(() => { this.status = 'error' })
    }
  }
}
</script>
