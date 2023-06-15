<template>
    <div class="video-container">
      <iframe
        :src="'https://www.youtube.com/embed/' + youtube_id"
        width="100%"
        height="400"
        frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture;"
        allowfullscreen
      ></iframe>
    </div>
  </template>
  
  <script>
  export default {
    props: ['youtube_id']
  }
  </script>
  
  <style scoped>
  .video-container {
    position: relative;
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 aspect ratio */
    overflow: hidden;
  }
  
  .video-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  </style>
  