##### 1.
print('#1.')

# dla obu przypadkow a1 = 0, r = 2

# an = a1 + (n - 1)r
class ArithmeticSequence1:
    def __init__(self, min, max, difference):
        self.min = min
        self.difference = difference
        self.currentIndex = 1
        self.currentValue = min
        self.max = max

    def __next__(self):
        self.currentIndex += 1
        self.currentValue = self.min + (self.currentIndex - 1) * self.difference
        if self.currentValue < self.max:
            return self.currentValue
        raise StopIteration
    
    def __iter__(self):
        return self

# an = an-1 + r
class ArithmeticSequence2:
    def __init__(self, min, max, difference):
        self.min = min
        self.difference = difference
        self.max = max

    def __next__(self):
        self.min += self.difference
        if self.min < self.max:
            return self.min
        raise StopIteration
    
    def __iter__(self):
        return ArithmeticSequence2(self.min, self.max, self.difference)

seq = ArithmeticSequence1(0, 10, 2)
for i in seq:
    for j in seq:
        print(f'({i},{j})', end = ' ')
    print()
print()

seq = ArithmeticSequence2(0, 10, 2)
for i in seq:
    for j in seq:
        print(f'({i},{j})', end = ' ')
    print()
print()

##### 2.
print('\n#2.')

class RandomIterator:
    def __init__(self, min, a, c, m):
        self.current = min
        self.a = a
        self.c = c
        self.m = m

    def __next__(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

    def __iter__(self):
        return self

import math
f = lambda x : math.sin(x)

# liczymy calke z sinusa od 0 do pi (= 2)
# prostokat: 0 <= x <= pi
#            0 <= y <= 1
t, iteration, result, expectedResult, rectangleArea = 0, 0, 0, 2, math.pi
randomIterator = iter(RandomIterator(1, 44485709377909, 0, 2**48))
while abs(expectedResult - result) > 10**-7:
    iteration += 1
    x = next(randomIterator) / 2**48 * math.pi
    y = next(randomIterator) / 2**48 * 1.0
    if 0 < y <= f(x):
        t += 1
    elif f(x) <= y < 0:
        t -= 1
    result = rectangleArea * t / iteration

print(f'calka obliczona numerycznie = {result}, wynik analityczny = {expectedResult}')
print(f'Potrzebbne bylo {iteration} iteracji aby obliczyc calke\n')


##### 3.
print('\n#3.')

import scipy.misc

class NewtonRaphsonIterator:
    def __init__(self, min, eps, fun):
        self.x = min
        self.eps = eps
        self.fun = fun

    def __next__(self):
        self.x = self.x - self.fun(self.x) / scipy.misc.derivative(self.fun, self.x)
        if abs(self.fun(self.x)) < abs(self.eps):
            raise StopIteration
        return self.x

    def __iter__(self):
        return self

f = lambda x: math.sin(x) - (0.5 * x)**2
for i in NewtonRaphsonIterator(1.5, 10**-5, f):
    print(f'x = {i}, f(x) = {f(i)}');


