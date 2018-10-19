<template>
    <div id="helpCenter">
        <div class="help-center-menu">
            <ul class="nav-menu">
                <li v-for="(navMenuList, index) in helpMenu" :key="index">
                    <i :class="navMenuList.ilogo"></i>{{navMenuList.name}}
                        <ol>
                            <li v-for="(subItem, subIndex) in navMenuList.subMenu" :key="subIndex">    
                                <router-link :to="subItem.link" class="sub-router" >{{subItem.name}}</router-link>         
                            </li>
                        </ol>
                </li>
            </ul>
        </div>
        <div class="help-center-content">
            <router-view />
        </div>
    </div>
</template>

<script>
export default {
    name:'helpCenter',
    data(){
        return{
            helpMenu:[
                {ilogo:'fa fa-book',name:'入门指南',subMenu:[
                    {ilogo:'',name:'平台简介',link:'gettingStart',go:'gettingstart-introduce'},
                    {ilogo:'',name:'平台操作流程',link:'gettingStart',go:'gettingstart-operation'}
                ]},
                {ilogo:'fa fa-cubes',name:'创建应用',subMenu:[
                    {ilogo:'',name:'创建步骤1',link:'createApp',go:'createApp-one'},
                    {ilogo:'',name:'创建步骤2',link:'createApp',go:'createApp-two'}
                ]},
                {ilogo:'fa fa-indent',name:'服务使用',subMenu:[
                    {ilogo:'',name:'服务1',link:'serverUse',go:'serverUse-one'},
                    {ilogo:'',name:'服务2',link:'serverUse',go:'serverUse-two'}
                ]},
                {ilogo:'fa fa-question',name:'常见问题',subMenu:[
                    {ilogo:'',name:'常见问题1',link:'allQuestion',go:'allQuestion-one'},
                    {ilogo:'',name:'常见问题',link:'allQuestion',go:'allQuestion-two'}
                ]}]
        }
    }
}
</script>

<style lang="scss">
#helpCenter{
    background: pink;
    width: 100%;
    .help-center-menu{
        width: 174px;
        height: auto;
        background: #EDEDF0;
        text-align: center;
        .nav-menu{
                padding-top: 5px;
                >li{
                    color: #383849;
                    font-family: PingFangSC-Regular;
                    font-size: 18px;
                    i{
                        padding-right: 10px;
                    }
                    li{
                        text-align: left;
                        font-family: PingFangSC-Regular;
                        font-size: 16px;
                        padding: 13px;
                        padding-left: 40px;
                        .sub-router{
                            color: #383849;
                        }
                        &:hover{
                            border-left: 5px solid #4F74FF;
                            background:rgba(79,116,255,0.1);
                        }
                         &:hover .sub-router{
                            color: #4F74FF;
                        }
                    }
                    :first-child{
                        margin-top: 15px;
                    }
                }
        }
    }
}
</style>

