#1.
print('#1.')
import time
import sys
powt = 1000
N = 10000

def tester(fun):
    timeElapsed = time.time_ns()
    for i in range(powt):
        fun()
    timeElapsed = time.time_ns() - timeElapsed
    return timeElapsed


def forStatement():
    list = []
    for i in range(N):
        list.append(i)
    return list

def listComprehension():
    return [i for i in range(N)]

def mapFunction():
    return list(map(lambda x: x, range(N)))

def generatorExpression():
    return list((i for i in range(N)))

# print(sys.version)
# test = (forStatement, listComprehension, mapFunction, generatorExpression)
#
# for testFunction in test:
#     print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

'''
3.8.9 (default, Apr  3 2021, 01:00:00) 
[GCC 7.5.0]

dodawanie elementu
forStatement         => 5618451794
listComprehension    => 1831733013
mapFunction          => 1403670
generatorExpression  => 1566715

dodawanie elementu podniesionego do kwadratu
forStatement         => 9420837795
listComprehension    => 8386960834
mapFunction          => 1092446
generatorExpression  => 1200473

sumowanie elementow z wykorzystaniem petli for
forStatement         => 4665626526
listComprehension    => 2948165431
mapFunction          => 4091402885
generatorExpression  => 3298696581

sumowanie z wykorzystaniem funkcji sum
forStatement         => 3622220976
listComprehension    => 1862848668
mapFunction          => 2901818234
generatorExpression  => 2037490453

konwersja obiektu map i generatora do listy
forStatement         => 3415048710
listComprehension    => 1632180648
mapFunction          => 3419128037
generatorExpression  => 2261568843
'''

#2.
import random
print('\n#2.')
listA, listB = [random.randrange(0,20) for _ in range(100)], [random.randrange(0,20) for _ in range(100)]
result = zip(listA, listB)
result = list(filter(lambda x: x[0] + x[1] <= 15 and x[0] + x[1] >= 3, result))
print(result)

#3. 
import math
print('\n#3.')
def fun3(xValues, yValues):
    n = len(xValues)
    xMean = sum(xValues) / n
    D = sum(map(lambda x: (x - xMean)**2, xValues))
    a = sum(map(lambda x, y: y * (x - xMean), xValues, yValues)) / D
    yMean = sum(yValues) / n
    b = yMean - a * xMean
    dy = math.sqrt(sum(map(lambda x, y: (y - (a * x + b))**2, xValues, yValues)) / (n - 2))
    da = dy / math.sqrt(D)
    db = dy * math.sqrt(1 / n + xMean**2 / D)
    return f'y = {a}x + {b}, da = {da}, db = {db}'

print(fun3([0, 1, 2, 3, 4, 5], [10, 8, 7 , 4, 2]))

#4. 
print('\n#4.')
def myreduce(fun, seq):
    result = None
    for i in seq:
        if (result == None):
            result = i
        else:
            result = fun(i, result)
    return result

print('1 + 2 + 3 = ', myreduce(lambda x, y: x + y, [1, 2, 3]))
print('1 * 2 * 3 = ', myreduce(lambda x, y: x * y, [1, 2, 3]))


#5
print('\n#5.')
listC = [[0, 0], [1, -1], [2, -2], [3, 7], [8, 12]]
print(listC)
listCY, listCX = myreduce(lambda x, y: (list(x), list(y)), (map(lambda x: x[0], listC), map(lambda x: x[1], listC)))
print(listCX)
print(listCY)
