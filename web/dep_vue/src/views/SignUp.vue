<template>
    <div class="signup">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">Sign up</h1>
        </div>
      </div>
  
      <section class="section">
          <div class="container">
              <div class="columns">
                  <div class="column is-4 is-offset-4">
                      <form v-on:submit.prevent="submitForm">
                          <div class="field">
                              <label>E-mail</label>
                              <div class="control">
                                  <input type="email" class="input" v-model="username">
                              </div>
                          </div>
  
                          <div class="field">
                              <label>Password</label>
                              <div class="control">
                                  <input type="password" class="input" v-model="password">
                              </div>
                          </div>
  
                          <div class="field">
                              <label>Ulangi password</label>
                              <div class="control">
                                  <input type="password" class="input" v-model="password2">
                              </div>
                          </div>
  
                          <div class="notification is-danger" v-if="errors.length">
                              <p
                                  v-for="error in errors"
                                  v-bind:key="error"
                              >
                                  {{ error }}
                              </p>
                          </div>
  
                          <div class="field">
                              <div class="control">
                                  <button class="button is-dark">Sign up</button>
                              </div>
                          </div>
                      </form>
  
                      <hr>
  
                      Or <router-link to="/log-in">Klik di sini </router-link> untuk log in!
                  </div>
              </div>
          </div>
      </section>
    </div>
  </template>
  
  <script>
  import '../assets/css/SignUp.css'
  export default {
      data() {
          return {
              username: '',
              password: '',
              password2: '',
              errors: []
          }
      },
      mounted() {
          document.title = 'Sign up | StudyNet'
      },
      methods: {
          submitForm() {
              console.log('submitForm')
  
              this.errors = []
  
              if (this.username === '') {
                  this.errors.push('The username is missing!')
              }
  
              if (this.password === '') {
                  this.errors.push('The password is missing!')
              }
  
              if (this.password !== this.password2) {
                  this.errors.push('The passwords are not matching!')
              }
  
              if (!this.errors.length) {
                  // Simulate a sign-up process without backend interaction
                  // Replace this with your desired logic
                  this.$router.push('/log-in')
              }
          }
      }
  }
  </script>