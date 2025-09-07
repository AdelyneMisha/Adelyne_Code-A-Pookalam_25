import turtle as t

# screen

wn = t.Screen()
wn.bgcolor("white")
wn.title("Pookalam Design")
wn.setup(width=750, height=750)

#attributes

speed = 0
size = 3
colours = ["#F7EE7F","#F1A66A", "#F26157","#DA4167","#8A1C7C","#F0BCD4","#899D78","#436436","#1F0322", "#582630"] 


# main outer circle

t.speed(speed)
t.pensize(size) 
t.color(colours[-2])
t.begin_fill()
t.goto(0,-280)
t.circle(280)
t.end_fill()
t.penup()
t.hideturtle()


##lotus
pink=["#fb6f92","#ff8fab","#ffb3c6","#ffc2d1"]
lo=t.Turtle()
lo.speed(speed)
lo.penup()
lo.goto(0,250)

for z in range(40):
    lo.penup()
    lo.circle(-250,360/40)
    lo.pendown()
    lo.left(130)  #140
    for i in range(6):
        for j in range(3):
            lo.color(pink[j])
            lo.begin_fill()
            lo.circle(20-j*5,60)
            lo.left(120)
            lo.circle(20-j*5,60)
            lo.end_fill()
            lo.left(120)
        lo.right(27)
    lo.left(32)  #49
lo.hideturtle()
lo.penup()
lo.home()

# green circle border

lo.goto(0,-235)
lo.color("#0B6E4F")
lo.pensize(10)
lo.pendown()
lo.circle(235)


## yellow ring

t.color(colours[0])
t.begin_fill()
t.goto(0,-220)
t.circle(220)
t.end_fill()
t.penup()
t.hideturtle()


##leafs
colours1=["#6BBF59","#08A045","#0B6E4F","#073B3A"]

z=t.Turtle()
z.speed(speed)
z.shape("circle")
z.penup()
z.hideturtle()
z.goto(0,-150)
z.circle(150,360/16)
for i in range(8):
    z.circle(150,360/8)
    z.shape("arrow")
    z.shapesize(2,5)
    z.color(colours1[-1])
    z.right(90)
    z.forward(5)
    z.stamp()
    z.backward(5)
    z.left(90)
    z.shape("circle")

    for j in range(4):
        z.color(colours1[3-j])
        z.shapesize(4-j,2-j*0.5)
        z.stamp()


#ring petals

q=t.Turtle()
q.hideturtle()
q.speed(speed)  
for i in range(1):
    q.penup()
    q.goto(0,-100)
    q.pendown()
    q.shapesize(9,6)
    q.shape("circle")
    q.color(colours[-2])
    for _ in range(8):
        q.penup()
        q.circle(100,360/8)
        q.pendown()
        q.stamp()

#outer ring corners

c = t.Turtle()

c.penup()
c.color(colours[-2])
c.goto(0,200)
c.shapesize(9,4.5)
c.speed(speed)
c.hideturtle()
for k in range(8):
    c.left(90)
    c.stamp()
    c.right(90)
    c.circle(-200,360/8)

for i in range(5):
    q.penup()
    q.goto(0,-100)
    q.pendown()
    q.shapesize(7-i,6)
    q.shape("circle")
    q.color(colours[4-i])
    for _ in range(8):
        q.penup()
        q.circle(100,360/8)
        q.pendown()
        q.stamp()


#circle border ring

t.penup()
t.goto(0,-120)
t.pendown()
t.pensize(5)
t.color(colours[-2])
t.begin_fill() 
t.circle(120)
t.end_fill() 

t.penup()
t.goto(0,-100)
t.pendown()
t.shapesize(2,1)
t.shape("circle")
t.color("white")
for _ in range(36):
    t.penup()
    t.circle(100,10)
    t.pendown()
    t.stamp()


#inner circle for 16 
t.home()
t.goto(0,-105)
t.color(colours[-3])
t.pendown()
t.begin_fill()
t.circle(105)
t.end_fill()

pens=[]
# Create 16 pens for petals
l=0
for _ in range(16):
    pen = t.Turtle()
    pen.color(colours[0])
    pen.speed(speed)
    pen.pensize(size)
    pens.append(pen)
    pen.right(22.5*l)  # Initial rotation for better alignment
    l+=1

for i in range(5):
    for pen in pens:
        pen.pensize(2)
        pen.color(colours[i])
        pen.begin_fill()
        pen.circle(100-i*10,60)
        pen.left(120)
        pen.circle(100-i*10,60)
        pen.end_fill()
        pen.hideturtle()
t.penup()
t.goto(0,-35)
t.pendown()
t.color(colours[0])
t.begin_fill()
t.circle(35)
t.end_fill()
t.penup()

t.done()