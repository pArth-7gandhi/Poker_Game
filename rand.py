from collections import defaultdict 
from collections import Counter 
import sys 
import random



def player_card_generator(deck,list_cards):
    p=[]
    # print("player card generator me aaya")
    while len(p)!=2:
        flag=0
        temp=random.randint(1,52)
        if temp not in deck and temp not in p:
            for i in range(0,len(list_cards)):
                if temp in list_cards[i]:
                    flag=1
            if flag==0:
                p.append(temp)          
    return p


   


def deck_generator():
    duck=[]
    while len(duck)!=5:
        temp=random.randint(1,52)
        if(temp not in duck):
            duck.append(temp)

    return duck


def converter(p):
    
    p_ex=[]
    for i in range(0,len(p)):
        store=""
        flag=0
        if int(p[i]/13==1):
            if p[i]%13==0:
                p_ex.append('13s')
                flag=1
        elif int(p[i]/13==2):
            if p[i]%13==0:
                p_ex.append('13d')
                flag=1
        elif int(p[i]/13==3):
            if p[i]%13==0:
                p_ex.append('13c')
                flag=1
        elif int(p[i]/13==4):
            if p[i]%13==0:
                p_ex.append('13h')
                flag=1
        if flag==0:
            if int(p[i]/13)==0:                       ##spade
                if p[i]%13==11:
                    store='11'
                elif p[i]%13==12:
                    store='12'
                elif p[i]%13!=0:
                    store=str(p[i]%13)
                p_ex.append(store+'s')

            elif int(p[i]/13)==1:                     ##diamonds
                if p[i]%13==11:
                    store='11'
                elif p[i]%13==12:
                    store='12'
                elif p[i]%13!=0:
                    store=str(p[i]%13)
                p_ex.append(store+'d')
                
            elif int(p[i]/13)==2:                     ##clown
                if p[i]%13==11:
                    store='11'
                elif p[i]%13==12:
                    store='12'
                elif p[i]%13!=0:
                    store=str(p[i]%13)
                p_ex.append(store+'c')

            elif int(p[i]/13)==3:                     ## hearts
                if p[i]%13==11:
                    store='11'
                elif p[i]%13==12:
                    store='12'
                elif p[i]%13!=0:
                    store=str(p[i]%13)
                p_ex.append(store+'h')
    
    return p_ex


list_cards=[]
client_cards=[]
deck=deck_generator()
yunhi=converter(deck)
print(yunhi)
for i in range(0,5):
    p=player_card_generator(deck,list_cards)
    list_cards.append(p)
    p_ex=converter(p)
    client_cards.append(p_ex)
    # print(p_ex)

print(client_cards)