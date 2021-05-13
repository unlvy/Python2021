##### 1.
print('#1.')

class GameOfLife:

    def __init__(self, size, cellsSquare, iterations):
        self._size = size
        self._maxIteration = iterations
        self._cells = [[0 for i in range(self._size)] for j in range(self._size)]
        self._iteration = 0
        for i in range(cellsSquare):
            for j in range(cellsSquare):
                self._cells[(self._size - cellsSquare) // 2 + i][(self._size - cellsSquare) // 2 + j] = 1

    def print(self):
        strToPrint = ""
        for i in range(self._size):
            strToPrint += "|"
            for j in range(self._size):
                strToPrint += " " if self._cells[i][j] == 0  else "*" 
            strToPrint += "|\n"
        print(strToPrint)


    def calculateAliveNeighbors(self, row, column):
        result = 0
        if row != 0:
            result += self._cells[row - 1][column]
        if row != self._size - 1:
            result += self._cells[row + 1][column]
        if column != 0:
            result += self._cells[row][column - 1]
        if column != self._size - 1:
            result += self._cells[row][column + 1]
        return result

    def evolve(self):
        newCells = self._cells
        for i in range(self._size):
            for j in range(self._size):
                aliveNeighbors = self.calculateAliveNeighbors(i, j)
                if aliveNeighbors == 3:
                    newCells[i][j] = 1
                elif aliveNeighbors == 2 and self._cells[i][j] == 1:
                    newCells[i][j] = 1
                else:
                    newCells[i][j] = 0
        self._cells = newCells

    def play(self):
        while (self._iteration < self._maxIteration):
            self.evolve()
            self._iteration += 1
    
print("10x10")
game1 = GameOfLife(30, 10, 10)
game1.print()
game1.play()
game1.print()
print("11x11")
game2 = GameOfLife(30, 11, 10)
game2.print()
game2.play()
game2.print()

##### 2.
print('\n#2.')

class WrongArraySize(Exception):
    pass

class Tablica:

    def __init__(self, size, elements):
        if size != len(elements):
            raise WrongArraySize
        self._size = size
        self._elements = elements

    def __add__(self, other):
        additionRange = min(len(self._elements), len(other._elements))
        result = [self._elements[i] + other._elements[i] for i in range(additionRange)]
        return Tablica(additionRange, result)

    def __iadd__(self, other):
        additionRange = min(len(self._elements), len(other._elements))
        for i in range(additionRange):
            self._elements[i] += other._elements[i]
        return(self)

    def __getitem__(self, index):
        return self._elements[index]

    def __setitem__(self, index, value):
        if type(self._elements[index]) == type(value):
            self._elements[index] = value

    def getSize(self):
        return self._size

    def print(self):
        print(self._elements)

tab1 = Tablica(5, [1, 2, 3, 4, 5])
tab2 = Tablica(5, [2, 3, 4, 5, 6])

tab1.print()
tab2.print()

tab3 = tab1 + tab2
tab1 += tab2

tab1.print()
tab3.print()

tab1[0] = tab1[4] + tab1.getSize()
tab1.print()
