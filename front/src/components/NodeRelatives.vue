<template>
    <div v-if="relatives.length > 0">
        <h3>{{term.direct.plural}}</h3>

        <table>
            <tr v-for="r in relatives">
                <router-link :to="{name: 'node', params: {id: r.id, name: r.name}}"
                             tag="td"
                             @click.native="rememberDebug(r.id)">
                    <a>{{r.id}}</a>
                </router-link>
                <td>
                    {{r.name}}
                </td>
            </tr>
        </table>
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
            rememberDebug(id) {
                console.log(this.$props.parentNodeDebug + ' click ' + id)
            }
        },
        props: ['relatives', 'downInt', 'parentNodeDebug']
    }
</script>

<style>
    td {
        border: 1px solid black;
        background-color: burlywood;
        padding: 2px 5px;
    }
    table {
        border-collapse: collapse;
    }
</style>
