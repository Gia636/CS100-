import turtle
s = turtle.Screen()
t = turtle.Turtle()
def equalSign(t, length):
    t.down()
    t.forward(length)
    t.up()
    t.back(length)
    t.left(90)
    t.forward(length/2)
    t.right(90)
    t.down()
    t.forward(length)
    t.up()
    t.back(length)
    t.right(90)
    t.forward(length/2)
    t.left(90)
        
equalSign(t, 100)

def equalSigns(t, length, spacing, number):
    for i in range(number):
        equalSign(t, length)
        t.forward(length+spacing)
equalSigns(t, 50, 25, 4)
        
    
