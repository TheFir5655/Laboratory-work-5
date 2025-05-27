x = int(input("Вевдите число: "))
y = int(input("Введите число: "))
def count ():
    folded = 0
    for i in range(x, y +1):
        folded += i
    print(f"Сложенные числа: {folded}")
count()