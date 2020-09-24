# Putting a gif image on a canvas with Tkinter
# tested with Python24 by  vegaseat  25jun2005
import time
from tkinter import *
import socket
import pickle
import threading 
import os




# import tkinter as tk 
# import Tkinter

# root1 = Tk()               
  
# root1.geometry('1000x400') 

# name=StringVar()
# frame=LabelFrame(root1,text="Holaaa",padx=50,pady=50)
# frame.pack(padx=20,pady=20)
# name=StringVar()

# name_label = Label(root1, text = 'Enter your Name: ') 

# name_entry = Entry(root1,width=40,borderwidth=5) 
# name_label.grid(row=0,column=0) 
# name_entry.grid(row=0,column=1)

# name=name_entry.get()
# print(name)


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port=1234
mysock.connect((host,port))
print('Connected to the server')

message=mysock.recv(1024).decode('utf-8')
print('Server message: ',message)

root = Tk()               

root.geometry('700x400') 
root.title('Client 3')    
# create the canvas, size in pixels
canvas = Canvas(width = 300, height = 200, bg = 'yellow')
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
flag=0
def submit():
    # root1.destroy()
   
    print("Enter your name")
    

    new_message=input(str('>>'))
    
    new_m=new_message.encode()
    mysock.send(new_m)

    
    # load the .gif image file
    # put in your own gif file here, may need to add full path
    # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
    arr=[]
    arr_client=[]
    rec=mysock.recv(100).decode()
    yunhi=rec.split(' ')
    print(yunhi)
    # yunhi=['10h','1h','10s','2s','11h']
    # cards=mysock.recv(100).decode()

    
    client_cards=[yunhi.pop(),yunhi.pop()]
    print(client_cards)
    print(yunhi)
    # gif1 = PhotoImage(file = 'DECK//10h.
    # gif')
    # gif2 = PhotoImage(file = 'DECK//1h.gif')

    # gif3 = PhotoImage(file = 'DECK//10s.gif')
    # gif4 = PhotoImage(file = 'DECK//2s.gif')

    gifclose=PhotoImage(file = 'DECK//b.gif')
    # arr.append(gif1)
    # arr.append(gif2)
    # arr.append(gif3)
    # arr.append(gif4)
    for i in range(0,len(yunhi)):
        string='DECK//'+yunhi[i]+'.gif'
        arr.append(PhotoImage(file =string))

    for i in range(0,2):
        string='DECK//'+client_cards[i]+'.gif'
        arr_client.append(PhotoImage(file =string))

    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    # canvas.create_image(50, 10, image = gif1, anchor = NW)
    # canvas.create_image(100, 10, image = gif2, anchor = NW)

    # canvas.create_image(50, 200, image = gif4, anchor = NW)
    # canvas.create_image(100, 200, image = gif3, anchor = NW)
    # run it ...
    
    store=[]
    store_client=[]
    store_winner=[]

    for i in range(0,5):
        store.append(gifclose)

    for i in range(0,2):
        store_client.append(gifclose)
        store_winner.append(gifclose)

    if flag==0:
        for i in range(0,len(arr)):
            canvas.create_image(100*(i+1), 10, image = gifclose, anchor = NW)

        for i in range(0,2):
            canvas.create_image(100*(i+1), 200, image = gifclose, anchor = NW)
            canvas.create_image(350*((0.25*i)+1), 200, image = gifclose, anchor = NW)

    def winner_card(win):
        arr_winner=[]
        for i in range(0,2):
            string='DECK//'+win[i]+'.gif'
            arr_winner.append(PhotoImage(file =string))
        for i in range(0,2):
            store_winner.pop(i)
            store_winner.insert(i,arr_winner[i])
        for i in range(0,2):
            canvas.create_image(350*((0.25*i)+1), 200, image = store_winner[i], anchor = NW)

    def winner():
        winner=mysock.recv(100).decode()
        winn=winner.split(' ')
        print(winn)
        if winn[2]==new_message:
            Label(root, text = f'You are the WINNER! Congrats.', font=('calibre', 10, 'bold')).pack()
            import win
        else:
            Label(root, text = f'Winner name:  {winn[2]} \t Won by: {winn[3]}', font=('calibre', 10, 'bold')).pack()
            winner_card(winn)

    def open(x,y):
        
        length=len(store)
        if x==4:
            # flag=1
            Button(root, text = 'Find Winner', bd = '5', command = winner).pack()
        # print(store)
        # store.append(arr[len(store)])
        for i in range(x,y):
            store.pop(i)
            store.insert(i,arr[i])
        for i in range(x,y):
            canvas.create_image(100*(i+1), 10, image = store[i], anchor = NW)


    def start_game():

        for i in range(0,2):
            store_client.pop(i)
            store_client.insert(i,arr_client[i])
        for i in range(0,2):
            canvas.create_image(100*(i+1), 200, image = store_client[i], anchor = NW)

    
    Label(root, text = f'NAME: {new_message}', font=('calibre', 10, 'bold')).pack() 
    play = Button(root, text = 'Start game', bd = '5', command = start_game)
    play.pack()
    round1 = Button(root, text = 'Round 1 !', bd = '5', command = lambda: open(0,3))
    round2 = Button(root, text = 'Round 2 !', bd = '5', command = lambda: open(3,4))
    round3 = Button(root, text = 'Round 3 !', bd = '5', command = lambda: open(4,5))  
    
    round1.pack()
    round2.pack()
    round3.pack()
    

submit()


# root.wait_variable(1000)
# Button(root1,text = 'Submit', command = submit).grid(row=1,column=1)
# while 1:
#     if flag==1:
#         mysock.send('Game over'.encode())
#     else:
#         mysock.send('Wait'.encode())


root.mainloop()
