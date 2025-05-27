x = int(input())
y = int(input())

r = int(input()) #Тут радиус

distance = (x * x + y * y) ** 0.5
if distance <= r:
    print("принадлежит")
else:
    print("не принадлежит")