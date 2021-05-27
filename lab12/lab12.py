##### 1.
print('#1.')

import abc

class IncorrectParameters(Exception):
    pass

class Integral(abc.ABC):

    def __init__(self, start, stop, steps, fun):
        if stop < start or steps < 1:
            raise IncorrectParameters
        self.start = start
        self.stop = stop
        self.steps = steps
        self.fun = fun

    @abc.abstractmethod
    def calculate(self):
        ''' '''

class TrapezoidIntegral(Integral):

    def calculate(self):
        h = (self.stop - self.start) / self.steps
        result = 0
        for i in range(1, self.steps):
            result += self.fun(self.start + i * h) + self.fun(self.start + (i + 1) * h)
        result *= (h / 2)
        return result

class SimpsonIntegral(Integral):

    def calculate(self):
        h = (self.stop - self.start) / (2 * self.steps)
        result = 0
        for i in range(1, 2 * self.steps):
            if i % 2:
                result += 4 * self.fun(i * h + self.start)
            else:
                result += 2 * self.fun(i * h + self.start)
        result += self.fun(self.start) + self.fun(self.stop)
        result *= (h / 3)
        return result

tIntegral = TrapezoidIntegral(0, 2, 2000, lambda x : x**3)
print(f'Calka z x^3 od 0 do 2 (2000 krokow) metoda trapezow: {tIntegral.calculate()}')

sIntegral = SimpsonIntegral(0, 2, 2000, lambda x : x**3)
print(f'Calka z x^3 od 0 do 2 (2000 krokow) metoda Simpsona: {sIntegral.calculate()}')
print('(Wynik analityczny = 4)')    

##### 2.
print('\n#2.')

import copy

class Stack:

    def __init__(self, other = None):
        if not other:
            self.data = []
        else:
            self.data = copy.deepcopy(other.data)

    def insert(self, element):
        self.data.insert(0, element)

    def pop(self):
        return self.data.pop(0)

    def addOtherStack(self, other):
        # elementy z other ida na gore stosu
        temp = other.data + self.data
        self.data = copy.deepcopy(temp)

    def print(self):
        for i in self.data:
            print(i)

    def size(self):
        return len(self.data)

class SortedStack(Stack):

    def __init__(self, ascending = True, other = None):
        super().__init__(other)
        self.isAscending = ascending
        if other:
            self.data.sort(not self.isAscending)

    def insert(self, element):
        if not self.data:
            self.data.insert(0, element)
        elif self.isAscending and self.data[0] < element:
            self.data.insert(0, element)
        elif not self.isAscending and self.data > element:
            self.data.insert(0, element)

    def addOtherStack(self, other):
        for i in other.data:
            self.insert(i)

import random


result = 0
for _ in range(100):
    s = SortedStack()
    for _ in range(100):
        s.insert(random.randint(0, 100))
    result += s.size()

result /= 100

print(f'Sredni rozmiar stosu: {result}')

##### 3.
print('\n#3.')

class Counter:

    def __init__(self, fileName):
        self.fileName = fileName
        self.lines = 0
        self.words = 0
        self.characters = 0

    def count(self):
        with open(self.fileName) as file:
            for line in file.readlines():
                self.lines += 1
                self.words += len(line.split())
                self.characters += len(line)
        print(f'{self.lines} {self.words} {self.characters} {self.fileName}')

    @staticmethod
    def wc(*fileNames):
        counters = []
        for fileName in fileNames:
            counters.insert(0, Counter(fileName))

        lines = 0
        words = 0
        characters = 0

        for counter in counters:
            counter.count()
            lines += counter.lines
            words += counter.words
            characters += counter.characters

        print(f'{lines} {words} {characters} razem')     

Counter.wc('AA.txt', 'BB.txt')
