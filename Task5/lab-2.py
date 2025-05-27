num = [3, -5, 2, 7, -1, 4, -2]

def calculate_stats(num):
    sum_positive = sum(num for num in num if num > 0)
    min_index = num.index(min(num))
    max_index = num.index(max(num))
    start = min(min_index, max_index)
    end = max(min_index, max_index)
    product = 1
    for num in num[start + 1: end]:
        product *= num

    return sum_positive, product

sum_pos, prod = calculate_stats(num)
print(sum_pos, prod)