#1
print('#1')
k = [1, 2, 1, 2, 1, 2]
for i in range (len(k)):
    if 1 in k:
        k.remove(1)
    else: 
        break  
print(k)
print('\n')

#2
print('#2')
k = [1, 2, 1, 2, 1, 2]
while 1 in k:
    k.remove(1)
print(k)
print('\n')

#3
print('#3')
k = [1, 2, 1, 2, 1, 2]
for i in range(1,len(k),2):
    print(k[i], end = ', ')
print('\n')

#4
print('#4')
k = [1, 2, 1, 2, 1, 2]
print(k[1::2])
print('\n')

#5
print('#5')
k = [1, 2, 1, 2, 1, 2]
for i in range(len(k)-1,0,-2):
    print(k[i], end = ', ')
print('\n')

#6
print('#6')
k = [1, 2, 1, 2, 1, 2]
print(k[10:-10:-2])
print('\n')

#7
print('#7')
k = [1, 2, 1, 2, 1, 2]
c = [(i, k[i]) for i in range(len(k))]
print(c)
print('\n')

#8
print('#8')
k = [1, 2, 1, 2, 1, 2]
c = [(i, k[i]) for i in range(len(k))]
print(c, '\nsortowanie\n')
c.sort(key = lambda x: x[1])
print(c)
print('\n')

#9
print('#9')
k = [1, 2, 1, 2, 1, 2]
c = [(i, k[i])  for i in range(len(k)) if not k[i]%2]
print(c)
print('\n')

#10
print('#10')
k = [1, 2, 1, 2, 1, 2]
c = [(i, k[i]) if i > k[i] else (k[i], i) for i in range(len(k))]
print(c)
print('\n')