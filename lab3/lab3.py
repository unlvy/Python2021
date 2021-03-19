##### 1
print('#1')
import sys
if (len(sys.argv) >= 2):
    s = ''.join(sys.argv[1:])
    print(s)
else :
    print('Blad! Program zostal uruchomiony bez podania parametrow\n')
    print('Przykladowe wywolanie:\n\'python main.py arg1 arg2\'  ')
    sys.exit()
print('\n')

##### 2
print('#2')
lowerLetters = [i for i in s if i.islower()]
print('lowerLetters: ', lowerLetters)
upperLetters = [i for i in s if i.isupper()]
print('upperLetters: ', upperLetters)
numbers = [i for i in s if i.isnumeric()]
print('numbers: ', numbers)
nonLetters = [i for i in s if not i.isalpha()]
print('nonLetters: ', nonLetters)
print('\n')

##### 3
print('#3')
lonelyLowerLetters = []
for i in lowerLetters:
    if i not in lonelyLowerLetters:
        lonelyLowerLetters.append(i)
print('lonelyLetters: ', lonelyLowerLetters)
lowerLettersWithCount = [(i, lowerLetters.count(i)) for i in lonelyLowerLetters]
print('lowerLettersWithCount: ', lowerLettersWithCount)
print('\n')

##### 4
print('#4')
lowerLettersWithCountSorted = lowerLettersWithCount.copy()
lowerLettersWithCountSorted.sort(key = lambda x : x[1], reverse = True)
print('lowerLettersWithCountSorted: ', lowerLettersWithCountSorted)
print('\n')

##### 5
print('#5')
samogloski = 'aeiouyAEIOUY'
a, b = 0, 0
for i in lowerLetters:
    if i in samogloski:
        a += 1
    else:
        b += 1 
for i in upperLetters:
    if i in samogloski:
        a += 1
    else:
        b += 1
linear = [(int(i), a * int(i) + b) for i in numbers]
print('a = ', a, ', b = ', b)
print('linear: ', linear)

print('\n')

##### 6
print('#6')
meanX = sum(float(i[0]) for i in linear) / len(linear)
meanY = sum(float(i[1]) for i in linear) / len(linear)

D = sum((float(i[0]) - meanX)**2 for i in linear)
a1 = sum((float(i[1]) * (float(i[0]) - meanX)) for i in linear) / D
b1 = meanY - a * meanX

print('D: ', D)
print('a: ', a1)
print('b: ', b)
