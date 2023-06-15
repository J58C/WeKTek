<template>
    <div class="card">
      <div class="card-image">
        <figure class="image is-4by3">
          <img :src="course.image" alt="Placeholder image">
        </figure>
      </div>
  
      <div class="card-content" style="background-color: #444; color: white;">
        <div class="media">
          <div class="media-content">
            <p class="is-size-5">{{ course.title }}</p>
          </div>
        </div>
  
        <div class="content">
          <p>{{ course.short_description }}</p>
  
          <router-link :to="{name: 'Course', params: {slug: course.slug}}">Selengkapnya</router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['course']
  }
  </script>
  