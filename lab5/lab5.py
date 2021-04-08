#1
import random
import sys
print('#1.')
def fun1(s):
    # ascii: male litery 97-122 (x 120), cyfry 48-57
    d = dict((i + 97, random.randrange(48, 58)) for i in range(26))
    d.pop(120)
    s = s.translate(d)
    print(s)
    args = [random.randrange(0, 10) for i in range(10)]
    return [(x, eval(s)) for x in args]

print(fun1(sys.argv[1]))

#2
print('\n#2.')
def fun2(*args):
    result = []
    for i in args[0]:
        for j in args[1:]:
            if i not in j:
                break
        else:
            result.append(i)
    return result

print(fun2([1,2,3], (1,3,5), [3,2]))
print(fun2([1,2,3], (1,3,5), [3,2,1]))

#3
print('\n#3.')
def fun3(seq1, seq2, flag = True):
    if flag:
        return [(seq1[i], seq2[i]) for i in range(min(len(seq1), len(seq2)))]
    elif len(seq1) > len(seq2):
        return [(seq1[i], seq2[i]) if i < len(seq2) else (seq1[i], None) for i in range(len(seq1))]
    else:
        return [(seq1[i], seq2[i]) if i < len(seq1) else (None, seq2[i]) for i in range(len(seq2))]

sequence1, sequence2 = [0, 1, 2, 3, 4], ['0', '1', '2']

print(fun3(sequence1, sequence2))
print(fun3(sequence1, sequence2, False))

#4
print('\n#4.')
def fun4(cash, nominalValues = (10,5,2)):
    i = 0
    result = []
    while cash > 0:
        if cash >= nominalValues[i]:
            cash -= nominalValues[i]
            result.append(nominalValues[i])
        elif i < len(nominalValues) - 1:
            i += 1
        else:
            result.append(f'rest: {cash}')
            break
    return result

print(fun4(27))
print(fun4(27, (31, 11, 3)))

#5
print('\n#5.')
def fun5(number, minimum, maximum, flag = 'r'):
    n = maximum + 1
    steps = 0
    while n != number:
        steps += 1
        n = random.randint(minimum, maximum) if flag == 'r' else (minimum + maximum) // 2
        if flag != 'r':
            minimum, maximum = (minimum, (minimum + maximum) // 2) if n > number else ((minimum + maximum) // 2, maximum)
    return f'number = {n}, steps = {steps}, mode = {flag}'

print(fun5(37, 0, 100))
print(fun5(37, 0, 100, 'not r'))