#Giavanna Esposito
#CS 100 - 006
#HW 04, February 15, 2016

# Problem 3.20

lst = ['January', 'February', 'March']
for month in lst:
    print(month[0:3])

# Problem 3.21

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
for i in range(2, 9, 2):
    print(i)

# Problem 3.22

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in x:
    if i**2%8 == 0:
        print(i)

# Problem 3.23

#a

for i in range(0, 2, 1):
    print(i, end = ' ')

#b

for i in range(0, 1):
    print(i, end = ' ')

#c

for i in range(3, 7):
    print(i, end = ' ')

#d

for i in range(1, 2):
    print(i, end = ' ')

#e

for i in range(0, 4, 3):
    print(i, end = ' ')

#f

for i in range(5, 22, 4):
    print(i, end = ' ')

# Practice Midterm 1 Multiple Choice 1 - 10

# Problem 1
# My answer: D
# Correct answer: D

# Problem 2
# My answer: A
# Correct answer: A

# Problem 3
# My answer: C
# Correct answer: C

# Problem 4
# My answer: B
# Correct answer: E
# Reason for the difference: I thought that for suffix, I would start at -1 and continue, but I needed to start adding on from 2.

# Problem 5
# My answer: A
# Correct answer: C
# Reason for difference: I forgot to include 0 as a value in the range.

# Problem 6
# My answer: B
# Correct answer: A
# Reason for difference: Initially, I did not understand the question, and thought that I had to add 1 to the element to see if it still was the same, which could not happen. It was actually asking if the next element in the list was the same as before, in which case 0 appeared twice, resulting in true, but after, there was a 1, meaning it would not be true again.

# Problem 7
# My answer: B
# Correct answer: E
# Reason for difference: Since veryCold = True, it prints "car won't start", and ends there.

# Problem 8
# My answer: D
# Correct answer: D

# Problem 9
# My answer: B
# Correct answer: B

# Problem 10
# My answer: A
# Correct answer: D
# Reason for difference: I failed to recognize that it would add each element separately to the list.



    
