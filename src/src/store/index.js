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
        isLoggedIn: JSON.parse(localStorage.getItem('isLoggedIn')) || false, // 恢复登录状态
        userName: localStorage.getItem('userName') || '', // 恢复用户名
        userAvatar: localStorage.getItem('userAvatar') || '', // 恢复用户头像
        activeIndex: 'homepage',
    },

    getters:{

    },

    mutations:{
        setActiveIndex(state, index) {
            state.activeIndex = index; // 更新导航状态
        },
        setLoginState(state, { isLoggedIn, userName, userAvatar }) {
            state.isLoggedIn = isLoggedIn;
            state.userName = userName;
            state.userAvatar = userAvatar;

            // 将状态存储到 localStorage
            localStorage.setItem('isLoggedIn', JSON.stringify(isLoggedIn));
            localStorage.setItem('userName', userName);
            localStorage.setItem('userAvatar', userAvatar);
        },
        clearLoginState(state) {
            state.isLoggedIn = false;
            state.userName = '';
            state.userAvatar = '';

            // 清除 localStorage 中的状态
            localStorage.removeItem('isLoggedIn');
            localStorage.removeItem('userName');
            localStorage.removeItem('userAvatar');
        },
    },

    actions:{
        updateActiveIndex({ commit }, index) {
            commit('setActiveIndex', index); // 调用 mutation
        },
        login({ commit }, userData) {
            commit('setLoginState', {
                isLoggedIn: true,
                userName: userData.username,
                userAvatar: userData.avatar_url,
            });
        },
        logout({ commit }) {
            commit('clearLoginState');
        },
    },

    modules:{

    }
})