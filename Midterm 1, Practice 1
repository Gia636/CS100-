#1
#D

#2
#D

#3
#B

#4
#A

#5
#A

#6
#E

#7
#A

#8
#C

#9
#D

#10
#B

#11

import turtle
s = turtle.Screen()
t = turtle.Turtle()

def parallelLines(t, numLines, lineLength):
    for i in range(numLines):
        t.down()
        t.forward(lineLength)
        t.up()
        t.back(lineLength)
        t.left(90)
        t.forward(25)
        t.right(90)
parallelLines(t, 4, 50)

#12

def containsLetter(aLetter, strList):
    lst = []
    for words in strList:
        if aLetter in words:
            lst.append(words)
    return lst
fruits = ['apple', 'banana', 'orange', 'strawberry']
print(containsLetter('e', fruits))
print(containsLetter('f', fruits))
print(containsLetter('r', fruits))

#13

line1 = 'Please give a number no less than'
line2 = 'and no greater than'
def getInt(minInt, maxInt):
    number = input(line1 + ' ' + minInt + ' ' + line2 + ' '+ maxInt )
    print(int(number))
    return number
getInt('3', '7')

number = getInt('-2', '7')
if int(number) > 0:
    print('This number is positive')
if int(number) == 0:
    print('This number is 0')
if int(number) < 0:
    print('This number is negative')
   

    
   


            
    
    
