import time
from tkinter import *
import socket
import pickle
import sqlite3
import select 
import random
from collections import defaultdict 
from collections import Counter 
import sys 
import datetime
import random

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port=1234
mysock.bind(('',port))
mysock.listen(5)

client1,add1 =mysock.accept()
client2,add2 =mysock.accept()
client3,add3 =mysock.accept()
client4,add4 =mysock.accept()
client5,add5 =mysock.accept()

# root = Tk()               
no_of_clients=[client1,client2,client3,client4,client5]



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



client_cards_copy=client_cards.copy()
n=len(no_of_clients)
client_name=[] #Name of all the players
for i in range(0,n):
    no_of_clients[i].send('Hello welcome!'.encode('utf-8'))
    
    # while 1:
    mess_recv=no_of_clients[i].recv(10).decode('utf-8')
    # if len(mess_recv)==0:
    #     break
    client_name.append(mess_recv)
    print(mess_recv," has joined")


for i in range(0,n):
    cards_total=yunhi+client_cards[i]
    cards_data=' '.join(cards_total)
    no_of_clients[i].send(cards_data.encode())



values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}


from collections import defaultdict 
from collections import Counter 
import sys 


# def check_flush(hand):
#     suits = [h[1] for h in hand]
#     if len(set(suits)) == 1:
#       return True
#     else:
#       return False

