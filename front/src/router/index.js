import Vue from 'vue'
import Router from 'vue-router'

import Node from '../components/Node'
import Nodes from '../components/Nodes'

Vue.use(Router)

export default new Router({
    routes: [
        {path: '/nodes', component: Nodes, name: 'nodes'},
        {path: '/nodes/:id', component: Node, name: 'node'},
    ],
    mode: 'history'
})
