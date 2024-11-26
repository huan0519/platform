import Vue from "vue";
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        user: {
            username: '',
            password: '',
            avatar_url: '',
            token: '',
        },
        activeIndex: 'homepage',
    },

    getters:{

    },

    mutations:{
        setActiveIndex(state, index) {
            state.activeIndex = index; // 更新导航状态
        },
    },

    actions:{
        updateActiveIndex({ commit }, index) {
            commit('setActiveIndex', index); // 调用 mutation
        },
    },

    modules:{

    }
})