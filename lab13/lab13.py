#1
print('#1')

class Point2D:

    def __init__(self):
        self.x = 0
        self.y = 0
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.getter
    def x(self):
        return self._x 

    @property
    def y(self):
        return self._x

    @y.setter
    def y(self, value):
        self._y = value

    @y.getter
    def y(self):
        return self._y 

P1 = Point2D()
P1.x, P1.y = 12, 13
print(f'P1 = ({P1.x},{P1.y})')

#2
print('\n#2')

class OutOfRangeException(Exception):
    pass

min_range = -100
max_range = 100

def checkRange(min_range, max_range):
    def dec(fun):
        def decPoints(p1, p2, op):
            if max(p1.x, p2.x, p1.y, p2.y) > max_range or min(p1.x, p2.x, p1.y, p2.y) < min_range:
                raise OutOfRangeException 
            return fun(p1, p2, op)
        return decPoints
    return dec

@checkRange(min_range, max_range)
def calculate(p1, p2, operation):
    if (operation == 'add'):
        result = Point2D()
        result.x = p1.x + p2.x
        result.y = p1.y + p2.y
        return result
    elif (operation == 'substract'):
        result = Point2D()
        result.x = p1.x - p2.x
        result.y = p1.y - p2.y
        return result
    else:
        print('unknown operation')
        return None

P2 = Point2D()
P2.x, P2.y = 7, 10
P3 = calculate(P1, P2, 'add')
print(f'P3 = ({P3.x},{P3.y})')
P3 = calculate(P1, P2, 'substract')
print(f'P3 = ({P3.x},{P3.y})')

#3
print('\n#3')
import math
class Calculator2D:

    @staticmethod
    def section(p1, p2):
        return math.sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 )

    @staticmethod
    def perimeter(A, B, C, D = None):
        a = Calculator2D.section(A, B)
        b = Calculator2D.section(B, C)
        if (D):
            c = Calculator2D.section(C, D)
            d = Calculator2D.section(D, A)
            return a + b + c + d 
        else:
            c = Calculator2D.section(C, A)
            return a + b + c

    @staticmethod
    def surface_area(A, B, C, D = None):
        a = Calculator2D.section(A, B)
        b = Calculator2D.section(B, C)
        if(D):
            c = Calculator2D.section(C, D)
            d = Calculator2D.section(D, A)
            p = (a + b + c + d) / 2
            return math.sqrt((p - a) * (p - b) * (p - c) * (p - d))
        else:
            c = Calculator2D.section(C, A)
            p = (a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))

A = Point2D()
B = Point2D()
C = Point2D()
D = Point2D()
A.x, A.y = -2, -2
B.x, B.y = 2, -2
C.x, C.y = 2, 2
D.x, D.y = -2, 2

print(f'Obwod kwadratu: {Calculator2D.perimeter(A, B, C, D)}, pole: {Calculator2D.surface_area(A, B, C, D)}')
print(f'Obwod trojkata: {Calculator2D.perimeter(A, B, C)}, pole: {Calculator2D.surface_area(A, B, C)}')

#4
print('\n#4')

class CallCounter:
    calls = {}

    def __init__(self, f):
        self.f = f
        CallCounter.calls[f.__name__] = 0

    def __call__(self):
        CallCounter.calls[self.f.__name__] += 1

    @staticmethod
    def print():
        for i in CallCounter.calls:
            print(f'Function {i} called {CallCounter.calls[i]} times')

@CallCounter
def f1():
    pass

@CallCounter
def f2():
    pass

@CallCounter
def f3():
    pass

for i in range (10):
    f1()
    for i in range(10):
        f2()
        for i in range(10):
            f3()

CallCounter.print()
