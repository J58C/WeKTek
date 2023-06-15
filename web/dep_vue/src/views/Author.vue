<template>
    <div class="courses">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">{{ created_by.first_name + ' ' + created_by.last_name }}</h1>
        </div>
      </div>
  
      <section class="section">
        <div class="container">
          <div class="columns is-multiline">
            <div class="column is-4" v-for="course in courses" v-bind:key="course.id">
              <div class="course-item">
                <h2>{{ course.title }}</h2>
                <p>{{ course.description }}</p>
                <!-- Tambahkan elemen lain yang diperlukan -->
              </div>
            </div>
  
            <div class="column is-12">
              <nav class="pagination">
                <a class="pagination-previous">Sebelumnya</a>
                <a class="pagination-next">Selanjutnya</a>
              </nav>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import '../assets/css/Author.css'
  
  export default {
    data() {
      return {
        courses: [],
        created_by: {
          first_name: 'John',
          last_name: 'Doe'
        }
      }
    },
    mounted() {
      console.log('mounted')
  
      // Panggil method getCourses() di sini
    },
    methods: {
      getCourses() {
        // Simulasikan pengambilan data courses
        this.courses = [
          {
            id: 1,
            title: 'Course 1',
            description: 'Deskripsi Course 1'
          },
          {
            id: 2,
            title: 'Course 2',
            description: 'Deskripsi Course 2'
          },
          {
            id: 3,
            title: 'Course 3',
            description: 'Deskripsi Course 3'
          }
        ]
      }
    }
  }
  </script>
  