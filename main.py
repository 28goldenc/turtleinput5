import turtle
import random

screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("black")

t=turtle.Turtle()

t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("Background Color",font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor("tan")
t.write("1. Tan",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor("azure")
t.write("2. Azure",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor("aquamarine")
t.write("3. Aqua Marine",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor("darkkhaki")
t.write("4. Dark Khaki",font=("Arial",20,"bold italic"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write("Choose a Color",font=("Arial",30,"bold italic"),align="center")

choose=int(input("Choose a number: "))
if choose==1:
    screen.bgcolor("tan")
elif choose==2:
    screen.bgcolor("azure")
elif choose==3:
    screen.bgcolor("aquamarine")
else:
    screen.bgcolor("darkkhaki")

t.clear()

t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("black")
t.write("Enter your name:",font=("Arial",30,"bold italic"),align="center")

name=input("Enter a name: ")
# num1=int(input("Enter a number: "))
# num2=int(input("Enter another number: "))
operation=random.randint(1,4)
operation=4
if operation==1:
    symbol="+"
    num1=random.randint(-100,100)
    num2=random.randint(-100,100)
    solution=num1+num2
elif operation==2:
    symbol="-"
    num1=random.randint(-100,100)
    num2=random.randint(-100,100)
    solution=num1-num2
elif operation==3:
    symbol="*"
    num1=random.randint(-10,10)
    num2 = random.randint(1, 10)
    sign = random.randint(1, 2)
    if sign==2:
        num2=-1 * num2
    solution=num1*num2
elif operation==4:
    symbol="/"
    num1=random.randint(-10,10)
    num2 = random.randint(1, 10)
    sign = random.randint(1, 2)
    if sign==2:
        num2=-1 * num2
    solution=num1/num2



t.penup()
t.goto(0,150)
t.pendown()
t.pencolor("blue")
t.write(name,font=("Arial",28,"bold italic"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("red")
t.write(num1,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("green")
t.write(num2,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("black")
t.write(symbol,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("brown")
t.write("=",font=("Arial",30,"bold italic"),align="center")

answer=float(input("Enter the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("purple")
t.write(solution,font=("Arial",30,"bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("black")
t.write("Your answer: " + str(answer),font=("Arial",30,"bold italic"),align="center")

if solution==answer:
    screen.bgcolor("dodgerblue")
else:
    screen.bgcolor("darkorange")

if solution==answer:
    t.penup()
    t.goto(0, 75)
    t.pendown()
    t.pencolor("black")
    t.write("Correct!", font=("Arial", 28, "bold italic"), align="center")
else:
    t.penup()
    t.goto(0, 75)
    t.pendown()
    t.pencolor("black")
    t.write("Incorrect", font=("Arial", 28, "bold italic"), align="center")

t.hideturtle()
turtle.done()