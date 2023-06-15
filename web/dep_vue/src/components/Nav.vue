<template>
    <nav class="navbar is-info" role="navigation" aria-label="main naviation" style="min-height: 5rem; background-color: black; color: white;">
      <div class="navbar-brand">
        <router-link class="navbar-item is-size-4" to="/" style="background-color: black; color: white;">WeKTeK</router-link>
      </div>
  
      <div id="navbar-item" class="navbar-menu">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item" style="background-color: black; color: white;">Home</router-link>
          <router-link to="/about" class="navbar-item" style="background-color: black; color: white;">Tentang Kami</router-link>
          <router-link to="/courses" class="navbar-item" style="background-color: black; color: white;">Kursus</router-link>
          <router-link to="/editor" class="navbar-item" style="background-color: black; color: white;">IDE</router-link>
        </div>
  
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/sign-up" class="button is-primary" style="background-color: #333; color: white;"><strong>Sign up</strong></router-link>
              <router-link to="/log-in" class="button is-light" style="background-color: #333; color: white;">Log in</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </template>
  