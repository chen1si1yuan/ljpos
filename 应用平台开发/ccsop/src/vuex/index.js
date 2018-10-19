import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

import userLogoUrl from '@/assets/img/login_register/userlogo.jpg';

/* 页面标志状态量 */
const modulePageStatus = {
    state: {  
        user: {
            isLogin: true
        },
        header: {
            currentNavList: 'index',
            currenSubNav: 'default',
        },     
        personCenter: { /* 个人中心 */
            currentSecondNav: 'PresonInfo-baseinfo'
        },
        presonInfo: {
            /* 正在修改基本资料 */
            isChangingBaseInfo: false,
            /* 验证真实资料中 */
            isChangingRealInfo: false,
            /* 真实资料验证完成 */
            changedRealInfo: false
        }
    },
    mutations: {},
    actions: {},
    getters: {
        getUserRealInfoState: (state) =>{
            if(!state.presonInfo.isChangingRealInfo){
                return {
                    'isChange': false,
                    'msg': {
                        userRealName: '',
                        userCardId: '',
                        userAddress: ''
                    }

                }
            }else if(state.presonInfo.isChangingRealInfo && !state.presonInfo.changedRealInfo){
                return {
                    'isChange': true,
                    'msg': {
                        userRealName: '验证中......',
                        userCardId: '验证中......',
                        userAddress: '验证中......'
                    }
                }
            }else if(state.presonInfo.isChangingRealInfo && state.presonInfo.changedRealInfo) {
                return {
                    'isChange': true,
                    'msg': {
                        userRealName: '小姐姐',
                        userCardId: '510129199211088237',
                        userAddress: '广东省深圳市龙华新区'
                    }
                }
            }
        }
    }
}

/* 网站公共数据 */
const modulePublicData = {
    state: {
        userinfo:{
            userCount: '1234567890',
            userLogoUrl: userLogoUrl,
            userNickName: '执子之手偕老',
            isIdentificate_msg:  '未认证',
            userTel: '18617280963',
            userEmail: '670178902@qq.com',
            userPwd: '************'
        }
    },
    mutations: {},
    actions: {},
    getters: {}
}

export default new Vuex.Store({
    modules: {
        pageStatus: modulePageStatus,
        publicData: modulePublicData
    }
});