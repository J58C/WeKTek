<template>
    <form v-on:submit.prevent="submitComment">
      <div class="field">
        <label class="label">Nama</label>
        <div class="control">
          <input type="text" class="input" v-model="comment.name" style="background-color: #555; color:whitesmoke">
        </div>
      </div>
  
      <div class="field">
        <label class="label">Isi</label>
        <div class="control">
          <textarea class="textarea" v-model="comment.content" style="background-color: #555; color:whitesmoke"></textarea>
        </div>
      </div>
  
      <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" :key="error">{{ error }}</p>
      </div>
  
      <div class="field">
        <div class="control">
          <button class="button is-link" style="background-color: #555; color:whitesmoke">Ajukan</button>
        </div>
      </div>
    </form>
  </template>
  
  <script>
  export default {
    props: ['course', 'activeLesson'],
    data() {
      return {
        comment: {
          name: '',
          content: '',
        },
        errors: []
      }
    },
    methods: {
      submitComment() {
        console.log('submitComment')
  
        this.errors = []
  
        if (this.comment.name === '') {
          this.errors.push('The name must be filled out')
        }
  
        if (this.comment.content === '') {
          this.errors.push('The content must be filled out')
        }
  
        if (!this.errors.length) {
          // Simulasi pemrosesan pengajuan komentar (tanpa koneksi backend)
          // Anda dapat menambahkan logika pemrosesan sesuai kebutuhan Anda di sini
          // Misalnya, menyimpan komentar ke dalam array atau melakukan operasi lainnya
  
          this.comment.name = ''
          this.comment.content = ''
  
          this.$emit('submitComment', this.comment)
        }
      },
    }
  }
  </script>
  