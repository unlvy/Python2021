##### 1.
print('#1.')

def fun1(fileName, n):
    with open(fileName) as file:
        lines = file.readlines()
        print(f'Pierwsze {n} linie pliku:')
        print(lines[:n])
        print(f'Ostatnie {n} linie pliku:')
        print(lines[-n:])
        print(f'Co {n} linia pliku:')
        print(lines[::n])
        print(f'Wyraz na pozycji {n} z kazdego wiersza:')
        print([i.split()[n-1] for i in lines])
        print(f'Znak na pozycji {n} z kazdego wiersza:')
        print([i[n-1] for i in lines])

fun1('file1.txt', 2)

##### 2.
print('\n#2.')
import glob
flag = False
values = []
for f in glob.glob('./data*.in'):
    with open(f) as file:
        lines = file.readlines()
        if flag:
            for i in range(len(lines)):
                values[i] += float(lines[i].split()[0])
        else:
            flag = True
            for i in lines:
                values.append(float(i.split()[0]))

average = []
deviation = []
indexes = []

for i in range(len(values)):
    indexes.append(i)
    average.append(values[i]/len(values))
    deviation.append(0.05)

with open('file2.txt', 'w') as file:
    for i in indexes:
        file.write(str(i) + '\t' + str(average[i]) + '\n')

##### 3.
print('\n#3.')

def fun3():
    with open('file3.py', 'w') as file:
        file.writrelines('''import matplotlib.pyplot as plt
                            #wyrysowanie krzywej y(x), 'o' oznacza styl punktu
                            plt.plot(indexes, values, 'o')
                            #wyrysowanie krzywej y(x) wraz z niepewnościami
                            plt.errorbar(x, y, marker='*', yerr=dy)
                            #opis osi
                            plt.xlabel('x')
                            #zapis do pliku, format określony przez rozszerzenie w nazwie
                            plt.savefig('res.pdf')')''')

##### 4.
years = []
results = {}
print('\n#4.')
for f in glob.glob('./rank/*.txt'):
    with open(f) as file:
        lines = file.readlines()
        years.append(f[7:11])
        for i in lines:
            if len(i.split()) > 1:
                if i.split()[0] not in results:
                    results[i.split()[0]] = []
                results[i.split()[0]].append(i.split()[1])
            

with open('file4.txt', 'w') as file:
    for i in years:
        file.write('\t' + str(i))
    for i in results:
        file.write('\n' + str(i))
        file.write(str(results[i]))