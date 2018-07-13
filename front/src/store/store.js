import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        nodes: [],
        backUrlBase: 'http://localhost:8000/',
        auth: {username: 'myname', password: 'mysecret'}
    },
    getters: {
        backUrlNodes(state) {
            return state.backUrlBase + 'api/node/'
        }
    },
    mutations: {
        UPDATE_NODES(state, payload) {
            state.nodes = payload
        }
    },
    actions: {
        updateNodes() {
            axios.get(this.getters.backUrlNodes, {auth: this.state.auth})
                .then(response => {
                    this.commit('UPDATE_NODES', response.data)
                })
                .catch(e => {
                    console.log(e)
                })
        }
    }
})
