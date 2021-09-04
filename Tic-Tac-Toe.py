#Приветствие
def hello():
    print("<<<<<<<<<<<<>>>>>>>>>>>>")
    print("    Здравствуй, друг!   ")
    print("Предлагаю сыграть в мою ")
    print("      первую игру!      ")
    print("    КРЕСТИКИ-НОЛИКИ     ")
    print("<<<<<<<<<<<<>>>>>>>>>>>>")
    print("   Правила - просты    ")
    print("   x - номер строки    ")
    print("   y - номер столбца   ")
    print("________________________")


#Игровое поле
matrix = [[" "] * 3 for i in range (3)]

def show():
    print("----ПОЛЕ БОЯ----")
    print(f"   | 0 | 1 | 2 |")
    print(f"----------------")
    for i, row in enumerate (matrix):
        row_info = f" {i} | {' | '.join(row)} | "
        print(row_info)
        print(f"----------------")

#Запрос данных
def ask():
    while True:
        cords = input("   Ваш ход (введите через пробел x и y): ").split()
        if len(cords) != 2:
            print("Введите 2 координаты")
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазоана")
            continue

        if matrix[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y


#Проверка выигрышных комбинаций
def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(matrix[i][j])
        if symbols == ["X", "X", "X"]:
            show()
            print("ВЫИГРАЛ Х!!!")
            return True
        elif symbols == ["0", "0", "0"]:
            show()
            print("ВЫИГРАЛ 0!!!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(matrix[j][i])
        if symbols == ["X", "X", "X"]:
            show()
            print("ВЫИГРАЛ Х!!!")
            return True
        elif symbols == ["0", "0", "0"]:
            show()
            print("ВЫИГРАЛ 0!!!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(matrix[i][i])
        if symbols == ["X", "X", "X"]:
            show()
            print("ВЫИГРАЛ Х!!!")
            return True
        elif symbols == ["0", "0", "0"]:
            show()
            print("ВЫИГРАЛ 0!!!")
            return True

    symbols = []
    for i in range(3):
        symbols.append(matrix[i][2-i])
    if symbols == ["X", "X", "X"]:
        show()
        print("ВЫИГРАЛ Х!!!")
        return True
    elif symbols == ["0", "0", "0"]:
        show()
        print("ВЫИГРАЛ 0!!!")
        return True

    return False

#Заполнение поля и сборка игры
hello()
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")

    x, y = ask()

    if num % 2 == 1:
        matrix[x][y] = "X"
    else:
        matrix[x][y] = "0"

    if check_win():
        break

    if num == 9:
        show()
        print("НИЧЬЯ!")
        break




