<template>
    <div v-if="relatives.length > 0">
        <h3>{{term.direct.plural}}</h3>

        <router-link v-for="relative in relatives"
                     :to="{name: 'node', params: {id: relative.id, name: relative.name}}">
            {{relative.id}}: {{relative.name}}<br>
        </router-link>
    </div>
</template>

<script>
    export default {
        data() { return {
            down: Boolean(this.downInt)
        }},
        computed: {
            term() { return {
                direct: {
                    singular: this.down ? 'child' : 'parent',
                    plural: this.down ? 'children' : 'parents'
                },
                indirect: {
                    singular: this.down ? 'descendant' : 'ancestor',
                    plural: this.down ? 'descendants' : 'ancestors'
                }
            }}
        },
        props: ['relatives', 'downInt']
    }
</script>
