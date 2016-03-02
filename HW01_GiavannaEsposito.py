#Giavanna Esposito
#CS 100 - 006
#HW 01, February 1, 2016

# Problem 2.18
#a
flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']
#b
flowers.append('potato')
print('potato' in flowers)
#c
thorny = [flowers[0:3]]
#d
poisonous = [flowers[5]]
#e
dangerous = thorny + poisonous

# Problem 2.19
answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
#a
numYes = answers.count('Y')
#b
numNo = answers.count('N')
#c
percentYes = (numYes / (numYes + numNo)) * 100
#d
answers.sort()
#e
f = answers.index('Y')

# Problem 2.21
s = 'Esposito'
t = 'Giavanna'
print(t[0] + s[0])

# Problem 3
grades = ['A', 'A', 'B', 'B', 'D', 'C', 'B', 'F']
A = grades.count('A')
B = grades.count('B')
C = grades.count('C')
D = grades.count('D')
F = grades.count('F')
frequency = [A, B, C, D, F]
print(frequency)



