<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered" style="background-color: #222; color: white;">
        <h1 class="title">Selamat Datang!</h1>
        <h2 class="subtitle">Teknik Komputer dalam Genggamanmu</h2>
      </div>
    </div>

    <section class="section" style="background-color: #333; color: white;">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered" style="background-color: #444; color: white;">
              <span class="icon is-size-2 has-text-info"><i class="far fa-clock"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Belajar kapan saja</h2>
              <p>Waktu belajar yang fleksibel dengan jadwal</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered" style="background-color: #444; color: white;">
              <span class="icon is-size-2 has-text-info"><i class="far fa-comments"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Belajar bersama</h2>
              <p>Dengan orang-orang yang bergerak pada bidangnya</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered" style="background-color: #444; color: white;">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Belajar di mana saja</h2>
              <p>Pembelajaran berbasis web yang bisa diakses di mana saja</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <a href="/sign-up" class="button is-info is-size-3 mt-6 mb-6" style="background-color: #555; color: white;">Silakan klik di sini untuk mulai</a>
          </div>

          <hr>

          <div class="column is-3" v-for="course in courses" :key="course.id">
            <div class="box has-text-centered" style="background-color: #444; color: white;">
              <span class="icon is-size-2 has-text-info"><i class="far fa-file-alt"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">{{ course.title }}</h2>
              <p>{{ course.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      courses: [
        {
          id: 1,
          title: 'Course 1',
          description: 'Course 1 Description'
        },
        {
          id: 2,
          title: 'Course 2',
          description: 'Course 2 Description'
        },
        {
          id: 3,
          title: 'Course 3',
          description: 'Course 3 Description'
        }
      ]
    }
  }
}
</script>

<style>
/* Styles */
</style>
