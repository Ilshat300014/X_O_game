# Создаем поле
field = [['-' for i in range(4)] for j in range(4)]
field[0][0] = ' '
field[0][1] = '0'
field[0][2] = '1'
field[0][3] = '2'
field[1][0] = '0'
field[2][0] = '1'
field[3][0] = '2'

print('''
        
''')

# Вывод поля
for s in field:
    print(*s)

def show_field(func):
    def wrapper(*args):
        x_y = func(*args)
        for s in field:
            print(*s)
        return x_y
    return wrapper

@show_field
def set_position(pos, l):
    x = pos // 10
    y = pos % 10
    field[x + 1][y + 1] = l
    return int(f'{x + 1}{y + 1}')

def check(l):
    x = [i // 10 for i in l]
    y = [i % 10 for i in l]
    d_x = {i: x.count(i) for i in x}
    d_y = {i: y.count(i) for i in y}
    # Проверяем горизонтаь и вертикаль
    if 3 in d_x.values() or 3 in d_y.values():
        return True
    # Проверяем диагональ
    if 11 in l and 22 in l and 33 in l or \
       13 in l and 22 in l and 31 in l:
        return True
    return False

X_coor = [] # Ходы первого игрока
O_coor = [] # Ходы второго игрока
all_coor = [] # Все ходы

# Ход игры
def game(s):
    print(f'Ходит {s[1]} игрок:')
    pos = int(input())
    while 0 > pos // 10 or pos // 10 > 2 or 0 > pos % 10 or pos % 10 > 2:
        print("Введите значение в пределах границы поля!")
        pos = int(input())
    while pos in all_coor:
        print("Это ячейка уже занята, введите другое значение :(")
        pos = int(input())
    all_coor.append(pos)
    cor = set_position(pos, s[0])
    s[2].append(cor)
    if check(s[2]):
        return s[0]
    return False

def main():
    for i in range(9):
        s = ['X', 'первый', X_coor] if i == 0 or i % 2 == 0 else ['O', 'второй', O_coor]
        result = game(s)
        if result:
            print(f'{result} player win!')
            break
    if not result:
        print('Ничья!')

if __name__ == '__main__':
    main()