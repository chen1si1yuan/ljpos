#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
from base import skillbase
from robot.struct.ttypes import *
import skillui
import json
class _450f787ed1b94b6a93c27fd730334ae7jn(skillbase):
    def get_founder_desc(self, name):
        info = {
          	'糖醋排骨':'糖醋排骨，是糖醋味型中具有代表性的一道大众喜爱的特色传统名菜。'
          		'它选用新鲜猪子排作主料，肉质鲜嫩，成菜色泽红亮油润。',
          	'十全大补汤':'“十全大补汤”选鲜料加入十味中药，五味小料，五味调料，细火炖制而成，既是一道咸鲜味浓的汤菜，又是一款药膳'
          		'富有营养，滋补身体，久食对冠心病、高血压、糖尿病、贫血、气喘、面黄体弱者有一定的疗效。',
          	'北京烤鸭':'烤鸭是具有世界声誉的北京著名菜式，起源于中国南北朝时期，《食珍录》中已记有炙鸭，在当时是宫廷食品。'
          		'用料为优质肉食鸭北京鸭，果木炭火烤制，色泽红润，肉质肥而不腻，外脆里嫩。北京烤鸭分为两大流派，而北京最著名的烤鸭店也即是两派的代表。它以色泽红艳，肉质细嫩，味道醇厚，肥而不腻的特色，被誉为“天下美味”。',
          	'可乐鸡翅':'可乐鸡翅具有味道鲜美、色泽艳丽、鸡肉嫩滑、咸甜适中的特点。'
          		'可乐鸡翅是一道以鸡翅和可乐为主料，以料酒、葱、姜、酱油、盐、鸡精作为调料制作而成的美食。',
            '小炒肉':'小炒肉，是湖南省一道常见的特色传统名菜，属于湘菜系。'
				'麻辣鲜香，口味滑嫩。制作原料主要是五花肉和青椒、红椒等',
            '宫保鸡丁':'宫保鸡丁，是一道闻名中外的特色传统名菜。鲁菜、川菜、贵州菜中都有收录，'
				'原料、做法有差别。[1]  该菜式的起源与鲁菜中的酱爆鸡丁，和贵州菜的胡辣子鸡丁有关，'
				'后被清朝山东巡抚、四川总督丁宝桢改良发扬，形成了一道新菜式——宫保鸡丁，'
				'并流传至今，此道菜也被归纳为北京宫廷菜[2]  。之后宫保鸡丁也流传到国外。',
            '水煮肉片':'水煮肉片，是一道地方新创名菜，起源于自贡，发扬于西南，属于川菜中著名的家常菜  '
          		'。因肉片未经划油，以水煮熟故名水煮肉片'
        }

        if name in info.keys():
            return info[name]
        return '菜单里没有这个菜哦'

    def get_founder_picurl(self, name):
        info2 = {
          	 '北京烤鸭':'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=a7828fb83987e950561afb3e71513826/738b4710b912c8fcd24c76b6ff039245d6882109.jpg',
          	 '糖醋排骨':'http://i8.meishichina.com/attachment/recipe/2014/06/11/20140611140717217157565.jpg@!p800',
          	 '十全大补汤':'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike92%2C5%2C5%2C92%2C30/sign=94ced97db3de9c82b268f1dd0de8eb6f/f9198618367adab44c7b26078bd4b31c8601e4ce.jpg',
          	 '可乐鸡翅':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534998625590&di=e5662e5a34a6f72f20f4cb85b66824f5&imgtype=0&src=http%3A%2F%2Fcp2.douguo.net%2Fupload%2Fcaiku%2Fb%2F9%2Ff%2Fyuan_b9f3b8d3323fd0a89e1555c0217e141f.jpg',
             '小炒肉':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534997959657&di=f9b0f2f52d654ad9f8198f5932e37b92&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170717%2Fdcdc5d19a9f54d709b688e9a9068533a_th.jpg',
             '宫保鸡丁':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516852524774&di=ae10ddd05b60fa8f46a4ae661666aa1e&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimage%2Fc0%253Dpixel_huitu%252C0%252C0%252C294%252C40%2Fsign%3Daf8cc03b576034a83defb0c1a26b2c38%2Fa686c9177f3e6709ff940cc530c79f3df8dc5577.jpg',
             '水煮肉片':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516852037888&di=94d4fd670c26edb9ec69e2dcb5c2bad1&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimage%2Fc0%253Dpixel_huitu%252C0%252C0%252C294%252C40%2Fsign%3Db02e84fe10d5ad6ebef46caae8b35cb7%2Faa64034f78f0f736cdf6f33b0155b319ebc413fb.jpg'
        }

        if name in info2.keys():
            return info2[name]
        return 'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=28460166b819ebc4d4757ecbe34fa499/b3119313b07eca80344f07e49a2397dda144836e.jpg'
    def food_price(self,name):
        info3 = {
          	 '北京烤鸭':'99',
          	 '糖醋排骨':'66',
          	 '十全大补汤':'88',
          	 '可乐鸡翅':'36',
             '小炒肉':'40',
             '宫保鸡丁':'30',
             '水煮肉片':'48'
        }

        return info3[name]
    def food_num(self,num):
        num1 = {
          '两':'2'
        }
        return num1[num]
     
    def get_comp_desc(self):
        desc = '点菜系统简介'
        return desc

    def get_help(self):
        return '你可以问介绍一下鱼香肉丝，鱼香肉丝多少钱，买单'
    def get_new_menu(self):
        menu= {
          'menuList':[
          ]
        }
        return menu;
    def get_new_item(self,name,count):
        item= {
          'name':name,
            'count':count
        }
        return item;
    
    def handle(self, context, intent):
      	global localMenu
        try:
          	#将skill_data中的数据转为python的数据结构 localMenu为字典，方便之后操作
            localMenu = json.loads(context.skill_data.values['localMenu'])
        except Exception:
            context.skill_data.values = {'localMenu':''}#当localMenu不存在时则初始化
            localMenu = self.get_new_menu()
        if context.skill_cmd == SkillCmd.Open:
            context.skill_reply.reply = '欢迎使用点菜系统，在这里您可以查询菜品简介，点菜，及买单哦'
        elif context.skill_cmd == SkillCmd.Close:   
            context.skill_reply.reply = '感谢您使用点菜系统，欢迎您再次使用'
            context.skill_data.values = {}
        else:
            intent_type = intent['intent']
            slot_values = intent['slot_values']
            slot_dict = intent['slot_dict']
            if intent_type == 'introuceMenuIntent':
                name_slot = slot_values[0].encode('utf-8')
                pic_url = self.get_founder_picurl(name_slot)
                context.skill_reply.reply = self.get_founder_desc(name_slot)
                it4 = skillui.getSingleComponent(name_slot,'',pic_url,self.get_founder_desc(name_slot))
                context.skill_reply.ui_reply = it4
            if intent_type == 'AllFoodIntent':
                context.skill_reply.reply = '我们有这些菜哦……'
                it1 = skillui.getSingleComponent('糖醋排骨','',self.get_founder_picurl('糖醋排骨'),self.get_founder_desc('糖醋排骨'))
                it2 = skillui.getSingleComponent('宫保鸡丁','',self.get_founder_picurl('宫保鸡丁'),self.get_founder_desc('宫保鸡丁'))
                it3 = skillui.getSingleComponent('水煮肉片','',self.get_founder_picurl('水煮肉片'),self.get_founder_desc('水煮肉片'))
                it4 = skillui.getSingleComponent('小炒肉','',self.get_founder_picurl('小炒肉'),self.get_founder_desc('小炒肉'))
                it5 = skillui.getSingleComponent('十全大补汤','',self.get_founder_picurl('十全大补汤'),self.get_founder_desc('十全大补汤'))
                it6 = skillui.getSingleComponent('北京烤鸭','',self.get_founder_picurl('北京烤鸭'),self.get_founder_desc('北京烤鸭'))
                it7 = skillui.getSingleComponent('可乐鸡翅','',self.get_founder_picurl('可乐鸡翅'),self.get_founder_desc('可乐鸡翅'))
                items = [it1,it2,it3,it4,it5,it6,it7]
                context.skill_reply.ui_reply = skillui.getListComponent(items)	
            if intent_type == 'picIntent':
                name_slot = slot_dict[u'菜品'].encode('utf-8')
                pic_url = self.get_founder_picurl(name_slot)
                context.skill_reply.reply = self.get_founder_desc(name_slot)
                it4 = skillui.getPicComponent(name_slot,pic_url)
                context.skill_reply.ui_reply = it4
            if intent_type == 'orderFood':
              	try:
                  name_slot = slot_dict[u'菜品'].encode('utf-8')
                  food_num = slot_dict[u'数量'].encode('utf-8')
                  food_type = slot_dict[u'单位'].encode('utf-8')
                except:
                  name_slot = slot_dict[u'菜品'].encode('utf-8')
                  food_num = "1"
                  food_type = "份"
                menu_list=''
                f=0
                for menuArr in localMenu.itervalues():
                  if(len(menuArr)>0):
                  	for i in menuArr:
                          #已经点过本菜 在数量上追加
                         if(str(i['name'])==name_slot):
                          if food_num=='两':
                              food_num = str(self.food_num(str(food_num)))
                          i['count']=int(i['count'])+int(food_num)
                          f=1
                        break
                if(f==0):
                  	if food_num == '两':
                         food_num =self.food_num(str(food_num))
                	new_order_item = self.get_new_item(name_slot,food_num)
                #将新点的菜放入localMenu的menuList中
                	localMenu['menuList'].append(new_order_item)
                #将字典转为一个字符串存入skill_data中
                menustring = json.dumps(localMenu)
                context.skill_data.values['localMenu'] = menustring
              	context.skill_reply.reply =food_num+'份'+name_slot+"点菜成功"
            if intent_type == 'cancelFood':
              	name_slot=''
              	name_slot = slot_values[0].encode('utf-8')
                for menuArr in localMenu.itervalues():
                  for j in menuArr:
                    if j['name']==name_slot and j['count']!=0:
                      j['count']=0
                      context.skill_reply.reply = name_slot+'已经退了'
                      break
                    else:
                      context.skill_reply.reply ="不好意思，没有这个菜"
                #修改了localMenu后需要跟新Skill_data中的数据
                menu_list=''
                menustring = json.dumps(localMenu)
                context.skill_data.values['localMenu'] = menustring
            if intent_type == 'whatChange':
              context.skill_reply.reply ="好的哦，你可以这样像对我说    我们想把宫保鸡丁换成小炒肉  请帮我们把宫保鸡丁换成小炒肉  我们的宫保鸡丁换成小炒肉"
              +"宫保鸡丁换成小炒肉  我们想把宫保鸡丁改成小炒肉  宫保鸡丁改成小炒肉  我们的宫保鸡丁改成小炒肉"
            if intent_type == 'changeFood':
              	old_food = slot_dict[u'菜品'].encode('utf-8')
                new_food = slot_dict[u'新菜品'].encode('utf-8')
                for menuArr in localMenu.itervalues():
                  for j in menuArr:
                    if j['name']==old_food and j['count']!=0:
                      j['name']=new_food
                      context.skill_reply.reply = old_food+'已经换成'+new_food
                      break
                    else:
                      context.skill_reply.reply ="不好意思，没有这个菜"
                menustring = json.dumps(localMenu)
                context.skill_data.values['localMenu'] = menustring
            if intent_type == 'payMoney':
                money="0"
                cost_money = 0
                food_numStr=''
                menu_list=''
                for menuArr in localMenu.itervalues():
                  if(len(menuArr)>0):
                      for i in menuArr:
                        menu_list += str(i['name'])+str(i['count'])+'份  '
                        money = self.food_price(str(i['name']))
                        food_numStr =str(i['count'])
                        cost_money += int(money)*int(food_numStr)
                      context.skill_reply.reply = '你好，本次用餐为'+menu_list+'   一共消费：'+str(cost_money)+'元'
                  else:
                    context.skill_reply.reply='你们还没有消费哦'
                context.skill_data.values = {}
                
            if intent_type == 'confirm':
                menu_list=''
                for menuArr in localMenu.itervalues():
                  if(len(menuArr)>0):
                  	for i in menuArr:
                         menu_list += str(i['name'])+str(i['count'])+'份  '
                        context.skill_reply.reply = '你好，您一共点了'+ menu_list +'这些菜'
                  else:
                    context.skill_reply.reply = '你好，你还没开始点菜，请对我说出你想点的菜'