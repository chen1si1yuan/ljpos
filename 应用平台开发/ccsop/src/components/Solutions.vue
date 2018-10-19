<template>
    <div id="solution">
        <div class="solution-part1">
            <h1>{{p1title}}</h1>
            <p>
                <a href="#">{{company}}</a><br>
                <span></span><br>
                <a class="look-provide-service" href="#">{{lookprovideservice}}<span>></span></a>
            </p>
            
        </div>
        <div class="solution-part2">
            <div class="solution2-con"> 
                <h1>{{p2title}}</h1>
                <p>{{p2artic}}</p>
            </div>
        </div>
        <div class="solution-part3">
            <div class="solution3-con">
                <div v-for="item in suitList" :key="item.suitid">
                    <h3>{{item.type}}</h3>
                    <p>{{item.name}}</p>
                    <img :src="item.picSrc" alt="">
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import robot from '@/assets/img/solutions/robot.png'
import AIhome from '@/assets/img/solutions/AIhome.png'
import movePC from '@/assets/img/solutions/movePC.png'
export default {
    name:"solution",
    data(){
        return{
            p1title:'',
            company:'',
            lookprovideservice:'',
            p2title:'',
            p2artic:'',
            suitList:[
                {"suitid":1,"type":"适用场景1",'name':"智能机器人",picSrc:robot},
                {"suitid":2,"type":"适用场景2",'name':"智能家居",picSrc:AIhome},
                {"suitid":3,"type":"适用场景3",'name':"移动端、桌面端、网页端应用",picSrc:movePC}
            ]
        }
    },
    created(){
        this.p1title='数据安全解决方案',
        this.company='富士康科技集团',
        this.lookprovideservice='查看方案提供服务',
        this.p2title='什么是自然语言处理解决方案',
        this.p2artic='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean euismod bibendum laoreet. Proin gravida dolor sit amet lacus accumsan et  viverra justo commodo. Proin sodales pulvinar sic tempor. Sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam fermentum, nulla luctus pharetra vulputate, felis tellus mollis orci, sed rhoncus pronin sapien nunc accuan eget.'
    }
}
</script>

<style lang="scss">
#solution{
    width: 100%;
    height: auto;
    .solution-part1{
        font-family: PingFangSC-Regular;
        width: 100%;
        height: 500px;
        background: url(../assets/img/solutions/banner@3x.png) no-repeat;
        background-size: cover;
        h1{
            color:white;
            font-size: 60px;
            padding: 114px 0px 0 336px;
        }
        p{
            font-size: 32px;
            padding: 43px 0 0 335px;
            span{
                display: inline-block;
                height: 73px;
                width: 20px;
            }
            .look-provide-service{
                font-size: 20px;
                border: 1px solid ;
                padding: 13px 34px;
                span{
                   padding-left: 30px; 
                }
            }
        }
    }
    .solution-part2{
        height: 442px;
        width: 100%;
        background: white;
        .solution2-con{
            text-align: center;
            font-family: PingFangSC-Regular;
            h1{
                font-size: 32px;
                color: #32323E;
                padding: 100px 0  90px 0;
            }
            p{
                font-size: 18px;
                padding:0 342px 0 342px;
            }
        }
    }
    .solution-part3{
        width: 100%;
        background: #F4F7FF;
        height: 778px;
        .solution3-con{
            margin-left: 300px;
            padding-top: 182px;
            div{
                display: inline-block;
                text-align: center;
                height: 411px;
                width: 363px;
                margin-right: 80px;
                background: white;
                h3{
                    padding-top: 36px;
                    color: #32323E;
                    font-size: 24px;
                }
                p{
                    color: #565660;
                    font-size: 18px;
                    padding: 40px 0 49px 0;
                }
                img{
                    height: 177px;
                    width: 202px;
                }
            }            
        }

    }
}
</style>

