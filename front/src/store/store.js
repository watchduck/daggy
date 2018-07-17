import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        nodes: [
            {"id": 1, "name": "One"},
            {"id": 2, "name": "Two"},
            {"id": 3, "name": "Three"},
            {"id": 4, "name": "Four"},
            {"id": 5, "name": "Five"},
            {"id": 6, "name": "Six"},
            {"id": 7, "name": "Seven"},
            {"id": 8, "name": "Eight"},
            {"id": 9, "name": "Nine"},
            {"id": 10, "name": "Ten"},
            {"id": 11, "name": "Eleven"},
            {"id": 12, "name": "Twelve"},
            {"id": 13, "name": "Thirteen"}
        ],
        nodeRelatives: {
            1: [
                [],
                [{"id": 2, "name": "Two"}, {"id": 10, "name": "Ten"}]
            ],
            2: [
                [{"id": 1, "name": "One"}],
                [{"id": 9, "name": "Nine"}, {"id": 3, "name": "Three"}, {"id": 4, "name": "Four"}, {"id": 5, "name": "Five"}]
            ],
            3: [
                [{"id": 2, "name": "Two"}],
                [{"id": 8, "name": "Eight"}]
            ],
            4: [
                [{"id": 2, "name": "Two"}],
                [{"id": 12, "name": "Twelve"}, {"id": 6, "name": "Six"}, {"id": 7, "name": "Seven"}]
            ],
            5: [
                [{"id": 2, "name": "Two"}],
                [{"id": 7, "name": "Seven"}, {"id": 8, "name": "Eight"}]
            ],
            6: [
                [{"id": 4, "name": "Four"}],
                []
            ],
            7: [
                [{"id": 4, "name": "Four"}, {"id": 5, "name": "Five"}],
                []
            ],
            8: [
                [{"id": 5, "name": "Five"}, {"id": 3, "name": "Three"}],
                []
            ],
            9: [
                [{"id": 2, "name": "Two"}],
                [{"id": 10, "name": "Ten"}, {"id": 11, "name": "Eleven"}, {"id": 12, "name": "Twelve"}]
            ],
            10: [
                [{"id": 1, "name": "One"}, {"id": 9, "name": "Nine"}],
                [{"id": 13, "name": "Thirteen"}]
            ],
            11: [
                [{"id": 9, "name": "Nine"}],
                []
            ],
            12: [
                [{"id": 9, "name": "Nine"}, {"id": 4, "name": "Four"}],
                [{"id": 13, "name": "Thirteen"}]
            ],
            13: [
                [{"id": 10, "name": "Ten"}, {"id": 12, "name": "Twelve"}],
                []
            ]
        }
    }
})
