<template>
    <div class="login">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">Log in</h1>
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
                                  <button class="button is-dark">Log in</button>
                              </div>
                          </div>
                      </form>
  
                      <hr>
  
                      Or <router-link to="/sign-up">Klik di sini </router-link> untuk sign up!
                  </div>
              </div>
          </div>
      </section>
    </div>
  </template>
  
  <script>
  import '../assets/css/LogIn.css'
  export default {
      data() {
          return {
              username: '',
              password: '',
              errors: []
          }
      },
      mounted() {
          document.title = 'Log in | StudyNet'
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
  
              if (!this.errors.length) {
                  // Simulate a login process without backend interaction
                  // Replace this with your desired logic
                  const token = 'dummy-token'
  
                  localStorage.setItem('token', token)
  
                  this.$router.push('/dashboard/my-account')
              }
          }
      }
  }
  </script>
  