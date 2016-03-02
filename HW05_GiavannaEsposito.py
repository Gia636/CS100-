# Giavanna Esposito
# CS 100 - 006
# HW 05, February 15, 2016

# Practice Problem 3.8

import math
def perimeter(radius):
    return 2 * math.pi * radius
    print(2 * math.pi * radius)
perimeter(2)

# Practice Problem 3.9

def average(value1, value2):
    print((value1 + value2) / 2)
average(3, 20)

# Practice Problem 3.10

def noVowel(string):
    for letter in string:
        if letter in 'AEIOUaeiou':
            return False
    return True
print(noVowel('vowel'))
print(noVowel('xzcvr'))

# Practice Problem 3.11

def allEven(numbers):
    for number in numbers:
        if number % 2 != 0:
            return False
    return True
print(allEven([2, 4, 6, 8]))
print(allEven([0, 1, 2, 3]))

# Practice Problem 3.12

def negative(numbers):
    for number in numbers:
        if number < 0:
            print(number)
negative([-1, 2, -3, 1, -4])

# Practice Problem 3.13

def negative(numbers):
    ' prints the negative numbers in the list '
    for number in numbers:
        if number < 0:
            print(number)
negative([-1, 2, -3, 1, -4])

def average(value1, value2):
    ' gives the average of two values ' 
    print((value1 + value2) / 2)
average(3, 20)

help(average)
help(negative)


# Problem 11

# a

import turtle
s = turtle.Screen()
t = turtle.Turtle()

def drawTick(t, tickLen):
    t.right(90)
    t.forward(tickLen)
    t.up()
    t.back(tickLen)

drawTick(t, 50)
s.bye()

# b

import turtle
s = turtle.Screen()
t = turtle.Turtle()

def drawTicks(t, tickLen, numTicks, distance):
    for i in range(numTicks):
        t.right(90)
        t.forward(tickLen)
        t.up()
        t.back(tickLen)
        t.left(90)
        t.forward(distance)
        t.down()

drawTicks(t, 50, 8, 20)
s.bye()

# Problem 12

List = ['this', 'is', 'the', 'list', 'of', 'strings']

def beginsWith(letter, strList):
    letterCount = 0
    for letter in strList:
        if letter in strList[0]:
            letterCount +=1
    print(letterCount)

beginsWith(t, List)
            
# Problem 13

def greeting(greetStr):
    name = input('What is your name?')
    day = input('What day of the week is today?')
    print(greetStr + day + name)
    if len(name) == len(day):
            print('Your name has the same number of characters as today!')
    if len(name) > len(day):
            print('Your name has more charcters than today.')
    if len(name) < len(day):
            print('Your name has less characters than today.')
                
greeting('Happy')
    
