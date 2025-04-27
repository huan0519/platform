import Vue from "vue";
import Vuex from 'vuex';
import vuexEsm from "vuex";

Vue.use(Vuex);

const store = new vuexEsm.Store({
    state: {
        currentPathName: ''
    },
    mutations: {
        setPath (state) {
            state.currentPathName = localStorage.getItem('currentPathName')
        }
    }
})
export default store
