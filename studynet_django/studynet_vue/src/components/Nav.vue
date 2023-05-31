<template>
    <nav class="navbar is-info" role="navigation" aria-label="main naviation" style="min-height: 5rem; background-color: black; color: white;">
        <div class="navbar-brand">
            <router-link class="navbar-item is-size-4" to="/" style="background-color: black; color: white;">[Nama webnya]</router-link>
        </div>

        <div id="navbar-item" class="navbar-menu">
            <div class="navbar-start">
                <router-link to="/" class="navbar-item" style="background-color: black; color: white;">Home</router-link>
                <router-link to="/about" class="navbar-item" style="background-color: black; color: white;">About</router-link>
                <router-link to="/courses" class="navbar-item" style="background-color: black; color: white;">Courses</router-link>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="$store.state.user.isAuthenticated">
                            <router-link to="/dashboard/create-course" class="button is-primary" style="background-color: #555; color: white;">Create course</router-link>
                            <router-link to="/dashboard/my-account" class="button is-info" style="background-color: #555; color: white;">My account</router-link>
                        </template>

                        <template v-else>
                            <router-link to="/sign-up" class="button is-primary" style="background-color: #333; color: white;"><strong>Sign up</strong></router-link>
                            <router-link to="/log-in" class="button is-light" style="background-color: #333; color: white;">Log in</router-link>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>