<template>
    <div class="courses">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">Kursus</h1>
        </div>
      </div>
  
      <section class="section" style="background-color: #333; color: white;">
        <div class="container">
          <div class="columns">
            <div class="column is-2">
              <aside class="menu">
                <p class="menu-label" style="color: white;">Kategori</p>
  
                <ul class="menu-list">
                  <li>
                    <a
                      v-bind:class="{'is-active': !activeCategory}"
                      @click="setActiveCategory(null)"
                      style="color: white;"
                    >
                      Semua Kursus
                    </a>
                  </li>
                  <li
                    v-for="category in categories"
                    v-bind:key="category.id"
                    @click="setActiveCategory(category)"
                  >
                    <a style="color: white;">{{ category.title }}</a>
                  </li>
                </ul>
              </aside>
            </div>
  
            <div class="column is-10">
              <div class="columns is-multiline">
                <div
                  class="column is-4"
                  v-for="course in courses"
                  v-bind:key="course.id"
                  style="color: white;"
                >
                  <div class="course-item">
                    <h3>{{ course.title }}</h3>
                    <p>{{ course.description }}</p>
                  </div>
                </div>
  
                <div class="column is-12">
                  <nav class="pagination">
                    <a class="pagination-previous">Previous</a>
                    <a class="pagination-next">Next</a>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        courses: [
          {
            id: 1,
            title: 'Course 1',
            description: 'Description of Course 1'
          },
          {
            id: 2,
            title: 'Course 2',
            description: 'Description of Course 2'
          },
          {
            id: 3,
            title: 'Course 3',
            description: 'Description of Course 3'
          }
        ],
        categories: [
          {
            id: 1,
            title: 'Category 1'
          },
          {
            id: 2,
            title: 'Category 2'
          },
          {
            id: 3,
            title: 'Category 3'
          }
        ],
        activeCategory: null
      }
    },
    methods: {
      setActiveCategory(category) {
        console.log(category)
        this.activeCategory = category
        this.getCourses()
      },
      getCourses() {
        // Simulasikan pengambilan data kursus berdasarkan kategori dari backend
        let filteredCourses = this.courses
  
        if (this.activeCategory) {
          filteredCourses = this.courses.filter(course => course.category_id === this.activeCategory.id)
        }
  
        this.courses = filteredCourses
      }
    }
  }
  </script>
  