# Создать список, состоящий из кубов нечётных чисел от 1 до 1000.
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

cube_list = [i**3 for i in range(1, 1001, 2)]
total_sum = 0

for list_number in cube_list:
    value = list_number
    digits_sum = 0
    while value > 0:
        digits_sum += value % 10
        value //= 10
    if digits_sum % 7 == 0:
        total_sum += list_number
print(total_sum)

total_sum = 0
for list_number in cube_list:
    value = list_number + 17
    digits_sum = 0
    while value > 0:
        digits_sum += value % 10
        value //= 10
    if digits_sum % 7 == 0:
        total_sum += list_number + 17
print(total_sum)
