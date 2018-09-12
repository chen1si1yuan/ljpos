Vue.component(
    'header-part',{
        template:` <nav id="header-part">
                        <div class="header-container">
                            <div class="header-title" >
                                <div class="header-logo">
                                        <img class="header-logo-pic" :src='logourl'> 
                                </div>
                                <div class="header-title-box">
                                    <span class="header-title-word"><a href="#">中控服务开放平台</a></span>
                                </div>
                                
                            </div>
                            <div class="header-menu">
                                <ul class="header-menu-ul" >
                                    <li class="header-menu-li" :class="{active:nav.id==flog}"  @click="active(nav.id)" v-for='nav in nav'><a href="#">{{nav.title}}</a>
                                        <ul v-if=nav.subnav class="menu-child" :class="{target:show}">
                                            <li v-for='childLi in nav.subnav' @click="goto(childLi)"><a href="#">{{childLi.value}}</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>

                            <div class="header-user">
                                    <div class="header-btn">
                                        <span><a href="#">登录</a></span>
                                        <span><a href="#">注册</a></span>
                                    </div>
                            </div>
                        </div> 
                    </nav>`,
        data:function(){
            return{
                logourl:"./images/lg-img/WechatIMG15.jpeg",
                flog:0,
                show:true,
                nav:[ 
                    {id:1,title:"服务商城",url:"",subnav:[
                            {id:1,value:"故宫问答",url:""},
                            {id:2,value:"故宫问答",url:""},
                            {id:3,value:"故问答",url:""}
                        ]
                    },
                    {id:2,title:"解决方案",url:"",subnav:[
                            {id:1,value:"解决方案",url:""},
                            {id:2,value:"解决方案",url:""},
                            {id:3,value:"解决方案",url:""},
                            {id:4,value:"解决方案",url:""}
                        ]
                    },
                    {id:3,title:"创建应用",url:"",subnav:[]
                    },
                    {id:4,title:"帮助中心",url:"",subnav:[
                            {id:1,value:"帮助中心",url:""},
                            {id:2,value:"帮助中心",url:""},
                            {id:3,value:"帮助中心",url:""}
                        ]
                    }
                ]
            }
        },
    methods:{
        //某一菜单被选中
        active:function(index){
            this.flog=index
        },
        //子菜单点击事件
        goto:function(index){
            console.log(index.id);
        }
    }
    }
)