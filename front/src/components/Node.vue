<template>
    <div>
        <h1>{{ id }}</h1>

        <node-relatives v-for="(relativesInOneDirection, i) in relativesInBothDirections"
                        :relatives="relativesInOneDirection"
                        :downInt="i"
        ></node-relatives>
    </div>
</template>

<script>
    import NodeRelatives from '../components/NodeRelatives.vue'

    import nodeRelativesData from '../data'

    export default {
        data() { return {
            id: this.$route.params.id,
            relativesInBothDirections: [],
        }},
        watch: {
            '$route'(to, from) {
                this.id = to.params.id
                this.getNodeRelatives()
            }
        },
        methods: {
            getNodeRelatives() {
                let f = () => {
                    this.relativesInBothDirections = nodeRelativesData[this.id]
                }
                setTimeout(f, 0)
            }
        },
        created() {
            this.getNodeRelatives()
        },
        components: {
            nodeRelatives: NodeRelatives
        }
    }
</script>
