import numpy
grid =[[0,0,9,0,0,0,5,0,0],
       [0,0,0,0,3,0,0,9,4],
       [3,1,6,0,4,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,7,0,9,0,2,8,0],
       [6,0,1,0,8,4,7,0,0],
       [0,7,0,0,0,5,0,0,6],
       [0,2,0,7,0,0,0,0,0],
       [1,6,5,0,0,0,0,0,0]]

print(grid)
print(numpy.matrix(grid),'\n')


def possible(x, y, n):  # Функция проверки можно ли поставить число n на позицию x, y
    global grid
    for i in range(9):
        if grid[y][i] == n:  # Проверка есть ли число n в строке
            return False
    for i in range(9):
        if grid[i][x] == n:  # Проверка есть ли число т в столбце
            return False
    x0 = (x//3)*3  # Находим х координату нужного квадрата
    y0 = (y//3)*3  # Находим у координату нужного квадрата
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+i] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x,y,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(numpy.matrix(grid))
    input("Ещё решение?")

solve()