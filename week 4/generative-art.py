import turtle


t = turtle.Turtle()

t.speed(0)
turtle.bgcolor("#023047")


#design1

colors1 = ["#ffb703", "#fb8500"]

for i in range(38): 
    t.color(colors1[i%2])     
    t.forward(100)
    t.right(30)
    t.forward(20)    
    t.left(60)
    t.forward(50)  
    t.right(30)
     
    t.penup()
    t.setposition(0, 0)
    t.pensize(5)
    t.pendown()    
    t.right(10)

    if i > 180:
        break 
    else:
        print (i)




#design2

colors2 = ["#8ecae6", "#219ebc"]

def drawCircle(radius):    
    for i in range(5):
        t.color(colors2[i%2])
        t.circle(radius)
        t.pensize(2)
        radius = radius- 4

def drawDesign():
    for i in range(10):
        t.color(colors2[i%2])
        drawCircle(120)
        t.right(36)

drawDesign()

#end the design ???

turtle.done()



















    











