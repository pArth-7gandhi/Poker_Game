import turtle
screen = turtle.Screen()
screen.setup(450,450)
screen.title('Lost')
screen.bgcolor('Green')
t1 = turtle.Turtle()
t1.ht()
t1.up()
t1.goto(-200,0)
t1.write('You Lost,Better Luck Next Time', font=("Arial", 20, "normal"))

turtle.mainloop()