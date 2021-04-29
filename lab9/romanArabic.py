# 2

romanAsArabic = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), 
                ("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400), 
                ("D", 500), ("CM", 900), ("M", 1000)]

def fromArabicToRoman(number):
    ''' 
    zwraca lancuch zawierajacy przekazana jako argument wywolania
    liczbe zapisana w systemie rzymskim
    '''
    result = ""
    currentPos = len(romanAsArabic) - 1
    while number > 0:
        while romanAsArabic[currentPos][1] > number:
            currentPos -= 1
        number -= romanAsArabic[currentPos][1]
        result += romanAsArabic[currentPos][0]  
    return result

print(fromArabicToRoman(111))

# 3

def fromRomanToArabic(number):
    ''' 
    zwraca liczbe bedaca zapisana w systemie arabskim liczba przekazana
    jako argument wywolania (bedaca w systemie rzymskim)
    '''
    result, i, j = 0, 0, len(romanAsArabic) - 1
    while i < len(number):
        if (number[i:].startswith(romanAsArabic[j][0])):
            result += romanAsArabic[j][1]
            i += len(romanAsArabic[j][0])
        else:
            j -= 1
    return result