def check_hand(hand):
    if check_straight_flush(hand):
        return 9
    if check_four_of_a_kind(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_three_of_a_kind(hand):
        return 4
    if check_two_pairs(hand):
        return 3    
    if check_one_pairs(hand):
        return 2
    return 1


card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values: 
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values: 
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_flush(hand):
    # print("handwa :",hand)
    suits = [i[1] for i in hand]
    if len(set(suits))==1:
        return True
    else:
        return False

def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else: 
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False

def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False

def custom_straight(listA):
    sorted_list = sorted(listA)
    #sorted(l) ==
    range_list=list(range(min(listA), max(listA)+1))
    if sorted_list == range_list:
        return True
    else:
        return False
    

    
from itertools import combinations
from itertools import permutations 
hand_dict = {9:"royal-flush", 8:"four-of-a-kind", 7:"full-house", 6:"flush", 5:"straight", 4:"three-of-a-kind", 3:"two-pairs", 2:"one-pair", 1:"highest-card"}


def play(cards):
    hand = cards[:5]
    deck = cards[5:]
    best_hand = 0
    store=[]
    possible_combos = combinations(cards, 5)
    for i in possible_combos:
        permu=permutations(i)
        for j in permu:
            hand_value=check_hand(j)
            if hand_value>best_hand:
                best_hand=hand_value
                store=j
    return hand_dict[best_hand],store,best_hand


            

    permu=permutations(hand)
    for c in possible_combos: 
        current_hand = list(c) + deck[:i]
        hand_value = check_hand(current_hand)
        if hand_value > best_hand:
            best_hand = hand_value
                
    return hand_dict[best_hand]


# hand=["2C", "KD", "3D", "5D", "3S","3H", "4S"]
# print(check_three_of_a_kind(hand))

def winner(p1,p2):
    rank1,b1,rank_value1=play(p1)
    rank2,b2,rank_value2=play(p2)
    # print(play(p1))
    if (rank_value1>rank_value2):
        return p1,'0',rank1
    elif rank_value2>rank_value1:
        return p2,'0',rank2
    else:
        if rank_value1==1 :                              ##highest card
            values1 = [i[0] for i in p1]
            value_counts1 = [card_order_dict[i] for i in values1]  
            value_counts1.sort(reverse=True)
            value_counts1=value_counts1[:5]
            # print("shhh :",value_counts1)


            values2 = [i[0] for i in p2]
            value_counts2 = [card_order_dict[i] for i in values2] 
            value_counts2.sort(reverse=True)
            value_counts2=value_counts2[:5]
            # print("shhh :",value_counts2)

            for i in range(len(b1)-1,-1,-1):
                if value_counts1[i]>value_counts2[i]:
                    return p1,'0',rank1
                elif value_counts2[i]>value_counts1[i]:
                    return p2,'0',rank2

        elif rank_value1==8 or rank_value1==7 :
            values1 = [i[0] for i in b1]
            values1= Counter(values1)
            values1.most_common()
            values1=dict(values1)

            values2 = [i[0] for i in b2]
            values2= Counter(values2)
            values2.most_common()
            values2=dict(values2)

            p1index=values1.keys()
            p1index=list(p1index)

            p2index=values2.keys()
            p2index=list(p2index)

            if 4 in values1.values():                     ##check four of a kind
                if(card_order_dict[p1index[0]]>card_order_dict[p2index[0]]):
                    return p1,'0',rank1
                else:
                    return p2,'0',rank2
            if 3 in values1.values() and 2 in values1.values():   ##full house
                if(card_order_dict[p1index[0]]>card_order_dict[p2index[0]]):
                    return p1,'0',rank1
                elif card_order_dict[p1index[0]]<card_order_dict[p2index[0]]:
                    return p2,'0',rank2
                elif card_order_dict[p1index[1]]>card_order_dict[p2index[1]]:
                    return p1,'0',rank1
                elif card_order_dict[p1index[1]]<card_order_dict[p2index[1]]:
                    return p2,'0',rank2
                else:
                    return p1,p2,rank1
        elif  rank_value1==4 or rank_value1==2:                  ## three of a kind ya to one pair
            values1 = [i[0] for i in p1]
            values1= Counter(values1)
            values1.most_common()
            values1=dict(values1)
           
            values2 = [i[0] for i in p2]
            values2= Counter(values2)
            values2.most_common()
            values2=dict(values2)

            p1index=values1.keys()
            p1index=list(p1index)

            p2index=values2.keys()
            p2index=list(p2index)

            if card_order_dict[p1index[1]]>card_order_dict[p2index[1]]:
                return p1,'0',rank1

            elif card_order_dict[p1index[1]]<card_order_dict[p2index[1]]:
                return p2,'0',rank2
            else:
                p1index=p1index[1:]
                value_counts1 = [card_order_dict[i] for i in p1index]
                value_counts1.sort(reverse=True)
                value_counts1=value_counts1[:2] 

                p2index=p2index[1:]
                value_counts2 = [card_order_dict[i] for i in p2index]
                value_counts2.sort(reverse=True)
                value_counts2=value_counts2[:2] 
                
                # print("yhree me ",value_counts2)

                for i in range(0,len(value_counts1)):
                    if value_counts1[i]>value_counts2[i]:
                        return p1,'0',rank1
                    elif value_counts1[i]<value_counts2[i]:
                        return p2,'0',rank2
                return p1,p2,rank1
        elif rank_value1==3:                ##    two pair 
            values1 = [i[0] for i in p1]
            values1= Counter(values1)
            values1.most_common()
            values1=dict(values1)
           
            values2 = [i[0] for i in p2]
            values2= Counter(values2)
            values2.most_common()
            values2=dict(values2)

            p1index=values1.keys()
            p1index=list(p1index)

            p2index=values2.keys()
            p2index=list(p2index)

            store1=[card_order_dict[p1index[0]],card_order_dict[p1index[1]]]
            store1.sort(reverse=True)

            store2=[card_order_dict[p2index[0]],card_order_dict[p2index[1]]]
            store2.sort(reverse=True)

            for i in range(0,len(store1)):
                if store1[i]>store2[i]:
                    return p1,'0',rank1
                elif store1[i]>store2[i]:
                    return p2,'0',rank2
            
                p1index=p1index[2:]
                value_counts1 = [card_order_dict[i] for i in p1index]
                value_counts1.sort(reverse=True)
                value_counts1=value_counts1[:2] 

                p2index=p2index[2:]
                value_counts2 = [card_order_dict[i] for i in p2index]
                value_counts2.sort(reverse=True)
                value_counts2=value_counts2[:2] 
                
                # print("yhree me ",value_counts2)

                for i in range(0,len(value_counts1)):
                    if value_counts1[i]>value_counts2[i]:
                        return p1,'0',rank1
                    elif value_counts1[i]<value_counts2[i]:
                        return p2,'0',rank2
                return p1,p2,rank1

        elif rank_value1==5:                    ## straight
            values1 = [i[0] for i in p1]
            p1 = [card_order_dict[i] for i in values1]

            values2 = [i[0] for i in p2]
            p2 = [card_order_dict[i] for i in values2]

            p1.sort()
            p2.sort()
            
            # print(p1)
            for i in range(2,-1,-1):
                if(custom_straight(p1[i:i+5])):
                    values1=p1[i:i+5]
                    break
            
            for i in range(2,-1,-1):
                if(custom_straight(p2[i:i+5])):
                    values2=p2[i:i+5]
                    break
            print(values1,values2)
            if (sum(values1)>sum(values2)):
                return p1,'0',rank1
            elif (sum(values1)>sum(values2)):
                return p2,'0',rank2
            # else:
                return p1,p2,rank1
        
        elif rank_value1==6:                       ##flush
            p1index = [i[1] for i in p1]
            p1val=[i[0] for i in p1]
            p1 = [card_order_dict[i] for i in p1val]
            values1=Counter(p1index)
            values1=dict(values1)
            values1=list(values1.keys())
            store1=[]
            # print(p1index)
            for i in range(0,len(p1index)):
                if values1[0]==p1index[i]:
                    store1.append(p1[i])
            store1.sort(reverse=True)
            store1=store1[:5]

            p2index = [i[1] for i in p2]
            p2val=[i[0] for i in p2]
            p2 = [card_order_dict[i] for i in p2val]
            values2=Counter(p2index)
            values2=dict(values2)
            values2=list(values2.keys())
            store2=[]
            # print(p1index)
            for i in range(0,len(p2index)):
                if values2[0]==p2index[i]:
                    store2.append(p2[i])
            store2.sort(reverse=True)
            store2=store2[:5]

            # print(store1)

            for i in range(0,len(store1)):
                if store1[i]>store2[i]:
                    return p1,'0',rank1
                elif store1[i]<store2[i]:
                    return p2,'0',rank2
            return p1,p2,rank1

        elif rank_value1==9:                ##royal flush
            p1index = [i[1] for i in p1]
            p1val=[i[0] for i in p1]
            p1 = [card_order_dict[i] for i in p1val]
            values1=Counter(p1index)
            values1=dict(values1)
            values1=list(values1.keys())
            store1=[]
            # print(p1index)
            for i in range(0,len(p1index)):
                if values1[0]==p1index[i]:
                    store1.append(p1[i])
            store1.sort()
            

            p2index = [i[1] for i in p2]
            p2val=[i[0] for i in p2]
            p2 = [card_order_dict[i] for i in p2val]
            values2=Counter(p2index)
            values2=dict(values2)
            values2=list(values2.keys())
            store2=[]
            # print(p1index)
            for i in range(0,len(p2index)):
                if values2[0]==p2index[i]:
                    store2.append(p2[i])
            store2.sort()


            temp1=[]
            for i in range(0,len(store1)-4):
                if(custom_straight(store1[len(store1)-5:len(store1)])):
                    temp1=store1[len(store1)-5:len(store1)]

            temp2=[]
            for i in range(0,len(store2)-4):
                if(custom_straight(store2[len(store2)-5:len(store2)])):
                    temp2=store2[len(store2)-5:len(store2)]
            # print(temp1,temp2)

            if(sum(temp1)>sum(temp2)):
                return p1,'0',rank1
            elif(sum(temp1)<sum(temp2)):
                return p2,'0',rank2
            else:
                return p1,p2,rank1
                

yunhi=[x.upper() for x in yunhi]
all_cards=[]
for i in range(0,n):
    client_cards[i]=[x.upper() for x in client_cards[i]]
    # all_cards.append(yunhi+client_cards[i])
print(all_cards)               


# yunhi wale ko logic ke form me layaa
for i in range(0,5):
    if yunhi[i][1]=='1':
        yunhi[i]='J'+yunhi[i][2]
    elif yunhi[i][1]=='2':
        yunhi[i]='Q'+yunhi[i][2]
    elif yunhi[i][1]=='3':
        yunhi[i]='K'+yunhi[i][2]
    elif yunhi[i][1]=='0':
        yunhi[i]='T'+yunhi[i][2]
        
    elif yunhi[i][0]=='1' and len(yunhi[i])==2:
        yunhi[i]='A'+yunhi[i][1]

# Client cards ko logic wale form me laaya
for i in range(0,n):
    for j in range(0,2):

        if client_cards[i][j][1]=='1':
            client_cards[i][j]='J'+client_cards[i][j][2]
        elif client_cards[i][j][1]=='2':
            client_cards[i][j]='Q'+client_cards[i][j][2]
        elif client_cards[i][j][1]=='3':
            client_cards[i][j]='K'+client_cards[i][j][2]
        elif client_cards[i][j][1]=='0':
            client_cards[i][j]='T'+client_cards[i][j][2]
            
        elif client_cards[i][j][0]=='1' and len(client_cards[i][j])==2:
            client_cards[i][j]='A'+client_cards[i][j][1]

# yunhi and client ke cards ko sathme liya
for i in range(0,n):
    all_cards.append(yunhi+client_cards[i])


win=all_cards[0]
rank=''
win2=''


# sabko winner wale function me dalke 1v1 check
for i in range(0,n-1):

    win,win2,rank=winner(win,all_cards[i+1])

winner_cards_name=[]
index=0
final_winner=''


# Final winner milega fhir uska client name milega from client_name list and uske 2 cards record karenge
for i in range(0,n):
    if all_cards[i]==win:
        final_winner=client_name[i]
        index=i
        winner_cards_name=client_cards_copy[index]
    

print('Winner: ',final_winner)


# client cards,name,rank sabko ekh list me daal diya
winner_cards_name.append(final_winner)
winner_cards_name.append(rank)
print(winner_cards_name)


#  DATABASE

print('-----------------------------------DATABASE---------------------------------')
conn = sqlite3.connect('poker.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE winner (name text, win_type text,date text,time text)''')

# Insert a row of data
# c.execute("Drop table winner")

# Date and Time record karenge
x = datetime.datetime.now()
date=x.strftime("%x")
time=x.strftime("%X")
c.execute(f"INSERT INTO winner VALUES ('{final_winner}','{rank}','{date}','{time}')" )

sqlite_select_query = """SELECT * from winner"""
c.execute(sqlite_select_query)

records=c.fetchall()
print("\nTotal rows are: ", len(records))
print()
# Pura database print karega
for rows in records:
    print('Name:',rows[0],'\t Win by: ',rows[1],'\t\tDate: ',rows[2],'\tTime: ',rows[3])
conn.commit()
conn.close()
print()

# sab clients ko winner ka cards,name,rank send karenge
for i in range(0,n):
    cards_data=' '.join(winner_cards_name)
    no_of_clients[i].send(cards_data.encode())




