import Vue from 'vue'
import Router from 'vue-router'
import Mainpage from '@/components/MainPage.vue'
import Servive from '@/components/Servive.vue'
import Solutions from '@/components/Solutions.vue'
import Application from '@/components/Application.vue'

/* 个人中心 */
import Personcenter from '@/components/person/PersonCenter.vue'
/* import Personnav from '@/components/person/PresonNav.vue' */
import Presoninfo from '@/components/person/PresonInfo.vue'
import Myapp from '@/components/person/MyApp.vue'
import Problem from '@/components/person/Problem.vue'
import Message from '@/components/person/Message.vue'

/* 帮助中心 */
import Help from '@/components/help/Help.vue'
import GettingStart from '@/components/help/GettingStart.vue'
import CreateApp from '@/components/help/CreateApp.vue'
import ServerUse from '@/components/help/ServerUse.vue'
import allQuestion from '@/components/help/allQuestion.vue'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index-Mainpage',
      component: Mainpage
    },
    {
      path: '/Mainpage',
      name: 'Mainpage',
      component: Mainpage
    },
    {
      path: '/Servive',
      name: 'Servive',
      component: Servive
    },
    {
      path: '/Solutions',
      name: 'Solutions',
      component: Solutions
    },
    {
      path: '/Application',
      name: 'Application',
      component: Application
    },
    {
      path: '/Help',
      name: 'Help',
      component: Help,
      children:[
        {
          path:'/Help/GettingStart',
          name:'GettingStart',
          component:GettingStart
        },{
          path:'/Help/CreateApp',
          name:'CreateApp',
          component:CreateApp
        },{
          path:'/Help/ServerUse',
          name:'ServerUse',
          component:ServerUse
        },{
          path:'/Help/allQuestion',
          name:'allQuestion',
          component:allQuestion
        }
      ]
    },
    {
      path: '/Personcenter',
      name: 'Personcenter',      
      component: Personcenter,      
        children:[
          {
            path: '/Personcenter/Presoninfo',
            name: 'Presoninfo',
            component: Presoninfo
          },
          {
            path: '/Personcenter/Myapp',
            name: 'Myapp',
            component: Myapp
          },
          {
            path: '/Personcenter/Problem',
            name: 'Problem',
            component: Problem
          },
          {
            path: '/Personcenter/Message',
            name: 'Message',
            component: Message
          },
        ]
      
      
    }    
  ]
})
