<template>
    <div>
        <nodes></nodes>
        <hr>

        <h1>Node {{id}}: {{name}}</h1>

        <h2>Relatives</h2>
        <node-relatives v-for="(relativesInOneDirection, i) in relativesInBothDirections"
                        :relatives="relativesInOneDirection"
                        :downInt="i"
        ></node-relatives>
    </div>
</template>

<script>
    import Nodes from '../components/Nodes.vue'
    import NodeRelatives from '../components/NodeRelatives.vue'

    export default {
        data() { return {
            id: this.$route.params.id,
            name: '',
            relativesInBothDirections: [],
        }},
        watch: {
            '$route'(to, from) {
                this.id = to.params.id
                this.name = to.params.name
                this.getNodeRelatives()
            }
        },
        methods: {
            getNode() {
                this.name = this.$store.state.nodes[this.id - 1]['name']
            },
            getNodeRelatives() {
                this.relativesInBothDirections = this.$store.state.nodeRelatives[this.id]
            }
        },
        created() {
            this.getNode()
            this.getNodeRelatives()
        },
        components: {
            nodes: Nodes,
            nodeRelatives: NodeRelatives
        }
    }
</script>
