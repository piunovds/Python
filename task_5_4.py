src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for num, num_prev in zip(src[1:], src[:-1]) if num > num_prev]
print(result)
