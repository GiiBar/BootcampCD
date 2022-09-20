from itertools import count


for i in range (151):
    print(i)

for x in range (5, 1001, 5):
    print(x)

for contar in range (101):
    if contar%10 == 0:
        print('Coding Dojo')
    elif contar%5 == 0:
        print('Coding')
    else:
        print(contar)

for contar in range (500000):
    if contar%3 == 0:
        print(contar)

for contar in range(2018, 0, -4):
    print(contar)

lowNum = 2
highNum = 9
mult = 3
for contar in range(lowNum, highNum+1):
    if contar % 3==0:
        print(contar)