from random import randint
import time,sys

class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber
        self.warriors = {}

class Warrior:

    def __init__(self, strength):
        self.strength = strength

    def healing(self, stoneCount):

        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        if self.strength > self.maxStrength:
            self.strength = self.maxStrength

class Archer(Warrior):

    typeName = '射手'

    price = 100

    maxStrength = 100

    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！!!!!!!')

class Axeman(Warrior):

    typeName = '斧头兵'

    price = 120

    maxStrength = 120

    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型妖怪！！！!!!!!!!')

class Eagle():
    typeName = '鹰妖'

class Wolf():
    typeName = '狼妖'

class Forest():
    def __init__(self,monster):

        self.monster = monster

print('''****           游戏开始             ****''')

forest_num = 7

forestList = []

for i in range(forest_num):
    typeName=randint(0,1)
    if typeName==0:
        forestList.append(Forest(Eagle()))
    else:
        forestList.append(Forest(Wolf()))

    print('第', i+1,'座森林，里面是',forestList[i].monster.typeName)
time.sleep(10)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
stoneNumber=1000

Archer_num=int(input('射手数量：'))
Axemen_num=int(input('斧头兵数量：'))
stoneNumber -= (Archer_num+Axemen_num)*100
print('zenglingkang',stoneNumber)
warrior_name = input('为战士命名：')
warriors_list = list(warrior_name)
print('命名完成，3秒后游戏开始，进入第一座森林')
time.sleep(3)

print('*****1*****')
r1=input('第一场战士：')
for i in warriors_list[:Archer_num-1]:
    if i == r1:
        r1=Archer()
        r1.strength=100
        g1 = forestList[0].monster
        r1.fightWithMonster(g1)
        print(r1.strength)
    else:
        r1=Axemen()
        r1.strength=100
        r1.fightWithMonster(forestList[0].monster)
        print(r1.strength)
print('over')
healing1=int(input('1_bc:'))
r1.healing(healing1)
stoneNumber-=healing1
print('zenglingkang:',stoneNumber,'hp:',r1.strength)
#######
print('******************************************')
for i in range(2,8):
    r2 = input('战士：')
    if r1==r2:
        r2=r1()
        r2.fightWithMonster(forestList[i-1].monster)
        print(r2.strength)
    else:   
        for i in warriors_list[:Archer_num-1]:

            if i == r2:
                r2= Archer()
                r2.strength = 100
                r2.fightWithMonster(forestList[i-1].monster)
                print(r2.strength)
            else:
                r2 = Axemen()
                r2.strength = 100
                r2.fightWithMonster(forestList[i-1].monster)
                print(r2.strength)
    print('over')
    if r2.if_vic:
        print('战斗胜利！！！！✌')
    else:
        print('战斗失败，游戏结束。')
        break
    healing2 = int(input('对该战士的补给值:'))
    r2.healing(healing2)
    stoneNumber -= healing2
    print('灵石余额:', stoneNumber, '生命值:', r2.strength)
