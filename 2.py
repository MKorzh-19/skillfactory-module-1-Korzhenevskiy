matrix = [[' ', 0, 1, 2]
          ,[0, '-', '-', '-']
          ,[1, '-', '-', '-']
          ,[2, '-', '-', '-']]

matrix_f_g = matrix.copy()

def matrix_print():
    for row in matrix_f_g:
       for element in row:
           print(element, end = " ")
       print()

def check_win():
    win_cord = (((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)),
                ((1, 3), (2, 2), (3, 1)), ((1, 1), (2, 2), (3, 3)), ((1, 1), (2, 1), (3, 1)),
                ((1, 2), (2, 2), (3, 2)), ((1, 3), (2, 3), (3, 3)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(matrix_f_g[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

matrix_print()

count = 0
while True:
    b = int(input("Игрок 1, выберите ваш ход по горизонтали (от 0 до 2):" ))
    a = int(input("Игрок 1, выберите ваш ход по вертикали (от 0 до 2):" ))
    if (0 <= a <= 2) and (0 <= b <= 2) and matrix_f_g[a + 1][b + 1] == '-':
        matrix_f_g[a+1][b+1] = 'X'
        matrix_print()
    else:
        print('Ход недоступен, начните заново!')
        break
    if check_win():
        break
    b = int(input("Игрок 2, выберите ваш ход по горизонтали (от 0 до 2):"))
    a = int(input("Игрок 2, выберите ваш ход по вертикали (от 0 до 2):"))
    if (0 <= a <= 2) and (0 <= b <= 2) and matrix_f_g[a + 1][b + 1] == '-':
        matrix_f_g[a + 1][b + 1] = 'О'
        matrix_print()
    else:
        print('Ход недоступен, начните заново!')
        break
    if check_win():
        break
    count += 1
    if count == 9:
        print('Ничья')
        break






























