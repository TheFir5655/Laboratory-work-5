import random
arr = [random.randint(1, 100) for i in range(10)]
even_numbers = []
for num in arr:
    if num % 2 == 0:
        even_numbers.append(num)
print(arr)
print(even_numbers)
even_numbers.sort()
print(even_numbers)