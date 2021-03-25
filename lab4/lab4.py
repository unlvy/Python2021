#1
k = 4
print('#1')
import random
s = dict.fromkeys(range(k), 0)
l = [random.randrange(k) for i in range(4 * k)]
shuffledL = l.copy()
for i in range(100):
    random.shuffle(shuffledL)
    for i in range(len(l)):
        if l[i] == shuffledL[i]:
            s[l[i]]+=1
print('s =', s)

#2
print('\n#2')
randomStr = ''
for i in range(10):
    randomStr += chr(random.randint(97, 122))
randomStr = '.'.join(randomStr)
print(randomStr)

#3
print('\n#3a')
l = [random.randrange(20) for i in range(100)]
s = {}
for i, j in enumerate(l):
     s.setdefault(j, []).append(i)
print(s)

print('\n#3b')
l = [random.randrange(20) for i in range(100)]
s = {}
for i in range(len(l)):
    s.setdefault(l[i], []).append(i)
print(s)

#4
print('\n#4')
s = {}
for i in range(1000):
    number = int(10**(random.randint(3, 6)) * random.uniform(0.1, 1))
    numberInStr = str(number)
    if numberInStr == numberInStr[::-1]:
        s.setdefault(number, True)
print(s)

#5
print('\n#5')
s1 = {}
s2 = {}
for i in range(10):
    s1.setdefault(i, random.randrange(1, 100))
    s2.setdefault(i, random.randrange(1, 100))
s1 = {j: i for i, j in s1.items()}
s2 = {j: i for i, j in s1.items()}
s3 = {}
for i in s1.keys():
    if i in s2.keys():
       s3.setdefault(i, (s1[i], s2[i]))
print(s3)