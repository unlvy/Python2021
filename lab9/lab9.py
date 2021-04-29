##### 1.
print('#1.')

##### 2.
print('\n#2.')
from romanArabic import fromArabicToRoman
help(fromArabicToRoman)
number = 1273 #MCCLXXIII
print(f'1273 = {fromArabicToRoman(number)}')

##### 3.
print('\n#3.')
from romanArabic import fromRomanToArabic
help(fromRomanToArabic)
number = 'MCMXLI' #1941
print(f'MCMXLI = {fromRomanToArabic(number)}')