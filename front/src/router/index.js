import Vue from 'vue'
import Router from 'vue-router'

import Node from '../components/Node.vue'


Vue.use(Router)

export default new Router({
    routes: [
        {path: '/nodes/:id', component: Node, name: 'node'},
    ],
    mode: 'history'
})
