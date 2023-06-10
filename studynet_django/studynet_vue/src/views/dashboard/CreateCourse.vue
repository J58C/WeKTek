<template>
    <div class="about" >
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Buat Kursus Baru</h1>
            </div>
        </div>

        <section class="section" >
            <div class="mb-6 px-6 py-4"  style="background-color: #333;">
                <h2 class="subtitle">Detail Kursus</h2>

                <div class="field">
                    <label>Judul</label>
                    <input type="text" class="input" v-model="form.title" style="background-color: #555; color:whitesmoke">
                </div>

                <div class="field">
                    <label>Deskripsi singkat</label>
                    <textarea class="textarea" v-model="form.short_description" style="background-color: #555; color:whitesmoke"></textarea>
                </div>

                <div class="field">
                    <label>Detail</label>
                    <textarea class="textarea" v-model="form.long_description" style="background-color: #555; color:whitesmoke"></textarea>
                </div>

                <div class="field" >
                    <div class="select is-multiple">
                        <select multiple size="10" v-model="form.categories" style="background-color: #555; color:whitesmoke">
                            <option 
                                v-for="category in categories"
                                v-bind:key="category.id"
                                v-bind:value="category.id"
                                style="background-color: #555; color:whitesmoke">
                                {{ category.title }}
                            </option>
                        </select>
                    </div>
                </div>
            </div>

            <div class="mb-6 px-6 py-4" style="background-color: #333;" >
                <h2 class="subtitle">Pembelajaran</h2>

                <div
                    v-for="(lesson, index) in form.lessons"
                    v-bind:key="index"
                    class="mb-4"
                >
                    <h3 class="subtitle is-size-6">Pembelajaran</h3>

                    <div class="field">
                        <label>Judul</label>
                        <input 
                            type="text" 
                            class="input" 
                            v-model="lesson.title"
                            :name="`form.lessons[${index}][title]`"
                        >
                    </div>

                    <div class="field">
                        <label>Deskripsi singkat</label>
                        <textarea class="textarea" v-model="lesson.short_description" :name="`form.lessons[${index}][short_description]`"></textarea>
                    </div>

                    <div class="field">
                        <label>Detail</label>
                        <textarea class="textarea" v-model="lesson.long_description" :name="`form.lessons[${index}][long_description]`"></textarea>
                    </div>

                    <hr>
                </div>

                <button class="button is-primary" @click="addLesson()" style="background-color: #555; color:whitesmoke">Tambahkan pembelajaran</button>
            </div>

            <div class="field buttons">
                <button class="button is-success" @click="submitForm('draft')" style="background-color: #555; color:whitesmoke">Simpan sebagai draf</button>
                <button class="button is-info" @click="submitForm('review')" style="background-color: #555; color:whitesmoke">Ajukan</button>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios'
import '../../assets/css/dashboard/CreateCourse.css'

export default {
    data() {
        return {
            form: {
                title: '',
                short_description: '',
                long_description: '',
                categories: [],
                status: '',
                lessons: []
            },
            categories: [],
        }
    },
    mounted() {
        this.getCategories()
    },
    methods: {
        getCategories() {
            console.log('getCategories')

            axios
                .get('courses/get_categories/')
                .then(response => {
                    console.log(response.data)

                    this.categories = response.data
                })
        },
        submitForm(status) {
            console.log('submitForm')
            console.log(this.form)

            this.form.status = status

            axios
                .post('courses/create/', this.form)
                .then(response => {
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error:', error)
                })
        },
        addLesson() {
            console.log('addLesson')

            this.form.lessons.push({
                title: '',
                short_description: '',
                long_description: ''
            })
        }
    }
}
</script>