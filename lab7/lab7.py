#2
print('\n#2.')
import random
N = 100
seq = [random.randint(0,1) for _ in range(N)]

def gen2(seq):
    for i in seq:
        if i != 0:
            break
    zeros = 0
    for i in seq:
        if i == 0:
            zeros += 1
        elif zeros != 0:
            yield zeros
            zeros = 0

d = list(gen2(seq))
print('average dist: ', sum(d)/len(d))

#3
print('\n#3.')

def gen3a():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def gen3b(seq):
    for i in seq:
        if i % 2:
            yield i

def gen3c(seq, value):
    for i in seq:
        if i <= value:
            yield i
        else:
            break


print(list(gen3c(gen3b(gen3a()), 100)))

#4
print('\n#4.')

def gen4(start, stop = None, step = None):
    start = float(start)
    if stop is None and step is None:
        stop = start
        step = 1.0
        start = 0.0
    elif step is None:
        step = 1.0
    if start < stop:
        if step <= 0.0:
            return
        value = start
        while value < stop:
            yield value
            value += step
    elif step >= 0.0:
        return
    else:
        value = start
        while value > stop:
            yield value
            value -= step
    
print(list(range(7)))
print(list(gen4(7)))

print(list(range(-7)))
print(list(gen4(-7)))

print(list(range(2, 7)))
print(list(gen4(2, 7)))

print(list(range(7, 2)))
print(list(gen4(7, 2)))

print(list(range(2, 7, 2)))
print(list(gen4(2, 7, 2)))

print(list(range(2, 7, -2)))
print(list(gen4(2, 7, -2)))


print(list(range(7, 7, 2)))
print(list(gen4(7, 7, 2)))


print(list(range(2, 7, -2)))
print(list(gen4(2, 7, -2)))

#5
print('\n#5.')
import math

def gen5():
    u, x0, a, i, x = 0.0, 1.0, 0.05, 1, 1.0
    while x < 1.5:
        u += a / x
        x = x0 + i * a
        i += 1
        yield f'x = {x}, log(x) ~ {u}, log(x) = {math.log(x)}'

for i in gen5():
    print(i)