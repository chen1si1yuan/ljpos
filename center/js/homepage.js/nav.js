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
                                    <li class="header-menu-li" :id=nav.className @mouseover="headerover(nav.id)" @mouseout="headerout"  @click="changeActive(nav.id)" :class="{headeractive:nav.id==flog,headerhovser:nav.id==hovershow}" v-for='nav in nav'><a :href="nav.url">{{nav.title}}</a>
                                        <ul v-if=nav.subnav class="menu-child" :class="{target:show}">
                                            <li @click="goto(childLi.url)" v-for='childLi in nav.subnav' ><a :href="childLi.url">{{childLi.value}}</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>

                            <div class="header-user">
                                    <div class="header-btn">
                                        <span>登录</span>
                                        <span>注册</span>
                                    </div>
                            </div>
                        </div> 
                    </nav>`,
        data:function(){
            return{
                logourl:"./images/lg-img/WechatIMG15.jpeg",
                flog:0,
                show:true,
                hovershow:0,//鼠标移动上去
                nav:[ 
                    {className:"headerli1",id:1,title:"服务商城",url:"",subnav:[
                            {id:1,value:"故宫问答",url:"index.html"},
                            {id:2,value:"故宫问答",url:"help.html"},
                            {id:3,value:"故问答",url:"index.html"}
                        ]
                    },
                    {className:"headerli2",id:2,title:"解决方案",url:"solution.html",subnav:[]
                    },
                    {className:"headerli3",id:3,title:"创建应用",url:"app.html",subnav:[]
                    },
                    {className:"headerli4",id:4,title:"帮助中心",url:"help.html",subnav:[]
                    }
                ]
            }
        },
    methods:{
        //某一菜单被选中
        changeActive:function(index){
            this.flog=index;
        },
        headerover:function(index){
            if(index==1){
                
            }
            if(index!=1){
                this.hovershow=index;
            }
        },
        headerout:function(){
            this.hovershow=0;
        },
        //子菜单点击事件
        goto:function(index){
            console.log(index);
        }
    }
    }
)