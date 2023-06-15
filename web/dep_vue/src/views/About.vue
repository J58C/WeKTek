<template>
  <div class="about">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Tentang Kami</h1>
      </div>
    </div>

    <section class="section">
      <p>Ini adalah halaman Tentang Kami tanpa koneksi ke backend. Pada web ini akan terlihat beberapa hal yang kurang cocok karena beberapa memerlukan backend untuk tampilannya. Untuk lebih lengkapnya, bisa dicoba untuk web dengan backend untuk mencoba fitur selengkapnya</p>
    </section>
  </div>
</template>

<script>
import '../assets/css/About.css'

export default {
  mounted() {
    document.title = 'About | StudyNet'
  }
}
</script>
