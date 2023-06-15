<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Akunku</h1>
      </div>
    </div>

    <section class="section">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="subtitle is-size-3">Kursus yang aktif</h2>
        </div>

        <div 
          class="column is-4"
          v-for="course in courses"
          v-bind:key="course.id"
        >
          <CourseItem :course="course" />
        </div>
      </div>

      <hr>

      <button @click="logout()" class="button is-danger">Log Out</button>
    </section>
  </div>
</template>

<script>
  import CourseItem from './CourseItem.vue';
  export default {
    data() {
      return {
        courses: []
      }
    },
    components: {
      CourseItem
    },
    props: {
      course: {
        type: Object,
        required: true
      }
    },
    mounted() {
      // Tidak ada pemanggilan API
    },
    methods: {
      async logout() {
        console.log('logout');

        // Tidak ada pemanggilan API

        // Kosongkan courses
        this.courses = [];

        // Tidak ada pengaturan token atau pemindahan halaman
      }
    }
  }

</script>