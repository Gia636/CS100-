#Giavanna Esposito
#CS 100 - 006
#HW 03, February 04, 2016

# Problem 1

# i.

a = 3
b = 4
c = 5

# ii.

if a < b:
    print('OK')

# iii.

if c < b:
    print('OK')

# iv.

if a + b == c:
    print('OK')

# v.

if a**2 + b**2 == c**2:
    print('OK')

# Problem 2

# i.

a = 3
b = 4
c = 5

# ii.

if a < b:
    print('OK')
else:
    print('NOT OK')

# iii.

if c < b:
    print('OK')
else:
    print('NOT OK')

# iv.

if a + b == c:
    print('OK')
else:
    print('NOT OK')

# v.

if a**2 + b**2 == c**2:
    print('OK')
else:
    print('NOI OK')

# Problem 3

import turtle
s = turtle.Screen()
t = turtle.Turtle()

color = input('What color?')
width = int(input('What line width?'))
length = int(input('What line length?'))
shape = input('Line, triangle, or square?')

t.width(width)


def line():
    t.color(color)
    t.forward(length)

def triangle():
    t.color(color)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)

def square():
    t.color(color)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)

if shape == ('line'):
    line()

if shape == ('triangle'):
    triangle()

if shape == ('square'):
    square()

