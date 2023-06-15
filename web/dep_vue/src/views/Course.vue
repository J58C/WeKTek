<template>
    <div class="courses">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">{{ course.title }}</h1>
  
          <router-link :to="{ name: 'Author', params: { id: course.created_by.id } }" class="subtitle">
            By {{ course.created_by.first_name + ' ' + course.created_by.last_name }}
          </router-link>
        </div>
      </div>
  
      <section class="section">
        <div class="container">
          <div class="columns content">
            <div class="column is-2">
              <h2 style="color: white;">Isi</h2>
  
              <ul>
                <li v-for="lesson in lessons" v-bind:key="lesson.id">
                  <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
                </li>
              </ul>
            </div>
  
            <div class="column is-10">
              <template v-if="isAuthenticated">
                <template v-if="activeLesson">
                  <h2>{{ activeLesson.title }}</h2>
  
                  <span class="tag is-warning" v-if="activity.status === 'started'" @click="markAsDone" style="background-color: #555; color: whitesmoke">Started (mark as done)</span>
                  <span class="tag is-success" v-else style="background-color: #666; color: whitesmoke">Done</span>
  
                  <hr>
  
                  {{ activeLesson.long_description }}
  
                  <hr>
  
                  <template v-if="activeLesson.lesson_type === 'quiz'">
                    <Quiz v-bind:quiz="quiz" />
                  </template>
  
                  <template v-if="activeLesson.lesson_type === 'video'">
                    <Video v-bind:youtube_id="activeLesson.youtube_id" />
                  </template>
  
                  <template v-if="activeLesson.lesson_type === 'article'">
                    <div v-for="comment in comments" v-bind:key="comment.id">
                      <p>{{ comment.text }}</p>
                    </div>
  
                    <div>
                      <input type="text" v-model="newComment" placeholder="Add a comment" />
                      <button @click="submitComment">Submit</button>
                    </div>
                  </template>
                </template>
  
                <template v-else>
                  {{ course.long_description }}
                </template>
              </template>
  
              <template v-else>
                <h2>Akses terbatas</h2>
  
                <p>Mohon Log In dulu untuk lanjut</p>
              </template>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import CourseComment from '@/components/CourseComment'
  import Quiz from '@/components/Quiz'
  import Video from '@/components/Video'
  
  export default {
    components: {
      CourseComment,
      Quiz,
      Video
    },
    data() {
      return {
        course: {
          created_by: {
            id: 0
          }
        },
        lessons: [],
        comments: [],
        activeLesson: null,
        isAuthenticated: true, // Ubah menjadi false jika ingin mensimulasikan akses terbatas
        newComment: '',
        quiz: {},
        activity: {}
      }
    },
    mounted() {
      console.log('mounted')
  
      // Panggil method getCourses() di sini
      this.getCourses()
    },
    methods: {
      getCourses() {
        // Simulasikan pengambilan data course dan lessons
        this.course = {
          title: 'Course Title',
          created_by: {
            id: 1,
            first_name: 'John',
            last_name: 'Doe'
          },
          long_description: 'Long description of the course'
        }
  
        this.lessons = [
          {
            id: 1,
            title: 'Lesson 1',
            lesson_type: 'video',
            youtube_id: 'abc123',
            long_description: 'Long description of Lesson 1'
          },
          {
            id: 2,
            title: 'Lesson 2',
            lesson_type: 'article',
            long_description: 'Long description of Lesson 2'
          },
          {
            id: 3,
            title: 'Lesson 3',
            lesson_type: 'quiz',
            long_description: 'Long description of Lesson 3'
          }
        ]
      },
      setActiveLesson(lesson) {
        this.activeLesson = lesson
  
        if (lesson.lesson_type === 'quiz') {
          this.getQuiz()
        } else {
          this.getComments()
        }
  
        this.trackStarted()
      },
      trackStarted() {
        // Simulasikan pengiriman data ke backend untuk melacak aktivitas dimulai
        this.activity = {
          status: 'started'
        }
      },
      markAsDone() {
        // Simulasikan pengiriman data ke backend untuk menandai aktivitas selesai
        this.activity = {
          status: 'done'
        }
      },
      getQuiz() {
        // Simulasikan pengambilan data quiz dari backend
        this.quiz = {
          // Data quiz
        }
      },
      getComments() {
        // Simulasikan pengambilan data komentar dari backend
        this.comments = [
          {
            id: 1,
            text: 'Comment 1'
          },
          {
            id: 2,
            text: 'Comment 2'
          }
        ]
      },
      submitComment() {
        // Simulasikan pengiriman data komentar ke backend
        const comment = {
          id: this.comments.length + 1,
          text: this.newComment
        }
        this.comments.push(comment)
        this.newComment = ''
      }
    }
  }
  </script>
  