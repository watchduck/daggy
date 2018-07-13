<template>
    <div v-if="relatives.length > 0">
        <h3>{{term.direct.plural}}</h3>

        <ul>
            <tr v-for="relative in relatives">
                <router-link :to="{name: 'node', params: {id: relative.id, name: relative.name}}"
                             tag="li"
                             @click.native="clickDebug(relative.id)">
                    <a>{{relative.id}}: {{relative.name}}</a>
                </router-link>
            </tr>
        </ul>
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
        methods: {
            clickDebug(clicked_id) {
                console.log(this.$props.currentNodeDebug + ' click ' + clicked_id)
            }
        },
        props: ['relatives', 'downInt', 'currentNodeDebug']
    }
</script>
