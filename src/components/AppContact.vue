<template>
  <div id="contact">

    <b-container>

      <p>If you’d like to find out more about how I work and my process, please fill out the form and say hi!</p>
      <!-- <p>&nbsp;</p>
      <hr />
      <p>&nbsp;</p> -->
      <b-form
        id="contactForm"
        method="post"
        data-netlify="true"
        data-netlify-honeypot="bot-field"
        @submit.prevent="handleSubmit">

        <input type="hidden" name="form-name" value="contact" />

        <p class="hide">
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
                       :rows="6"
                       :max-rows="12">
          </b-form-textarea>
        </b-form-group>
        <div class="text-right">

          <b-button type="submit" size="sm" class="btn-action">
            <icon name="paper-plane" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submit
          </b-button>

        </div>

      </b-form>
    </b-container>

    <div class="alerts">
      <b-container>

        <b-alert variant="danger"
                 dismissible
                 :show="showError"
                 @dismissed="clearError"
                 class="animated slideInUp">
          We are sorry, but there seems to be an error getting this form sent...
        </b-alert>

        <b-alert variant="success"
                 dismissible
                 :show="showSuccess"
                 @dismissed="clearForm"
                 class="animated slideInUp">
          Your message has been sent!
        </b-alert>

      </b-container>
    </div>

  </div>
</template>
<script>
import 'vue-awesome/icons/paper-plane'
export default {
  name: 'ContactComponent',

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
    clearForm() {
      this.form = {
        name: '',
        email: '',
        phone: '',
        message: ''
      }
      this.status = 'ready'
    },
    clearError() {
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
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: this.encode({
          'form-name': 'contact',
          ...this.form
        })
      })
      .then((res) => {
        if (res.ok) {
            this.status = 'success'
        } else {
            this.status = 'error'
        }
      })
    }
  }
}
</script>
