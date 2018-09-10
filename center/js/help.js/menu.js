var list_li1 = new Vue({
    el:"#word_part",
    data:{
        li_title:"入门指南",
        li_part1:"平台简介",
        li_part2:"平台操作流程",
        li_art1:"中控",
        li_art2:"登录注册实名认证",
    },
    components:{
        "art_part":{
            template:'<div>\
                <button @click="change1">入门指南</button>\
                <button @click="change2">应用创建指南</button>\
                <button @click="change3">服务使用指南</button>\
                <button @click="change4">常见问题</button>\
                <h2 class="li_title">{{li_title}}</h2>\
                <h3 class="li_part1 li_part">{{li_part1}}</h3>\
                <p class="li_art1 li_art">{{li_art1}}</p>\
                <h3 class="li_part2 li_part">{{li_part2}}</h3>\
                <p class="li_art2 li_art">{{li_art2}}</p>\
            </div>',
            props:['li_title','li_part1','li_part2','li_art1','li_art2'],
            methods:{
                change1:function(){
                    this.li_title='入门指南'
                    this.li_part1='入门指南等等'
                    this.li_part2='入门指南等等'
                    this.li_art1='入门指南等等详情'
                    this.li_art2='入门指南等等详情'
                },
                change2:function(){
                    this.li_title='应用服务指南'
                    this.li_part1='应用服务指南等等'
                    this.li_part2='应用服务指南等等'
                    this.li_art1='应用服务指南等等详情'
                    this.li_art2='应用服务指南等等详情'
                },
                change3:function(){
                    this.li_title='服务使用指南'
                    this.li_part1='服务使用指南等等'
                    this.li_part2='服务使用指南等等'
                    this.li_art1='服务使用指南等等详情'
                    this.li_art2='服务使用指南等等详情'
                },
                change4:function(){
                    this.li_title='常见问题'
                    this.li_part1='常见问题等等'
                    this.li_part2='常见问题等等'
                    this.li_art1='常见问题等等详情'
                    this.li_art2='常见问题等等详情'
                }
            }
        }
    }
})