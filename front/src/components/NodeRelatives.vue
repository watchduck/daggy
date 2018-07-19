<template>
    <div v-if="relatives.length > 0">
        <h3>{{ headline }}:</h3>

        <ul>
            <router-link v-for="relative in relatives"
                         :to="{name: 'node', params: {id: relative.id, name: relative.name}}"
                         tag="li">
                <a>{{relative.id}}</a>
            </router-link>
        </ul>
    </div>
</template>

<script>
    export default {
        data() { return {
            down: Boolean(this.downInt)  // Relatives are children if true, parents otherwise.
        }},
        computed: {
            headline() {
                return this.down ? 'Children' : 'Parents'
            }
        },
        props: ['relatives', 'downInt']
    }
</script>
