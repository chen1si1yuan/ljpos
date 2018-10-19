<template>
    <div id="personCenter">
        <div class="person-center-menu">
            <ul>
                <li v-for="(item, index) in navMenu" :key="index">
                    <div class="person-center-first-menu">
                        <span :class="item.ilogo"></span>                        
                        <p>{{item.name}}</p>
                    </div>
                    <ol>
                        <li v-for="(subItem, subIndex) in item.subMenu" :key="subIndex" 
                        :class="{ 'person-center-second-menu': true,'selected-menu': getcurrentSecondNav==subItem.go}"
                         >                           
                            <router-link :to="subItem.link" @click.native="changeSecondNav(subItem.go)" >{{subItem.name}}</router-link>              
                        </li>
                    </ol>
                </li>
            </ul>
        </div>            
        <div class="person-center-content">
            <router-view />
        </div>        
    </div>    
</template>

<script>
export default {
    name: 'personCenter',
    data() {
        return {
            /* 导航菜单 */
            navMenu: [
                {
                    ilogo: "fa fa-user",
                    name: '个人信息',
                    subMenu: [
                        {ilogo: '', name: '基本资料', link: 'PresonInfo', go:'PresonInfo-baseinfo'},
                        {ilogo: '', name: '实名认证', link: 'PresonInfo', go:'PresonInfo-authenticate'}
                    ]
                },
                {
                    ilogo: 'fa fa-th-large',
                    name: '我的应用',
                    subMenu: [
                        {ilogo: '', name: '应用列表', link: 'MyApp', go:'MyApp-list'},
                        {ilogo: '', name: '创建应用', link: 'MyApp', go:'MyApp-create'}
                    ]
                },
                {
                    ilogo: 'fa fa-question-circle',
                    name: '问题反馈',
                    subMenu: [
                        {ilogo: '', name: '问题创建', link: 'Problem', go:'Problem-create'},
                        {ilogo: '', name: '问题列表', link: 'Problem', go:'Problem-list'}
                    ]
                },
                {
                    ilogo: 'fa fa-bell',
                    name: '消息通知',
                    subMenu: [
                        {ilogo: '', name: '消息列表', link: 'Message', go:'Message-list'}
                    ]
                }
            ]
        }
    },
    computed: {
        getcurrentSecondNav() {
            return this.$store.state.pageStatus.personCenter.currentSecondNav;
        }    
    },    
    methods: {
        changeSecondNav(go) {
            let isChangingBaseInfo = this.$store.state.pageStatus.presonInfo.isChangingBaseInfo;
            if(go=='PresonInfo-authenticate' && isChangingBaseInfo){
                if(confirm('您正在修改个人资料，确定撤销修改？')){
                    this.$store.state.pageStatus.personCenter.currentSecondNav = go;
                    this.$store.state.pageStatus.presonInfo.isChangingBaseInfo = false;
                    return ;
                }else{
                    return ;
                }
            }
            this.$store.state.pageStatus.personCenter.currentSecondNav = go;
        }
    },
    mounted: function() {        
    }

}
</script>

<style lang="scss">
#personCenter{
    display: flex;
    flex-direction: row;
    height: 100%;
}
.person-center-menu {
    color: #383849;
    width: 200px;
    height: auto;
    padding-top: 30px;
    background-color: #EDEDF0;

    a{
        color: #383849;
        
    }

    .person-center-first-menu{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
        font-size: 18px;
        font-weight: 400;       
        .fa{            
            margin-right: 10px;    
        }        
    }
    .person-center-second-menu {
        text-align: center;
        height: 50px;
        line-height: 50px;
        font-size: 16px;
        &:hover{
            background-color: #DDE1F2;
            border-left: 5px solid #4F74FF;
            font-weight: 800;
        }
    }
    .selected-menu{
        background-color: #DDE1F2;
        border-left: 5px solid #4F74FF;
        font-weight: 800;
    }
}
.person-center-content{
    width: 100%;
}

</style>
