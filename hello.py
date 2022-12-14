# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


day = int(input("Введите день недели: "))

if day > 0 and day < 6:
    print("Нет")
elif day > 5 and day < 8:
    print("Да")
else:
    print("Некоректно ввели день недели, попробуйте ещё раз")


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x,y,z, " - ",not (x or y or z) == (not x and not y and not z))

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите координаты Х "))
y = int(input("Введите координаты Y "))

if x > 0 and y > 0:
    print("x = ", x, "y =", y," -> 1")
elif x > 0 and y < 0:
    print("x = ", x, "y =", y," -> 2")
elif x < 0 and y < 0:
    print("x = ", x, "y =", y," -> 3")
elif x < 0 and y < 0:
    print("x = ", x, "y =", y," -> 4")
else:
    print("Error")

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def sayMeChetvert (text):
    a = float(input(text))
    return a

a = sayMeChetvert("Введите четверть: ")
if a == 1:
    print("x = [0, 100]",  " y = [0, 100]")
elif a == 2:
    print("x = [0, 100]",  " y = [0, -100]")
elif a == 3:
    print("x = [0, -100]",  " y = [0, -100]")
elif a == 4:
    print("x = [0, 100]",  " y = [0, -100]")

else:
    print("Попробуйте ещё раз, нужно ввести четверть от 1 до 4")


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def sayNumberXandY(text):
    a = float(input(text))
    return a

def square(a1, b1, a2, b2):
    import math
    distans1 = math.sqrt((a1-a2)**2 + (b1-b2)**2)
    return distans1

def CalculateNumberTwo(a):
    n = int(a * 100)
    n = float(n / 100)
    return n

x1 = sayNumberXandY('Введите координаты точки a по оси x1:')
y1 = sayNumberXandY('Введите координаты точки a по оси y1:')
x2 = sayNumberXandY('Введите координаты точки b по оси x2:')
y2 = sayNumberXandY('Введите координаты точки b по оси y2:')

c = square(x1,y1,x2,y2)
print (CalculateNumberTwo(c))

