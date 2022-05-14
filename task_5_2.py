def odd_nums_generator(max_num):    
    for num in range(1, max_num + 1, 2):
        yield num


odd_to_17 = odd_nums_generator(17)
print(next(odd_to_17))
print(next(odd_to_17))
print(next(odd_to_17))
print(odd_to_17.__next__())
print(odd_to_17.__next__())
print(odd_to_17.__next__())
print(odd_to_17.__next__())
print(odd_to_17.__next__())
print(odd_to_17.__next__())


odd_nums = (num for num in range(1, 100, 2))
print(*odd_nums)
