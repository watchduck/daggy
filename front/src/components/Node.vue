<template>
    <div>
        <nodes></nodes>
        <hr>

        <h1>Node {{id}}: {{name}}</h1>

        <input v-model="newName">
        <button @click="putNodeName">change name</button>

        <br><br>
        <button @click="deleteNode">delete</button>

        <h2>Relatives</h2>
        <node-relatives v-for="(relativesInOneDirection, i) in relativesInBothDirections"
                        :relatives="relativesInOneDirection"
                        :downInt="i"
                        :currentNodeDebug="id"
        ></node-relatives>
    </div>
</template>

<script>
    import Nodes from '../components/Nodes.vue'
    import NodeRelatives from '../components/NodeRelatives.vue'

    import axios from 'axios'

    import { mapActions } from 'vuex'

    export default {
        data() { return {
            id: this.$route.params.id,
            name: '',
            newName: '',
            relativesInBothDirections: [],
            backUrlBase: this.$store.state.backUrlBase,
            backUrlNodes: this.$store.getters.backUrlNodes,
            auth: this.$store.state.auth
        }},
        computed: {
            nodesUrl() {
                return this.backUrlNodes + this.id + '/'
            },
            detailUrl() {
                return this.backUrlBase + 'node-details/' + this.id + '/'
            },
            deleteUrl() {
                return this.backUrlBase + 'node-delete/' + this.id + '/'
            }
        },
        watch: {
            '$route'(to, from) {
                console.log(from.params.id + ' ----> ' + to.params.id)
                this.id = to.params.id
                this.name = to.params.name
                this.newName = to.params.name
                this.getNodeRelatives()
            }
        },
        methods: {
            ...mapActions(['updateNodes']),
            getNode() {
                axios.get(this.nodesUrl, {auth: this.auth})
                    .then(response => {
                        this.name = response.data.name
                        this.newName = response.data.name
                    })
                    .catch(e => {
                        console.log(e)
                    })
            },
            getNodeRelatives() {
                axios.get(this.detailUrl, {auth: this.auth})
                    .then(response => {
                        this.relativesInBothDirections = response.data
                    })
                    .catch(e => {
                        console.log(e)
                    })
            },
            deleteNode() {
                axios.delete(this.deleteUrl, {auth: this.auth})
                    .then(response => {
                        if (response.data == 'node deleted') {
                            this.$store.dispatch('updateNodes')
                            this.$router.push({name: 'nodes'})  // redirect
                        } else {
                            alert('node was not deleted')
                        }
                    })
                    .catch(e => {
                        console.log(e)
                    })
            },
            putNodeName() {
                axios.put(this.url, {name: this.newName}, {auth: this.auth})
                    .then(response => {
                        this.$store.dispatch('updateNodes')
                    })
                    .catch(e => {
                        console.log(e)
                    })
                this.name = this.newName
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
