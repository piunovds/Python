# Дан список. Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов.

my_list = ['at', '5', 'hours', '17', 'minuts', 'air', 'temperature', 'was', '+5', 'degrees']

idx = 0
while idx < len(my_list):
    if all(letter in '0123456789+-' for letter in my_list[idx]):
        if (my_list[idx][0] in '+-'):
            my_list[idx] = my_list[idx].zfill(3)
        else:
            my_list[idx] = my_list[idx].zfill(2)
        my_list.insert(idx, '"')
        my_list.insert(idx+2, '"')
        idx += 2
    idx += 1

print(my_list)
#new_str = ' '.join(my_list)
print(' '.join(my_list))
