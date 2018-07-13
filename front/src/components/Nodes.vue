<template>
    <div>
        <h1>Nodes</h1>

        <ul>
            <router-link v-for="node in nodes"
                         :to="{name: 'node', params: {id: node.id, name: node.name}}"
                         tag="li"
                         active-class="active">
                <a>{{node.id}}: {{node.name}}</a>
            </router-link>
        </ul>
    </div>
</template>

<script>
    import Node from './Node.vue'

    export default {
        computed: {
            nodes() {
                return this.$store.state.nodes
            },
        },
        created() {
            this.$store.dispatch('updateNodes')
        }
    }
</script>

<style>
    .active {
        font-weight: bold;
    }
</style>

