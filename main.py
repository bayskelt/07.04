# task_1
print('task_1')
n = 0
q = 0
a = float(input('Введіть початок проміжку: '))
b = float(input('Введіть кінець проміжку: '))
print('Введіть 9 дійсних чисел:')
while n < 9:
    n += 1
    x = float(input())
    if a <= x <= b:
        q += 1
print(f'Кількість чисел, що належать проміжку [{a}; {b}]  = {q}')

# task_2
print('\ntask_2')
q = 0
n = int(input('Скільки цілих чисел ви хочете ввести: '))
print(f'Введіть {n} цілих чисел:')
while q < n:
    q += 1
    x = int(input())
    if (x ** 2) > 10:
        print(f'Квадрат з {x} більший 10')
    else:
        print(f'Квадрат з {x} менший або рівний 10')

# task_3
print('\ntask_3')
f = 0
s = 0
x = int(input("Введіть натуральне число: "))
if x > 0:
    while x > 0:
        if x % 10 == 5:
            f += 1
        elif x % 10 == 7:
            s += 1
        x = x // 10
print(f'Кількість цифр 5 в числі = {f}')
print(f'Кількість цифр 7 в числі = {s}')